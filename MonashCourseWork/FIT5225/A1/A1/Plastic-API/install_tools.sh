#!/bin/bash
set -euo pipefail

# Installs controller-VM tools needed to provision infrastructure and manage the K8s cluster.
# Target OS: Ubuntu/Debian-based VM.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SSH_KEY="$SCRIPT_DIR/id_ed25519"
KUBECTL_VERSION="${KUBECTL_VERSION:-v1.30}"

log() {
  echo "--- $* ---"
}

require_sudo() {
  if ! sudo -n true 2>/dev/null; then
    echo "This script needs sudo access. You may be prompted for your password." >&2
    sudo true
  fi
}

install_base_packages() {
  log "Updating system packages"
  sudo apt-get update
  sudo apt-get install -y --no-install-recommends \
    ca-certificates \
    software-properties-common \
    apt-transport-https \
    git \
    curl \
    wget \
    unzip \
    vim \
    python3 \
    python3-pip \
    python3-venv \
    python3-apt \
    gnupg \
    jq \
    lsb-release \
    openssh-client
}

install_hashicorp_tools() {
  log "Installing Terraform and Ansible"

  wget -qO- https://apt.releases.hashicorp.com/gpg | \
    gpg --dearmor | \
    sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg >/dev/null

  echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
    sudo tee /etc/apt/sources.list.d/hashicorp.list >/dev/null

  sudo apt-get update
  sudo apt-get install -y --no-install-recommends terraform ansible
}

install_kubectl() {
  log "Installing kubectl"

  sudo mkdir -p /etc/apt/keyrings
  curl -fsSL "https://pkgs.k8s.io/core:/stable:/${KUBECTL_VERSION}/deb/Release.key" | \
    sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

  echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/${KUBECTL_VERSION}/deb/ /" | \
    sudo tee /etc/apt/sources.list.d/kubernetes.list >/dev/null

  sudo apt-get update
  sudo apt-get install -y --no-install-recommends kubectl
}

generate_ssh_key_if_missing() {
  log "Checking SSH key"

  if [[ -f "$SSH_KEY" && -f "$SSH_KEY.pub" ]]; then
    chmod 600 "$SSH_KEY"
    chmod 644 "$SSH_KEY.pub"
    echo "Using existing SSH key: $SSH_KEY"
    return
  fi

  echo "SSH key not found. Generating: $SSH_KEY"
  ssh-keygen -t ed25519 -f "$SSH_KEY" -N "" -C "fit5225-controller"
  chmod 600 "$SSH_KEY"
  chmod 644 "$SSH_KEY.pub"
}

configure_local_path() {
  log "Ensuring local bin path is available"
  export PATH="$PATH:$HOME/.local/bin"
  if ! grep -qxF 'export PATH="$PATH:$HOME/.local/bin"' "$HOME/.bashrc"; then
    echo 'export PATH="$PATH:$HOME/.local/bin"' >> "$HOME/.bashrc"
  fi
}

check_cloud_credentials() {
  log "Checking Terraform cloud credentials"

  if [[ -n "${OCI_CONFIG_FILE:-}" || -f "$HOME/.oci/config" ]]; then
    echo "OCI config detected."
  else
    cat <<'MSG'
Warning: No OCI config detected.
Terraform may fail unless your provider credentials are already configured.
Expected one of:
  - ~/.oci/config
  - OCI_CONFIG_FILE=/path/to/config
  - other OCI_* environment variables required by your Terraform provider
MSG
  fi
}

print_versions() {
  log "Verification"
  terraform -version | head -n 1
  ansible --version | head -n 1
  kubectl version --client=true --output=yaml | grep gitVersion || true
  python3 --version
  pip3 --version
  jq --version
  ssh -V 2>&1 | head -n 1
}

main() {
  require_sudo
  install_base_packages
  install_hashicorp_tools
  install_kubectl
  generate_ssh_key_if_missing
  configure_local_path
  check_cloud_credentials
  print_versions
  log "Installation complete"

  cat <<EOF2

Next typical steps:
  ./deploy_vm.sh apply
  ./run_cluster_setup.sh

After the cluster is created, copy kubeconfig from the master if you want kubectl on this controller VM.
EOF2
}

main "$@"

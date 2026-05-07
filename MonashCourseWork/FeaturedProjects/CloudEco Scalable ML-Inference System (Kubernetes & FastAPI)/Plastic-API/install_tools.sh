#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SSH_KEY="$SCRIPT_DIR/id_ed25519"
GCP_KEY="$SCRIPT_DIR/gcp-key.json"
KUBECTL_VERSION="${KUBECTL_VERSION:-v1.30}"

log() { echo "--- $* ---"; }

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
    ca-certificates apt-transport-https software-properties-common \
    git curl wget unzip vim python3 python3-pip python3-venv python3-apt \
    gnupg jq lsb-release openssh-client
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

check_gcp_credentials() {
  log "Checking GCP Terraform credentials"
  if [[ -f "$GCP_KEY" ]]; then
    jq -e '.type == "service_account" and .client_email and .private_key and .project_id' "$GCP_KEY" >/dev/null \
      && echo "GCP service account key found: $GCP_KEY" \
      || { echo "ERROR: gcp-key.json exists but does not look like a valid service-account JSON file." >&2; exit 1; }
  else
    cat <<MSG
WARNING: $GCP_KEY was not found.
Terraform will fail unless you provide a valid GCP service account key named gcp-key.json in this directory.
Do not commit or submit this key.
MSG
  fi
}

print_versions() {
  log "Verification"
  terraform -version | head -n 1
  ansible --version | head -n 1
  kubectl version --client=true --output=yaml | grep gitVersion || true
  python3 --version
  jq --version
  ssh -V 2>&1 | head -n 1
}

main() {
  require_sudo
  install_base_packages
  install_hashicorp_tools
  install_kubectl
  generate_ssh_key_if_missing
  check_gcp_credentials
  print_versions
  log "Installation complete"
}

main "$@"

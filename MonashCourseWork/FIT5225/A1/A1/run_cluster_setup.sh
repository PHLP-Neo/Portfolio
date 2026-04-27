#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INVENTORY="${1:-$SCRIPT_DIR/hosts.ini}"
SSH_KEY="$SCRIPT_DIR/id_ed25519"
KNOWN_HOSTS="$HOME/.ssh/known_hosts"

if [[ ! -f "$SSH_KEY" ]]; then
  echo "SSH private key not found: $SSH_KEY" >&2
  exit 1
fi

if [[ ! -f "$INVENTORY" ]]; then
  echo "Inventory file not found: $INVENTORY" >&2
  exit 1
fi

cleanup_known_hosts() {
  echo "--- Cleaning stale SSH host keys from known_hosts ---"
  grep -E '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' "$INVENTORY" | awk '{print $1}' | while read -r host; do
    [[ -z "$host" ]] && continue
    ssh-keygen -R "$host" >/dev/null 2>&1 || true
  done
}

seed_known_hosts() {
  echo "--- Seeding known_hosts with current host keys ---"
  mkdir -p "$(dirname "$KNOWN_HOSTS")"
  touch "$KNOWN_HOSTS"
  chmod 600 "$KNOWN_HOSTS"

  grep -E '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' "$INVENTORY" | awk '{print $1}' | while read -r host; do
    [[ -z "$host" ]] && continue
    ssh-keyscan -H "$host" >> "$KNOWN_HOSTS" 2>/dev/null || true
  done
}

run_playbook() {
  local playbook="$1"
  ansible-playbook -i "$INVENTORY" --private-key "$SSH_KEY" "$playbook"
}

echo "--- Using inventory: $INVENTORY ---"
echo "--- Using SSH key: $SSH_KEY ---"
cleanup_known_hosts
seed_known_hosts

echo "--- Step 1: Configure sudo access ---"
run_playbook 1_users.yml

echo "--- Step 2: Install Kubernetes prerequisites ---"
run_playbook 2_install_k8s.yml

echo "--- Step 3: Initialize control plane ---"
run_playbook 3_create_master.yml

echo "--- Step 4: Join workers and install CNI ---"
run_playbook 4_join_worker.yml

echo "--- Step 5: Deploy application ---"
run_playbook 5_deploy_app.yml

echo "--- Cluster setup complete ---"

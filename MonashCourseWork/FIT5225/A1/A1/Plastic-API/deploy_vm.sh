#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TF_PLAN="tfplan"
SSH_KEY="$SCRIPT_DIR/id_ed25519"

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || { echo "Error: '$1' is required but not installed." >&2; exit 1; }
}

require_cmd terraform
require_cmd jq

terraform_setup() {
  echo "--- Formatting Terraform files ---"
  terraform fmt

  echo "--- Initializing Terraform ---"
  terraform init

  echo "--- Validating Terraform configuration ---"
  terraform validate
}

generate_inventory() {
  echo "--- Generating Ansible inventory (hosts.ini) ---"
  IPS=$(terraform output -json ips | jq -r '.[]')

  MASTER_IP=$(echo "$IPS" | sed -n '1p')
  WORKER1_IP=$(echo "$IPS" | sed -n '2p')
  WORKER2_IP=$(echo "$IPS" | sed -n '3p')

  cat > "$SCRIPT_DIR/hosts.ini" <<EOF
[masters]
$MASTER_IP ansible_user=ubuntu ansible_ssh_private_key_file=$SSH_KEY

[workers]
$WORKER1_IP ansible_user=ubuntu ansible_ssh_private_key_file=$SSH_KEY
$WORKER2_IP ansible_user=ubuntu ansible_ssh_private_key_file=$SSH_KEY
EOF

  echo "--- Inventory written to $SCRIPT_DIR/hosts.ini ---"
  cat "$SCRIPT_DIR/hosts.ini"
}

case "${1:-apply}" in
  apply)
    terraform_setup
    echo "--- Creating Terraform plan ---"
    terraform plan -out="$TF_PLAN"
    echo "--- Applying Terraform plan ---"
    terraform apply -auto-approve "$TF_PLAN"
    rm -f "$TF_PLAN"
    generate_inventory
    ;;
  destroy)
    terraform_setup
    echo "--- Destroying Terraform-managed infrastructure ---"
    terraform destroy -auto-approve
    rm -f "$TF_PLAN"
    ;;
  *)
    echo "Usage: $0 [apply|destroy]"
    exit 1
    ;;
esac

#!/bin/bash
set -e

echo "--- Formatting Terraform files ---"
terraform fmt

echo "--- Initializing Terraform ---"
terraform init

echo "--- Validating Terraform configuration ---"
terraform validate

echo "--- Creating Terraform plan ---"
terraform plan -out=tfplan

echo "--- Applying Terraform plan ---"
terraform apply -auto-approve tfplan
rm -f tfplan

echo "--- Generating Ansible inventory (hosts.ini) ---"
IPS=$(terraform output -json ips | jq -r '.[]')

MASTER_IP=$(echo "$IPS" | sed -n '1p')
WORKER1_IP=$(echo "$IPS" | sed -n '2p')
WORKER2_IP=$(echo "$IPS" | sed -n '3p')

cat > hosts.ini <<EOF
[masters]
$MASTER_IP

[workers]
$WORKER1_IP
$WORKER2_IP

[all:vars]
ansible_user=ubuntu
ansible_ssh_private_key_file=$(pwd)/id_ed25519
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
EOF

echo "--- Generated hosts.ini ---"
cat hosts.ini

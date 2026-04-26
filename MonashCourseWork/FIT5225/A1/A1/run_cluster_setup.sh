#!/bin/bash
set -e

INVENTORY=${1:-hosts.ini}

echo "--- Using inventory: $INVENTORY ---"

echo "--- Step 1: Configure sudo access ---"
ansible-playbook -i "$INVENTORY" 1_users.yml

echo "--- Step 2: Install Kubernetes prerequisites ---"
ansible-playbook -i "$INVENTORY" 2_install_k8s.yml

echo "--- Step 3: Initialize control plane ---"
ansible-playbook -i "$INVENTORY" 3_create_master.yml

echo "--- Step 4: Join workers and install CNI ---"
ansible-playbook -i "$INVENTORY" 4_join_worker.yml

echo "--- Step 5: Deploy application ---"
ansible-playbook -i "$INVENTORY" 5_deploy_app.yml

echo "--- Cluster setup complete ---"

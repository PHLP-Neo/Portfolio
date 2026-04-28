#!/bin/bash
set -euo pipefail

echo "=== Ensuring scripts are executable ==="
chmod +x install_tools.sh deploy_vm.sh run_cluster_setup.sh

echo "=== Step 1: Installing tools ==="
./install_tools.sh

echo "=== Step 2: Provisioning infrastructure ==="
./deploy_vm.sh apply

echo "=== Step 3: Setting up cluster and deploying app ==="
./run_cluster_setup.sh

echo "=== Done ==="
echo "Next steps:"
echo "1. SSH into master OR copy kubeconfig to controller"
echo "2. Run: kubectl get nodes"
echo "3. Run Locust for benchmarking"
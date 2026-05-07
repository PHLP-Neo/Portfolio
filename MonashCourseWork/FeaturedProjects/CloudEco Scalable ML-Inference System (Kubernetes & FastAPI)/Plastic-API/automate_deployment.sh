#!/bin/bash
set -euo pipefail

FIREWALL_RESOURCE="google_compute_firewall.k8s_allow_all"
FIREWALL_ID="projects/fit5225-a1-494406/global/firewalls/k8s-firewall-fit5225"

chmod +x install_tools.sh deploy_vm.sh run_cluster_setup.sh

echo "=== Step 1: Installing controller tools ==="
./install_tools.sh

echo "=== Step 2: Initialising Terraform ==="
terraform init
terraform validate

echo "=== Step 3: Importing existing firewall into state if needed ==="
if terraform state show "$FIREWALL_RESOURCE" >/dev/null 2>&1; then
  echo "Firewall already managed by Terraform state."
else
  if terraform import "$FIREWALL_RESOURCE" "$FIREWALL_ID"; then
    echo "Firewall import successful."
  else
    echo "Firewall import did not succeed. This is OK if the firewall does not exist yet."
  fi
fi

echo "=== Step 4: Provisioning / reconciling infrastructure ==="
./deploy_vm.sh apply

echo "=== Step 5: Waiting briefly for fresh VMs to finish booting ==="
sleep 30

echo "=== Step 6: Setting up Kubernetes cluster and deploying app ==="
./run_cluster_setup.sh

echo "=== Done ==="
echo "Check with: kubectl get nodes && kubectl get pods -o wide && kubectl get svc"
echo "Access: http://<node-public-ip>:30001/docs"

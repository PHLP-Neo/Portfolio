#!/bin/bash
set -e

echo "--- Updating system packages ---"
sudo apt-get update
sudo apt-get install -y \
  software-properties-common \
  git \
  curl \
  wget \
  unzip \
  vim \
  python3 \
  python3-pip \
  gnupg \
  jq

echo "--- Adding HashiCorp GPG key ---"
wget -O- https://apt.releases.hashicorp.com/gpg | \
  gpg --dearmor | \
  sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null

echo "--- Adding HashiCorp repository ---"
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
  sudo tee /etc/apt/sources.list.d/hashicorp.list

echo "--- Installing Terraform and Ansible ---"
sudo apt-get update
sudo apt-get install -y terraform ansible

echo "--- Ensuring local bin path is available ---"
export PATH="$PATH:$HOME/.local/bin"
grep -qxF 'export PATH="$PATH:$HOME/.local/bin"' ~/.bashrc || \
  echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bashrc

echo "--- Verification ---"
terraform -version
ansible --version
python3 --version
pip3 --version
jq --version

echo "Installation complete!"

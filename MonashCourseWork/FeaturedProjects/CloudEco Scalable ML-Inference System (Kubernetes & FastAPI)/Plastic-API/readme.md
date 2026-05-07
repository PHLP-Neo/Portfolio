# Plastic API Deployment Guide

## Prerequisites

- Ubuntu-based VM running 22.04 (controller)
- Internet access
- A valid Google Cloud service account key (`gcp-key.json`) placed in the project root
- SSH key will be generated automatically (`id_ed25519`)

---

## Deployment Steps

```bash
sudo apt update
sudo apt install unzip -y

unzip Plastic-API.zip
cd Plastic-API

chmod +x automate_deployment.sh
./automate_deployment.sh
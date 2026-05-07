provider "google" {
  credentials = file("gcp-key.json")
  project     = "fit5225-a1-494406"
  region      = "australia-southeast1"
  zone        = "australia-southeast1-a"
}

locals {
  project_id   = "fit5225-a1-494406"
  region       = "australia-southeast1"
  zone         = "australia-southeast1-a"
  machine_type = "e2-custom-4-8192"
  ssh_user     = "ubuntu"
  ssh_pub_key  = file("${path.module}/id_ed25519.pub")
  node_tag     = "k8s-node"
}

resource "google_compute_instance" "k8s_node" {
  count        = 3
  name         = count.index == 0 ? "k8s-master" : "k8s-worker-${count.index}"
  machine_type = local.machine_type
  zone         = local.zone
  tags         = [local.node_tag]

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
      size  = 30
      type  = "pd-balanced"
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }

  metadata = {
    ssh-keys = "${local.ssh_user}:${local.ssh_pub_key}"
  }

  service_account {
    scopes = ["cloud-platform"]
  }

  allow_stopping_for_update = true
}

resource "google_compute_firewall" "k8s_allow_all" {
  name    = "k8s-firewall-fit5225"
  network = "default"

  allow {
    protocol = "tcp"
    ports = [
      "22",            # SSH
      "80",            # optional HTTP
      "443",           # optional HTTPS
      "6443",          # Kubernetes API server
      "2379-2380",     # etcd
      "10250",         # kubelet
      "10257",         # kube-controller-manager
      "10259",         # kube-scheduler
      "30000-32767"    # NodePort service range
    ]
  }

  allow {
    protocol = "udp"
    ports    = ["8472"] # Flannel VXLAN overlay, harmless if unused
  }

  allow {
    protocol = "icmp"
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = [local.node_tag]
}

output "ips" {
  value = google_compute_instance.k8s_node[*].network_interface[0].access_config[0].nat_ip
}

output "master_ip" {
  value = google_compute_instance.k8s_node[0].network_interface[0].access_config[0].nat_ip
}

output "worker_ips" {
  value = slice(google_compute_instance.k8s_node[*].network_interface[0].access_config[0].nat_ip, 1, 3)
}

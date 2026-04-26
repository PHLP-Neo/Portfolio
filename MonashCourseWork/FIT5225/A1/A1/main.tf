provider "google" {
  credentials = file("gcp-key.json")
  project     = "fit5225-a1-494406"
  region      = "australia-southeast1"
}

resource "google_compute_instance" "k8s_node" {
  count        = 3
  name         = count.index == 0 ? "k8s-master" : "k8s-worker-${count.index}"
  machine_type = "e2-custom-4-8192"
  zone         = "australia-southeast1-a"

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
      size  = 30
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }

  metadata = {
    ssh-keys = "ubuntu:${file("${path.module}/id_ed25519.pub")}"
  }

  tags = ["k8s-node"]
}

resource "google_compute_firewall" "k8s_allow_all" {
  name    = "k8s-firewall-fit5225"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["22", "6443", "2379-2380", "10250", "10257", "10259", "30000-32767"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["k8s-node"]
}

output "ips" {
  value = google_compute_instance.k8s_node[*].network_interface[0].access_config[0].nat_ip
}

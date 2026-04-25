provider "google" {
  credentials = file("gcp-key.json")
  project     = "fit5225-a1-494406"
  region      = "australia-southeast1"
}

# 自动创建 3 台 VM
resource "google_compute_instance" "k8s_node" {
  count        = 3
  name         = count.index == 0 ? "k8s-master" : "k8s-worker-${count.index}"
  machine_type = "e2-standard-4" # 2 vCPU, 8GB RAM，跑K8s很稳
  zone         = "australia-southeast1-a"

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
      size  = 30
    }
  }

  network_interface {
    network = "default"
    access_config {} # 分配公网IP
  }

  metadata = {
    # 这一步非常重要：自动把控制节点的公钥注入到 3 台新机器的 ubuntu 用户下
    ssh-keys = "ubuntu:${file("~/.ssh/id_ed25519.pub")}"
  }
}

# 自动配置防火墙（开放所有 K8s 需要的端口）
resource "google_compute_firewall" "k8s_allow_all" {
  name    = "k8s-firewall"
  network = "default"
  allow {
    protocol = "tcp"
    ports    = ["22", "6443", "2379-2380", "10250", "10257", "10259", "30000-32767"]
  }
  source_ranges = ["0.0.0.0/0"]
}

# 运行完后直接显示 3 台机器的公网 IP
output "ips" {
  value = google_compute_instance.k8s_node[*].network_interface[0].access_config[0].nat_ip
}

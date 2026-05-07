# CloudEco: Scalable ML-Inference for Marine Plastic Detection

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)](https://www.terraform.io/)

##  Project Overview
CloudEco is a high-performance, cloud-native inference system designed to detect marine plastic pollution in real-time. The system utilizes a **YOLO (You Only Look Once)** object detection model to identify plastic bags, bottles, and general waste in image payloads [cite: 23, 27, 50].

This project demonstrates a full-scale DevOps pipeline, including **Infrastructure as Code (IaC)**, **Docker optimization**, and **Kubernetes orchestration** [cite: 32, 33, 91, 98].

##  Technical Architecture
The system is built to handle high-concurrency traffic by decoupling the web interface from the heavy computational requirements of ML inference.

* **API Layer:** Developed with **FastAPI**, featuring asynchronous endpoints for standard JSON predictions (`/api/predict`) and base64-encoded annotated images (`/api/annotate`) [cite: 31, 55, 85].
* **Inference Engine:** Integration of the **Ultralytics YOLO** engine, specifically optimized to run on CPU-only environments within containers to minimize bloat [cite: 87, 93].
* **Orchestration:** Managed via **Kubernetes** with a 1-master, 2-worker node configuration [cite: 100].
* **Infrastructure:** Provisioned using **Terraform/Ansible** to automate the creation of VCNs, subnets, and internet gateways [cite: 9, 33, 40].

##  Performance & Scalability
A key component of this project was an **empirical benchmark study** using **Locust** to determine system saturation points [cite: 34, 112, 116].

* **Baseline Performance:** Engineered to meet or exceed the performance baseline of **5-10 Queries Per Second (QPS)** per 1 vCPU pod [cite: 13].
* **Horizontal Scaling:** Evaluated system behavior across 1, 2, 4, and 8 pod configurations to measure scaling efficiency and latency degradation [cite: 118, 126].
* **Optimization:** Implemented efficient **event-loop management** to prevent CPU-bound YOLO inference from blocking the FastAPI asynchronous event loop, ensuring minimal latency queuing [cite: 5, 115].

##  Repository Structure
* `/api`: FastAPI source code and YOLO integration [cite: 144].
* `/terraform`: IaC scripts for cloud resource provisioning [cite: 148].
* `/k8s`: Kubernetes Deployment and Service manifests [cite: 145].
* `/benchmarks`: Locust load-generation scripts and the **Empirical Benchmark Report** [cite: 140, 146].

---
*This project was developed for FIT5225 at Monash University and validated through a live technical interview demonstrating mastery of cloud architecture and container optimization [cite: 17, 21].*

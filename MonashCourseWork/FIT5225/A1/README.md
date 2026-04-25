# FIT5225 2026 S1 Assignment 1

## CloudEco: An Environmental Machine Learning-Based Cloud Application in Container Orchestration

**Due date:** 29 April 2026, Wednesday, Week 8, 23:55

## 1. Synopsis and Background

Environmental monitoring increasingly relies on edge-to-cloud computer vision architectures to detect and track ecological events such as bushfires, marine plastic pollution, urban waste accumulation, and wildlife movements. These complex systems utilise deep neural networks, specifically single-stage object detectors such as YOLO (You Only Look Once), to identify, classify, and localise objects in images in real time.

This project, titled **CloudEco**, requires the development of a highly scalable, web-based machine-learning inference system hosted on public clouds. End users simulated by automated test scripts will submit images to your RESTful web service via HTTP POST requests. The system will process these images using pre-trained environmental machine learning models and return a structured payload detailing the detected objects, alongside an annotated image.

The web service must be developed using Python’s FastAPI framework. The application will be containerised using Docker and orchestrated using a Kubernetes cluster. To align with modern DevOps practices, you are strongly encouraged to provision your networking and cluster infrastructure using Infrastructure-as-Code (IaC) tools such as Terraform or Ansible. Finally, the system’s performance will be rigorously tested. By utilising the load-generation tool Locust, you will benchmark your service under varying degrees of concurrent demand and resource availability by scaling the number of active Kubernetes pods within your cluster.

## 2. Assignment Objectives

This assignment is designed to evaluate competency in cloud-native development, distributed systems, and performance engineering, encompassing the following core objectives:

1. API Development: Constructing a Python-based RESTful API using FastAPI to handle image payloads, perform blocking or asynchronous ML inference safely, and return structured JSON and base64-encoded annotated images.
2. Containerisation: Packaging the Python application, model weights, and system dependencies into an optimised, lightweight Docker image.
3. Infrastructure as Code (IaC): Automating the provisioning of cloud resources and allocation policies using Terraform, Ansible, or Chef.
4. Container Orchestration: Deploying the containerised application, configuring Kubernetes Deployments and Services (LoadBalancer), and managing strict pod resource requests and limits.
5. Performance Benchmarking: Using Locust to simulate high-concurrency traffic and measure system latency, throughput (queries per second), and failure rates while keeping hardware limits in mind.
6. Empirical Reporting: 500 words analysing system bottlenecks, processing efficiency, and horizontal scaling characteristics in a concise, data-driven benchmark report.

## 3. Model Allocation Strategy

To ensure diversity in system testing and prevent widespread code duplication, you are assigned one of four environmental YOLO models based on the last digit of your Monash Student ID number. You will be provided with the pre-trained model weights and source code for your specific model. You are not required to train or fine-tune the model; your task is purely focused on cloud deployment, inference integration, and architectural scaling.

| Student ID Ending Digit | Assigned Environmental Model | Target Detection Classes |
|---|---|---|
| 0 or 5 | Model 1 | Wildfire Smoke Detection: Fire, Smoke |
| 1, 4, or 6 | Model 2 | Marine Plastic Pollution: Plastic Bag, Plastic Bottle, Other Waste |
| 2 or 7 | Model 3 | Urban Waste Detection: Glass, Metal, Paper, Plastic, General Waste |
| 3, 8, or 9 | Model 4 | Wildlife Detection: Elephant, Buffalo, Rhino, Zebra |

## 4. The Web Service Architecture

You must develop a RESTful API using the FastAPI framework. The server must be capable of efficiently handling multiple concurrent clients. The web service creates asynchronous task handling for each incoming request, utilising the YOLO engine to detect objects in the image.

### 4.1 Inference JSON API (`/apipredict`)

Clients will send an HTTP POST request containing a JSON object with a unique identifier (e.g., a UUID) and a base64-encoded image. Binary image data cannot be directly transmitted in standard JSON, necessitating this encoding translation. The web service must decode the base64 string into a NumPy array or an OpenCV image, pass it through the assigned YOLO model, and return a JSON object containing the bounding boxes, confidence scores, and class labels for all detected objects.

A sample JSON request used to send an image could be as follows:

```json
{
  "uuid": "e4b2c1d0-8d2e-11eb-8dcd-0242ac130003",
  "image": "<base64 string>"
}
```

Required response payload format:

```json
{
  "uuid": "e4b2c1d0-8d2e-11eb-8dcd-0242ac130003",
  "count": 2,
  "detections": ["object1", "object2"],
  "boxes": [
    {"x": 1, "y": 2, "width": 3, "height": 4, "probability": 0.9},
    {"x": 5, "y": 6, "width": 7, "height": 8, "probability": 0.8}
  ],
  "speedpreprocessms": "a",
  "speedinferencems": "b",
  "speedpostprocessms": "c"
}
```

Notes:
1. The uuid is the same ID sent by the client along with the image. This is used to associate an asynchronous response with the request at the client side.
2. The count `n` represents the number of objects detected in the image.
3. The boxes represent the list of `n` rectangles around the detected objects, with information on x, y coordinates, width, height, and the probability that the rectangular area contains the detected objects. When the count is 0, this should be an empty array.
4. The latency metrics `speedpreprocessms`, etc. are automatically generated by the Ultralytics YOLO inference engine upon prediction and must be dynamically extracted and returned in the payload.

### 4.2 Annotated Image API (`/apiannotate`)

A secondary endpoint must accept the exact same request payload schema but return a JSON object containing the original image overlaid with bounding boxes and labels. The Ultralytics library provides plotting utilities that automatically render these annotations. The resulting annotated image must be encoded back into base64 format and returned to the client.

## 5. Containerization and Infrastructure as Code

### 5.1 Dockerfile Engineering

Docker builds images by reading instructions from a Dockerfile. You must create an optimised Dockerfile to package your web service. Optimisation is critical for cloud deployments. Avoid installing unnecessary packages, e.g. text editors or GUI libraries, to minimise the final image size and reduce registry pull times. You must use an appropriate Python base image and ensure that heavy machine learning libraries like PyTorch are installed using CPU-only index flags to reduce container bloat by several gigabytes.

### 5.2 Infrastructure as Code (IaC)

To reflect modern DevOps practices, part of the total assignment mark is awarded for utilising Terraform, Ansible, or Chef to automate infrastructure provisioning. You must submit scripts that automatically create the required cloud resources and allocation policies. Manual creation of these resources via the graphical OCI web console is permitted to complete the assignment, but doing so will forfeit the marks allocated for IaC.

## 6. Kubernetes Cluster Configuration

You will deploy your containerised application on a public cloud platform (GCP, Oracle, or Azure) using three virtual machines (4 cores and 8 GB RAM each). You need to set up a K8s cluster on those VMs as 1 master node and 2 worker nodes. You must provision a basic K8s cluster and host your application on it. You must create standard Kubernetes manifest files (YAML) to orchestrate your application.

Deployments: Create a Kubernetes Deployment that pulls your Docker image from an accessible registry.

Resource Limits: You must restrict each pod to a maximum of 1 vCPU CPU limit (1.0) and a specified amount of memory (see the rubric for more details). This hardware restriction is mathematically vital for the validity of the performance benchmarking phase.

Service Exposure: Expose your deployment using a Kubernetes Service of NodePort, LoadBalancer or an ingress controller. A standalone load balancer on the master node is also allowed. You need to route external Internet traffic into your cluster pods.

## 7. Load Generation and Performance Metrics

Using Locust, you will write a Python load-generation script to simulate concurrent user access to your API. The script must continuously encode a local environmental test image to base64, embed it in the required JSON schema, and execute an HTTP POST to your `/apipredict` and `/apiannotate` endpoints.

Hint: Because machine learning inference is highly CPU-bound, achieving high concurrency in Python requires careful architectural management. If you simply execute the synchronous YOLO prediction inside a standard asynchronous FastAPI route, you will block the main event loop, causing catastrophic latency spikes for all concurrent requests.

## 8. Experiments and Benchmark Report

You must test the scalability of your system under different resource conditions. You must execute your Locust scripts against your K8s cluster while scaling the Deployment replicas to vary the number of active pods: 1, 2, 4, and 8 pods. For each specific pod configuration, you will gradually increase the number of concurrent Locust users until the system reaches its breaking point, defined as the threshold at which response times degrade exponentially or HTTP 500/503 errors begin to occur. Record the maximum stable concurrent users and the average response time at that threshold.

Reporting Requirement: You must submit a concise, data-driven benchmark report (maximum 500 words) containing the following:

1. Results table documenting the maximum users and average response time for the 1, 2, 4, and 8 pod configurations.
2. Graphical plots: Two distinct plots mapping the correlation between concurrent users and average latency across the different scaling configurations.
3. Performance analysis: A technical discussion explaining the scaling efficiency. According to queuing theory and Little’s Law, explain the latency spikes observed during saturation. Identify the primary bottlenecks in your FastAPI-YOLO architecture and justify how horizontal pod autoscaling mitigates them.

## 9. Interview/Demo

Now that you have completed the project, you will go through a mandatory 20-minute live technical interview with the teaching team. This is a strict hurdle requirement for this assignment. If you do not attend the interview or cannot show sufficient understanding of your own project, the maximum mark you will receive is 45 out of 100.

During the interview session, you will be required to:
1. Share your screen and demonstrate the live cluster using `kubectl` commands.
2. Execute the Locust script in real time to demonstrate application functionality and load balancing.
3. Explain some of the source code in your application when asked by the interviewer.
4. Explain your optimisation strategies and walk through your IaC scripts, if any.

Failure to adequately explain your own code or to demonstrate a lack of understanding of your cloud infrastructure will result in an automatic Fail NH for the entire assignment, capping your mark at 45, regardless of the system’s operational status.

## 10. Submission

You need to submit 3 files via Moodle:

1. A report in PDF format as requested: filename `firstname lastname studentid.pdf`.
2. A PDF file containing the Generative AI prompts you have used and their output.
3. A `.ZIP` file (not `.RAR` or other formats) containing the following:
   - Your Dockerfile.
   - Your web service source code.
   - Your Kubernetes deployment and service configurations YAML files.
   - Your Locust client script.
   - Any script that automates running experiments, if you have one.
   - Your IaC scripts.
   - A `readme.md` file with brief instructions regarding how to run your application.
   - The URL of your deployed application, accessible over the Internet.

This zip file is essentially the deliverable artefact when you finish a software project: deliver a buildable, deployable package to your client.

## 11. Generative AI Statement

As per the University’s policy on the guidelines and practices pertaining to the usage of Generative AI, AI tools may be used openly within this assessment. Where used, AI must be used responsibly, clearly documented and appropriately acknowledged; see Learn HQ. Any work submitted for a mark must:

1. Represent a sincere demonstration of your human efforts, skills and subject knowledge that you will be accountable for.
2. Adhere to the guidelines for AI use set for the assessment task.
3. Reflect the University’s commitment to academic integrity and ethical behaviour.
4. Be aware that inappropriate AI use and/or AI use without acknowledgment will be considered a breach of academic integrity.

The teaching team encourages students to apply their own critical thinking and reasoning skills when working on the assessments with an assistant from GenAI. Generative AI tools may produce inaccurate content, which could negatively impact student comprehension of big data topics. All the prompts that you have used and their output must be attached in your submission as a reference.

# FIT5225 Week 3 Cheat Sheet

Based on the attached Week 3 lecture slides: *3-containers.pdf* [file:5]

## What this week is about
Week 3 focuses on containers, how they compare with virtual machines, Docker as a container platform, Docker Engine components, images and layers, Dockerfiles, and basic orchestration ideas such as Docker Compose, Docker Swarm, and Kubernetes. [file:5]

## Learning outcomes to remember
- Describe fundamental principles and paradigms of cloud computing. [file:5]
- Demonstrate a comprehensive understanding of virtualization and container technologies. [file:5]

## Lecture outline to memorize
The lecture covers: [file:5]
- VMs and containers. [file:5]
- Docker as a container enabler. [file:5]
- Docker Engine components. [file:5]
- Docker images, registries, layers, and Dockerfile. [file:5]
- Container orchestration. [file:5]
- Docker Swarm. [file:5]
- Kubernetes. [file:5]

## Why containers appeared
The lecture first reminds you of the advantages of virtualization, such as lower hardware costs, easier VM movement across data centers, disaster recovery, maintenance support, workload consolidation, better device utilization, energy savings, easier automation, and flexibility for multiple operating systems. [file:5]

But virtualization also has problems: every VM needs its own OS, each OS consumes CPU, RAM, and storage, OS licenses increase CapEx, maintenance raises OpEx, VMs are slower to boot, and portability between hypervisors and cloud platforms can be difficult. [file:5]

### Exam-ready takeaway
Containers emerged as a lighter alternative to VMs because VMs carry full-OS overhead, slower boot time, and extra cost and maintenance. [file:5]

## What containers are
Containers are not new; the slides mention Google’s container technology as well as earlier systems such as Solaris Zones, BSD jails, and LXC. [file:5]

Containers on a single host share one operating system, start quickly, are ultra-portable, and are isolated. [file:5]

### Fast exam phrasing
A container is a lightweight isolated execution environment that packages an application and its dependencies while sharing the host OS. [file:5]

## Container benefits
Memorize these benefits:
- Multiple copies can run on the same or different machines, which supports scalability. [file:5]
- The same image can run on a personal machine, in a data center, or in a cloud. [file:5]
- OS resources can be restricted or unrestricted as designed at build time. [file:5]
- Containers provide isolation. [file:5]
- Containers can be stopped, saved, and moved for later execution. [file:5]

### Nice example from the slides
The lecture notes that the `ps` command inside a container shows only the processes in that container, illustrating isolation. [file:5]

## VMs and containers: similarities
Both VMs and containers isolate an application and its dependencies into a self-contained unit that can run anywhere. [file:5]

Both also reduce the need for direct physical hardware use and help improve efficiency in energy use and cost. [file:5]

## VMs vs containers
This comparison is very likely to be tested. [file:5]

| Topic | VMs | Containers |
|---|---|---|
| Weight | Heavyweight. [file:5] | Lightweight. [file:5] |
| Performance | Limited performance, with CPU overhead greater than 10% and disk I/O overhead greater than 50%. [file:5] | Near-native performance, with CPU overhead below 5% and negligible disk I/O overhead. [file:5] |
| OS model | Each VM runs its own OS. [file:5] | All containers share the host OS. [file:5] |
| Virtualization level | Hardware-level virtualization. [file:5] | OS virtualization. [file:5] |
| Boot time | Minutes. [file:5] | Seconds or milliseconds. [file:5] |
| Memory usage | Allocates required memory with higher overhead. [file:5] | Requires less memory space. [file:5] |
| Security/isolation | Fully isolated and therefore more secure. [file:5] | Process-level isolation and possibly less secure. [file:5] |
| Legacy-app impact | Low to medium impact on legacy apps. [file:5] | High impact on legacy apps. [file:5] |

### Short-answer line
VMs virtualize hardware and include a guest OS per instance, while containers virtualize at the OS level and share the host OS, making them lighter and faster. [file:5]

## Containers inside VMs
The lecture also shows a mixed scenario where containers can run inside VMs. [file:5]

That means VMs and containers are not mutually exclusive; they are often used together in layered cloud deployments. [file:5]

## Docker: what the term can mean
The slides say “Docker” may refer to three different things: [file:5]
- **Docker, Inc.**: the company. [file:5]
- **Docker Engine**: the container runtime and orchestration technology. [file:5]
- **Docker project**: the open-source project, now called **Moby**. [file:5]

### Important distinction
In most technical discussion, “Docker” usually means **Docker Engine** unless the context clearly refers to the company or open-source project. [file:5]

## Moby / Docker open-source project
The Moby project is the upstream open-source project for Docker and aims to break Docker into more modular components in the open. [file:5]

The core Docker Engine project is located at GitHub under `moby/moby`, it uses the Apache License 2.0, and much of it is written in Go. [file:5]

## Docker, Inc.
Docker, Inc. is described as a San Francisco startup founded by Solomon Hykes. [file:5]

It began as a PaaS provider called dotCloud, which used Linux containers behind the scenes, and later shifted mission to bring Docker and containers to the world. [file:5]

## DevOps view of Docker
From the developer perspective, Docker is about pulling app code, inspecting a Dockerfile, containerizing the app, and running it as a container. [file:5]

From the operations perspective, Docker is about downloading an image, starting a container, logging into it, running commands inside it, and then destroying it. [file:5]

## Docker Engine
Docker Engine is the core container runtime that runs and orchestrates containers. [file:5]

Other Docker and third-party tools plug into Docker Engine and build around it, and the engine can be downloaded from Docker or built from source. [file:5]

The lecture mentions two editions: **Enterprise Edition (EE)** for deployment with paid support and **Community Edition (CE)** as the free option for experimentation. [file:5]

## Docker Engine components
This is highly testable. [file:5]

Main components shown in the lecture:
- Docker daemon. [file:5]
- Docker client. [file:5]
- Remote REST API. [file:5]
- containerd. [file:5]
- runc. [file:5]
- Images. [file:5]
- Containers. [file:5]
- Registry / Docker Hub. [file:5]

### Roles of main components
- **Docker daemon** manages containers, images, builds, and more. [file:5]
- **Docker client** communicates with the daemon to execute commands. [file:5]
- **REST API** enables remote interaction with the daemon. [file:5]
- **containerd** manages container lifecycle operations such as start, stop, pause, and remove. [file:5]
- **runc** is a lightweight CLI wrapper for libcontainer. [file:5]

## Images
You start a container from an image, and containers are built from images and can also be saved back as images. [file:5]

The lecture says the image and container become dependent, so you cannot delete an image until the last container using it has been stopped and destroyed. [file:5]

Examples in the slides:
- Alpine Linux image is about 4 MB. [file:5]
- Ubuntu image is about 110 MB. [file:5]
- A Microsoft .NET image is over 1.7 GB uncompressed. [file:5]

The process of getting images onto a Docker host is called **pulling**. [file:5]

### Exam-ready definition
A Docker image is a read-only template used to create containers. [file:5]

## Image registries
Docker images are stored in **image registries**. [file:5]

Types mentioned in the lecture:
- Local registry on the same host. [file:5]
- Docker Hub, a globally shared registry. [file:5]
- A private registry on Docker.com. [file:5]

If an image is not found locally, Docker downloads it from the specified location. [file:5]

The lecture also distinguishes **official** images, which are vetted by Docker, from **unofficial** images, which should be used with care. [file:5]

Each image can have several **tags** such as `latest` or `v2`, and each image is identified by a **256-bit hash**. [file:5]

## Layers
A Docker image is made of loosely connected read-only layers. [file:5]

Images are built layer by layer, layers can be inspected with Docker commands, each layer has its own 256-bit hash, and layers can be shared across many containers. [file:5]

The lecture’s example sequence is: install Ubuntu, install Python, then apply a Python security patch, with each step becoming a separate layer. [file:5]

A file in a higher layer obscures the file directly below it, allowing updated versions of files to be added without replacing the whole image. [file:5]

### Why layers matter
Shared layers improve space efficiency and performance, and any change to the content changes the associated hashes. [file:5]

## Starting a new container
When a command is entered into the Docker CLI, the Docker client converts it into the correct API payload and sends it to the daemon. [file:5]

The daemon then calls `containerd`, and `containerd` uses `runc` to create the container. [file:5]

The lecture says `runc` works with OS-kernel constructs such as **namespaces** and **cgroups** to create the container. [file:5]

### Core flow to memorize
CLI command -> Docker client -> Docker daemon/API -> containerd -> runc -> kernel features such as namespaces and cgroups -> running container. [file:5]

## What shim does
The shim supports daemonless containers. [file:5]

The lecture explains that `containerd` forks a new `runc` process for each container, but once the container is created, the parent `runc` exits; the shim then keeps the container running and keeps stdin/stdout open, becoming the container’s parent process. [file:5]

## Common Docker commands
Commands shown in the lecture include: [file:5]
- `docker container run` [file:5]
- `docker container ls` [file:5]
- `docker container exec` [file:5]
- `docker container stop` [file:5]
- `docker container start` [file:5]
- `docker container rm` [file:5]
- `docker container inspect` [file:5]

The lecture also notes that containers can be stopped, started, paused, and restarted many times. [file:5]

If data is stored in a **volume**, that data persists even after the container is removed. [file:5]

## Web server example details
The lecture gives a background web-server example using `docker container run -d --name webserver -p 80:8080 ...`. [file:5]

Here, `-d` means daemon mode or background execution, and the port mapping format is `host-port:container-port`. [file:5]

## Dockerfile
A Dockerfile is a plain-text document that describes how to build an application into a Docker image. [file:5]

It contains the commands a user could otherwise issue manually to assemble the image. [file:5]

### Why Dockerfile is preferred
The lecture gives these reasons:
- It acts as an audit log of how the image is built. [file:5]
- It supports automation of builds and updates. [file:5]
- It works well in continuous delivery pipelines. [file:5]
- It is a cleaner way to create layers. [file:5]

## Building an image
The example command `docker image build -t web:latest .` builds an image tagged `web:latest`. [file:5]

The period `.` at the end means Docker uses the current working directory as the **build context**. [file:5]

## Docker Compose
Modern applications are often made of multiple smaller services, called **microservices**. [file:5]

Docker Compose lets you define a multi-container application in a single declarative YAML file and deploy it with one command through the Docker Engine API. [file:5]

### Exam-ready phrasing
Docker Compose simplifies deployment of multi-service applications by describing them declaratively in YAML instead of using long manual Docker commands. [file:5]

## Container orchestration
The outline explicitly lists **container orchestration**, **Docker Swarm**, and **Kubernetes** as Week 3 topics. [file:5]

Even though the slides you attached provide little detail on Swarm and Kubernetes in the extracted text, you should at least remember that these are orchestration technologies for managing containers at scale. [file:5]

## Fast memory table
| Topic | What to remember |
|---|---|
| Why containers | VMs have full-OS overhead, slower boot, higher cost, and portability issues. [file:5] |
| Container idea | Lightweight isolated app packaging that shares the host OS. [file:5] |
| VM vs container | VM = hardware virtualization with guest OS; container = OS virtualization sharing host OS. [file:5] |
| Docker meanings | Company, Engine, and open-source project/Moby. [file:5] |
| Core Docker parts | Client, daemon, REST API, containerd, runc, images, containers, registry. [file:5] |
| Image | Read-only template for creating containers. [file:5] |
| Registry | Storage and distribution for Docker images. [file:5] |
| Layer | Read-only image component with its own hash. [file:5] |
| Dockerfile | Plain-text instructions for building an image. [file:5] |
| Compose | YAML-based deployment for multi-container apps. [file:5] |

## What is most likely to appear in short answers
### 1) Why use containers instead of VMs?
Possible points:
- Containers are lighter. [file:5]
- Containers start much faster. [file:5]
- Containers share the host OS, so they avoid per-VM OS overhead. [file:5]
- Containers often give near-native performance. [file:5]
- Containers are portable across personal machines, data centers, and clouds. [file:5]

### 2) Explain Docker Engine architecture
- The client sends commands to the daemon, often through the API. [file:5]
- The daemon manages images, builds, and containers. [file:5]
- containerd manages lifecycle. [file:5]
- runc creates containers using kernel features such as namespaces and cgroups. [file:5]

### 3) Explain images, registries, and layers
- Images are read-only templates. [file:5]
- Registries store and distribute images. [file:5]
- Layers are stacked read-only components with hashes and sharing support. [file:5]

### 4) Why use Dockerfile or Compose?
- Dockerfile improves reproducibility, maintainability, and automation. [file:5]
- Compose simplifies multi-service deployment. [file:5]

## Sample multiple-choice questions
### Set 1
1. Which problem of virtualization is explicitly listed in the lecture?  
A. No isolation at all  
B. Every VM requires its own dedicated OS  
C. Containers cannot be moved  
D. Hypervisors cannot use RAM  
**Answer: B** [file:5]

2. Which is a reason containers are attractive?  
A. They require a full guest OS per app  
B. They are fast to start  
C. They always boot in minutes  
D. They eliminate all security issues  
**Answer: B** [file:5]

3. Which older container-related technologies are mentioned?  
A. Solaris Zones, BSD jails, and LXC  
B. Only VMware and ESXi  
C. Only Docker Hub  
D. BIOS and UEFI  
**Answer: A** [file:5]

4. Containers on a single host share:  
A. Separate guest OSs  
B. A single operating system  
C. A separate hypervisor each  
D. No networking  
**Answer: B** [file:5]

5. Which command example illustrates isolation by showing only processes in the container?  
A. ls  
B. ping  
C. ps  
D. mkdir  
**Answer: C** [file:5]

6. A key benefit of containers is that the same image can run:  
A. Only on one developer laptop  
B. Only in public cloud  
C. On a personal machine, in a data center, or in a cloud  
D. Only inside BIOS  
**Answer: C** [file:5]

7. Both VMs and containers:  
A. Always use the same isolation technique  
B. Isolate applications and dependencies into self-contained units  
C. Require physical hardware per app  
D. Are identical in security and overhead  
**Answer: B** [file:5]

8. Which statement about containers vs VMs is correct?  
A. Containers are heavyweight and VMs are lightweight  
B. VMs share the host OS while containers each run their own OS  
C. VMs virtualize hardware while containers virtualize at the OS level  
D. Containers always take minutes to boot  
**Answer: C** [file:5]

9. According to the slide table, containers usually have:  
A. Boot time in minutes  
B. Seconds or milliseconds boot time  
C. No boot process  
D. Larger memory footprint than VMs  
**Answer: B** [file:5]

10. According to the table, containers are:  
A. Fully isolated and more secure than VMs in all cases  
B. Process-level isolation and possibly less secure  
C. Hardware-level virtualization with guest OSs  
D. Always better for legacy apps  
**Answer: B** [file:5]

11. “Docker” may refer to:  
A. Only the company  
B. Only the engine  
C. The company, the engine, or the open-source project  
D. Only a Linux command  
**Answer: C** [file:5]

12. The open-source Docker project is now called:  
A. Swarm  
B. Moby  
C. Compose  
D. Alpine  
**Answer: B** [file:5]

13. Much of the Moby project is written in:  
A. Java  
B. Rust  
C. Go  
D. C#  
**Answer: C** [file:5]

14. Docker, Inc. originally began as:  
A. A hardware vendor  
B. A PaaS provider called dotCloud  
C. A hypervisor company called XenCloud  
D. A storage-only company  
**Answer: B** [file:5]

15. Docker Engine is best described as:  
A. A database only  
B. The core container runtime that runs and orchestrates containers  
C. A web browser plugin  
D. A Linux kernel replacement  
**Answer: B** [file:5]

16. Which is a Docker Engine edition mentioned in the lecture?  
A. Academic Edition  
B. Community Edition  
C. Student Edition  
D. Kernel Edition  
**Answer: B** [file:5]

17. Which component manages containers, images, and builds?  
A. Docker daemon  
B. Docker Hub only  
C. Volume driver only  
D. Hypervisor  
**Answer: A** [file:5]

18. Which component communicates with the daemon to execute commands?  
A. Docker client  
B. Dockerfile  
C. Image registry  
D. Kernel module only  
**Answer: A** [file:5]

19. Remote interaction with the Docker daemon can happen through:  
A. REST API  
B. BIOS API  
C. JVM API  
D. TLB API  
**Answer: A** [file:5]

20. Which component manages container lifecycle operations such as start and stop?  
A. Compose  
B. containerd  
C. Volume  
D. Dockerfile  
**Answer: B** [file:5]

### Set 2
21. runc is described as:  
A. A large hypervisor  
B. A lightweight CLI wrapper for libcontainer  
C. An image registry  
D. A YAML parser only  
**Answer: B** [file:5]

22. You start a container from an:  
A. API key  
B. Image  
C. Hypervisor driver  
D. Port map  
**Answer: B** [file:5]

23. A Docker image is:  
A. A read-only template  
B. A running process only  
C. Always writable  
D. The same thing as a volume  
**Answer: A** [file:5]

24. Pulling refers to:  
A. Deleting an image  
B. Getting an image onto a Docker host  
C. Pausing a container  
D. Mapping a port  
**Answer: B** [file:5]

25. Which image size example is given?  
A. Alpine about 4 MB  
B. Ubuntu about 4 KB  
C. .NET image about 17 MB  
D. Alpine about 400 MB  
**Answer: A** [file:5]

26. Docker images are stored in:  
A. Registries  
B. Only RAM  
C. Only BIOS memory  
D. Only YAML files  
**Answer: A** [file:5]

27. Docker Hub is described as:  
A. A local-only registry  
B. A globally shared registry  
C. A Linux distribution  
D. A hypervisor type  
**Answer: B** [file:5]

28. Official images are:  
A. Always larger than unofficial ones  
B. Vetted by Docker  
C. Never tagged  
D. Stored only locally  
**Answer: B** [file:5]

29. Image tags include examples such as:  
A. latest and v2  
B. only root and sudo  
C. BIOS and UEFI  
D. ps and ls  
**Answer: A** [file:5]

30. Each image is identified by a:  
A. 32-bit integer  
B. 256-bit hash  
C. MAC address only  
D. YAML block  
**Answer: B** [file:5]

31. A Docker image is built from:  
A. One single writable layer only  
B. Loosely connected read-only layers  
C. Only one binary file  
D. Only containers  
**Answer: B** [file:5]

32. Multiple images sharing layers leads to:  
A. Worse space efficiency  
B. Efficiencies in space and performance  
C. No performance effect  
D. Mandatory reinstallation  
**Answer: B** [file:5]

33. A file in a higher layer:  
A. Deletes the entire image  
B. Obscures the file directly below it  
C. Must be in a separate registry  
D. Cannot affect lower layers  
**Answer: B** [file:5]

34. After the Docker daemon receives a create-container request, it calls:  
A. Dockerfile  
B. containerd  
C. Kubernetes  
D. YAML parser only  
**Answer: B** [file:5]

35. containerd uses ___ to create the container.  
A. ps  
B. runc  
C. YAML  
D. Docker Hub  
**Answer: B** [file:5]

36. The kernel constructs named in the lecture for creating containers are:  
A. NAT and DNS  
B. namespaces and cgroups  
C. BIOS and UEFI  
D. RAID and LVM  
**Answer: B** [file:5]

37. The shim mainly helps by:  
A. Compiling Dockerfiles  
B. Keeping the container running and stdio open after runc exits  
C. Replacing the daemon  
D. Storing images in Docker Hub  
**Answer: B** [file:5]

38. Which command lists containers?  
A. docker image pull  
B. docker container ls  
C. docker daemon show  
D. docker registry list  
**Answer: B** [file:5]

39. Data that should persist beyond a container’s removal should be stored in a:  
A. Tag  
B. Volume  
C. Registry hash  
D. Namespace  
**Answer: B** [file:5]

40. In `-p 80:8080`, the syntax means:  
A. container-port:host-port  
B. host-port:container-port  
C. internal-IP:external-IP  
D. registry-port:image-port  
**Answer: B** [file:5]

41. In the lecture, `-d` means:  
A. debug mode  
B. daemon mode or background run  
C. delete mode  
D. directory mode  
**Answer: B** [file:5]

42. A Dockerfile is:  
A. A binary log file  
B. A plain-text file describing how to build an image  
C. A running process  
D. A hypervisor configuration file  
**Answer: B** [file:5]

43. One benefit of using a Dockerfile is:  
A. It removes all need for images  
B. It provides an audit log of how the image is built  
C. It makes layers impossible  
D. It only works for single-service apps  
**Answer: B** [file:5]

44. The period `.` in `docker image build -t web:latest .` indicates:  
A. Hidden mode  
B. The current directory as build context  
C. Root filesystem only  
D. The latest image layer  
**Answer: B** [file:5]

45. Modern apps made of multiple smaller services are called:  
A. Monoliths only  
B. Microservices  
C. Hypervisors  
D. Registries  
**Answer: B** [file:5]

46. Docker Compose uses a:  
A. Binary executable image format only  
B. Declarative YAML file for multi-container apps  
C. Hypervisor config file  
D. Java source file  
**Answer: B** [file:5]

47. Docker Compose deploys apps via the:  
A. BIOS menu  
B. Docker Engine API  
C. TLB  
D. runc shell only  
**Answer: B** [file:5]

48. Which topics are explicitly listed under orchestration in the outline?  
A. Docker Swarm and Kubernetes  
B. VMware and Xen  
C. BIOS and UEFI  
D. RSA and AES  
**Answer: A** [file:5]

## Sample short-answer questions with model points
### SAQ 1
**Question:** Why were containers introduced when virtualization already existed?  
**Model points:** VMs require a full OS for each instance, which increases CPU, RAM, storage, licensing, maintenance cost, and boot time. Containers reduce this overhead by sharing the host OS while keeping applications isolated. [file:5]

### SAQ 2
**Question:** Define a container.  
**Model points:** A container is a lightweight isolated environment that packages an application and its dependencies, shares the host OS, starts quickly, and can run consistently across machines. [file:5]

### SAQ 3
**Question:** Compare containers and VMs.  
**Model points:** VMs are heavyweight, use hardware virtualization, include a guest OS per instance, and boot more slowly. Containers are lightweight, use OS-level virtualization, share the host OS, use less memory, and start in seconds or milliseconds. [file:5]

### SAQ 4
**Question:** What can the term Docker refer to?  
**Model points:** It may refer to Docker, Inc.; Docker Engine, the runtime/orchestration technology; or the open-source project, now called Moby. [file:5]

### SAQ 5
**Question:** What is Docker Engine?  
**Model points:** Docker Engine is the core container runtime that runs and orchestrates containers, and other Docker and third-party tools plug into it. [file:5]

### SAQ 6
**Question:** Explain the main Docker Engine components.  
**Model points:** The Docker client sends commands, the daemon manages containers and images, the REST API enables remote interaction, containerd manages lifecycle, and runc creates containers using kernel mechanisms. [file:5]

### SAQ 7
**Question:** What is a Docker image?  
**Model points:** A Docker image is a read-only template used to create containers. Containers are built from images, and images can also be saved from containers. [file:5]

### SAQ 8
**Question:** What is an image registry?  
**Model points:** A registry stores and distributes Docker images. Examples include a local registry, Docker Hub, and private registries. [file:5]

### SAQ 9
**Question:** Explain Docker image layers.  
**Model points:** Docker images are made of stacked read-only layers, each with its own hash. Layers can be shared among images and containers, which improves efficiency, and higher layers can obscure files in lower layers. [file:5]

### SAQ 10
**Question:** Describe the process of starting a new container.  
**Model points:** The Docker client converts the command into an API request, the daemon receives it, calls containerd, containerd invokes runc, and runc works with kernel features such as namespaces and cgroups to create the container. [file:5]

### SAQ 11
**Question:** What is the role of shim?  
**Model points:** The shim keeps the container running and keeps stdin/stdout open after runc exits, becoming the parent process of the container. [file:5]

### SAQ 12
**Question:** Why use a Dockerfile instead of building manually?  
**Model points:** A Dockerfile provides a build audit log, supports automation, works well in continuous delivery, and gives a cleaner way to create image layers. [file:5]

### SAQ 13
**Question:** What is the build context in `docker image build -t web:latest .`?  
**Model points:** The dot means the current working directory is used as the build context for the image build. [file:5]

### SAQ 14
**Question:** What problem does Docker Compose solve?  
**Model points:** Compose simplifies deployment of multi-container or microservice applications by letting users define the entire application in one declarative YAML file and deploy it with a single command. [file:5]

### SAQ 15
**Question:** Why are containers useful in cloud environments?  
**Model points:** They are scalable, portable across environments, fast to start, lightweight, and easy to package and move, making them suitable for cloud deployment and microservices. [file:5]

## Likely exam traps
- Do not say containers are completely new; the lecture explicitly mentions older container technologies. [file:5]
- Do not confuse **Docker Engine** with **Docker, Inc.** or **Moby**. [file:5]
- Do not confuse an **image** with a **container**; the image is the template, while the container is the running instance. [file:5]
- Do not forget that **layers are read-only**. [file:5]
- Do not reverse port mapping; the lecture uses **host-port:container-port**. [file:5]
- Do not forget that **Compose** is for multi-container apps defined in YAML. [file:5]

## 15-minute revision plan
1. Memorize why containers are needed compared with VMs. [file:5]
2. Memorize the VM vs container comparison table. [file:5]
3. Memorize the meanings of Docker, plus Docker Engine components. [file:5]
4. Understand images, registries, tags, hashes, and layers. [file:5]
5. Memorize Dockerfile, build context, and Compose. [file:5]

## Ultra-short cram sheet
- Containers share the host OS and are lightweight. [file:5]
- VMs include a guest OS and are heavier. [file:5]
- Docker can mean the company, the engine, or the project/Moby. [file:5]
- Docker Engine core parts = client, daemon, API, containerd, runc. [file:5]
- Image = read-only template; container = running instance. [file:5]
- Registry stores images; Docker Hub is global. [file:5]
- Images are built from layers with hashes. [file:5]
- runc uses namespaces and cgroups. [file:5]
- Dockerfile describes how to build an image. [file:5]
- Compose deploys multi-container apps from YAML. [file:5]

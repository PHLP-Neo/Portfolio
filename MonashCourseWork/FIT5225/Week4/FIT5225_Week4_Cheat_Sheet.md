# FIT5225 Week 4 Cheat Sheet

Based on the attached Week 4 lecture slides: *4-Orchestration.pdf* [file:7]

## What this week is about
Week 4 focuses on container orchestration, especially Docker Swarm and Kubernetes, and on the core Kubernetes objects you are most likely to be tested on: Pods, Deployments, and Services. [file:7]

## Learning outcomes to remember
- Describe fundamental principles and paradigms of cloud computing. [file:7]
- Demonstrate a comprehensive understanding of virtualization and container technologies. [file:7]

## What an orchestrator does
An orchestrator manages and organizes both hosts and Docker containers running in a cluster. [file:7]

The main issue it solves is **resource allocation**: deciding where a container can be scheduled based on CPU, RAM, and disk requirements, while also tracking nodes and scaling. [file:7]

### Fast exam phrasing
A container orchestrator automates large-scale deployment, scheduling, scaling, networking, and recovery of containers across clusters. [file:7]

## Container orchestration tools
Container orchestration tools provide a framework for integrating and managing containers at scale. [file:7]

They simplify container management processes and help manage availability and scaling. [file:7]

Examples in the lecture:
- **Kubernetes**: open-source and a CNCF product. [file:7]
- **Apache Mesos**: a cluster management tool that can also support orchestration, originally through Marathon. [file:7]
- **Docker Swarm**: integrated into the Docker container platform. [file:7]

Core orchestration features listed:
- Networking. [file:7]
- Scaling. [file:7]
- Service discovery. [file:7]
- Load balancing. [file:7]
- Health checks and self-healing. [file:7]
- Security. [file:7]
- Rolling updates. [file:7]

## Scalability comparison
The lecture compares orchestration tools by scale: [file:7]
- **Kubernetes** is good for scheduling groups of complex applications and scaling to enterprise-level requirements. [file:7]
- **Swarm** is better suited to small or medium clusters. [file:7]
- **Mesos** supports orchestration at the largest scale. [file:7]

## Docker Swarm overview
At a high level, Docker Swarm has two major components: [file:7]
- A **secure cluster**. [file:7]
- An **orchestration engine**. [file:7]

A swarm consists of one or more Docker nodes, which may be physical servers, virtual machines, Raspberry Pis, or cloud instances. [file:7]

All swarm nodes communicate over reliable networks, and nodes are configured as either **managers** or **workers**. [file:7]

Swarm uses **TLS** to encrypt communication, authenticate nodes, and authorize roles. [file:7]

## Swarm modes and leadership
Docker hosts can run in: [file:7]
- **Single Engine Mode**: not participating in a swarm. [file:7]
- **Swarm Mode**: participating in a swarm. [file:7]

Managers select a leader that keeps track of the swarm, while other managers monitor passively and can re-elect a leader if the leader fails. [file:7]

## Swarm service
In Docker Swarm, the atomic unit of scheduling is the **service**. [file:7]

A service is a higher-level construct that wraps advanced features around containers. [file:7]

When a container is wrapped in a service, it is called a **task** or **replica**, and the service adds capabilities such as scaling, rolling updates, and simple rollbacks. [file:7]

### Good short-answer line
Swarm schedules **services**, not raw standalone containers, because services add orchestration features like replicas and updates. [file:7]

## Swarm high availability and Raft
Swarm managers have native support for **high availability (HA)**, meaning one or more managers can fail and the swarm can keep running. [file:7]

This HA is powered by the **Raft consensus algorithm**. [file:7]

## Raft consensus algorithm
A consensus algorithm allows a collection of machines to work as a coherent group that can survive some failures while still agreeing on a single source of truth. [file:7]

The lecture presents Raft as a consensus algorithm that distributes a state machine across a cluster so each node agrees on the same series of state transitions. [file:7]

### Core Raft idea to memorize
Raft ensures cluster agreement even when some nodes fail. [file:7]

## Raft server states
Raft nodes move between three states: [file:7]
- **Follower**. [file:7]
- **Candidate**. [file:7]
- **Leader**. [file:7]

The lecture also notes the normal arrangement as **1 leader and N-1 followers**. [file:7]

## Terms in Raft
Time in Raft is divided into **terms**, and each term begins with an election. [file:7]

After a successful election, one leader manages the cluster until the term ends, though some elections may fail and end without producing a leader. [file:7]

## Leader elections in Raft
Key steps from the lecture:
1. Servers start as followers. [file:7]
2. They stay followers while receiving heartbeats. [file:7]
3. If a follower does not receive communication for an election timeout, it starts an election. [file:7]
4. The follower with the shortest timeout begins election activity. [file:7]
5. It increments the term. [file:7]
6. It becomes a candidate. [file:7]
7. It votes for itself. [file:7]
8. It sends `RequestVote` RPCs to other servers. [file:7]
9. If it gets a majority, it becomes leader and sends `AppendEntry` heartbeats. [file:7]
10. If it hears from a valid leader, it goes back to follower. [file:7]
11. If nobody wins, a new term and election begin. [file:7]

### Numbers worth remembering
Election timeouts are typically **100–500 ms**. [file:7]

## Swarm commands to know
Commands explicitly listed in the lecture:
- `docker swarm init` creates a new swarm and makes the current node the first manager. [file:7]
- `docker swarm join-token worker` or `docker swarm join-token manager` reveals join commands and tokens. [file:7]
- `docker node ls` lists nodes, managers, and the leader. [file:7]
- `docker service create` creates a service. [file:7]
- `docker service ls` lists services and replicas. [file:7]
- `docker service ps <service>` shows detailed information about service replicas. [file:7]
- `docker service inspect` shows very detailed service information. [file:7]
- `docker service scale` changes the number of replicas. [file:7]
- `docker service update` updates a running service. [file:7]
- `docker service logs` shows service logs. [file:7]
- `docker service rm` removes a service and all its replicas. [file:7]

## Docker Swarm networking
Containers in Docker need strong networking because they often need to communicate across many kinds of networks. [file:7]

The lecture notes that swarm nodes may not be on the same LAN, so **VXLAN** is used to provide virtual overlay networking. [file:7]

## Persistent data with volumes
The recommended way to persist data in containers is with **volumes**. [file:7]

The high-level pattern is: create a volume, create a container, mount the volume into the container, and then anything written to the mounted directory is stored in the volume. [file:7]

### Volume commands from the lecture
- `docker volume create` creates a volume. [file:7]
- `docker volume ls` lists volumes. [file:7]
- `docker volume inspect` shows details, including where the volume exists on the host. [file:7]
- `docker volume prune` deletes all unused volumes. [file:7]
- `docker volume rm` removes specific unused volumes. [file:7]

## Kubernetes overview
The lecture says Kubernetes is a Greek word meaning governor, helmsman, or captain. [file:7]

Kubernetes is an open-source container orchestration system originally designed by Google and maintained by the CNCF. [file:7]

It is a platform for automating deployment, scaling, and operations of containers across clusters of hosts. [file:7]

The lecture also says Kubernetes is two things: [file:7]
- A cluster for running applications. [file:7]
- An orchestrator of cloud-native microservices applications. [file:7]

## Kubernetes cluster structure
The lecture describes a Kubernetes cluster as made up of: [file:7]
- **Masters** or head nodes. [file:7]
- **Workers**. [file:7]

## Masters / control plane
A Kubernetes master is a collection of system services that make up the **control plane** of the cluster. [file:7]

The simplest setup runs all master services on a single host. [file:7]

Master components listed in the lecture:
- **API server**: all communication between all components goes through it, and it is a RESTful endpoint on port 443. [file:7]
- **Cluster store**: persistently stores the entire cluster configuration and state. [file:7]
- **Controller manager**: watches the cluster through control loops and responds to events. [file:7]
- **Scheduler**: watches for new work and assigns it to appropriate healthy nodes. [file:7]

## Nodes / data plane
Nodes are the workers of a Kubernetes cluster. [file:7]

They do three things: watch the API server for assignments, execute new work, and report back to the control plane. [file:7]

Node components listed in the lecture:
- **Kubelet**: handles node registration, watches the API server for assignments, and reports back to the master. [file:7]
- **Container runtime**: performs tasks such as pulling images and starting or stopping containers. [file:7]
- **Kube-proxy**: reflects Kubernetes networking services on each node. [file:7]

## Packaging apps for Kubernetes
For an application to run on Kubernetes, the lecture says it must: [file:7]
1. Be packaged as a container. [file:7]
2. Be wrapped in a Pod. [file:7]
3. Be deployed via a declarative manifest file. [file:7]

## Running apps on Kubernetes
The lecture gives this pattern: [file:7]
1. Write the application as small independent services. [file:7]
2. Package each service in its own container. [file:7]
3. Define a Kubernetes Pod to run the containerized service. [file:7]
4. Deploy Pods using higher-level controllers such as Deployments, DaemonSets, StatefulSets, or CronJobs. [file:7]
5. POST the desired state to the cluster and let Kubernetes implement it. [file:7]

## Pods
This is one of the most important topics. [file:7]

A **Pod** is the atomic unit of scheduling in Kubernetes. [file:7]

The lecture explicitly asks whether you can deploy a container directly in Kubernetes and answers **no, not directly**, because the smallest deployable unit is a Pod, not a container. [file:7]

A Pod is an all-or-nothing wrapper for one or more tightly related containers that must stay together. [file:7]

Examples of multi-container Pods in the lecture:
- Service meshes. [file:7]
- Web containers with a helper container pulling fresh content. [file:7]
- Containers with a tightly coupled log scraper. [file:7]

## Pod behavior and sharing
A Pod is considered running if all its containers are scheduled and running. [file:7]

The Pod itself does not run the workload directly; it acts as a sandbox for hosting containers. [file:7]

Containers inside the same Pod share the same environment, including memory, volumes, and network stack. [file:7]

All containers in the same Pod share the Pod’s IP address and communicate through ports on the Pod’s localhost interface. [file:7]

## Pod atomicity and placement
The deployment of a Pod is an **atomic operation**, meaning the whole Pod is deployed or none of it is. [file:7]

A single Pod can only be scheduled to **one node**. [file:7]

## Pod lifecycle
Pods are created, live, and die. [file:7]

If a Pod dies unexpectedly, Kubernetes starts a new one in its place, but the replacement Pod has a **new ID and new IP address**. [file:7]

### Exam-ready implication
Pods are not reliable long-term identity endpoints, which is why higher-level abstractions like Services are needed. [file:7]

## Deployments
A **Deployment** is a higher-level Kubernetes object that wraps a Pod and adds capabilities such as scaling, zero-downtime updates, and versioned rollbacks. [file:7]

A deployment can be created from a YAML file specifying image and replica information. [file:7]

The lecture says Deployments implement a controller and watch loop that constantly checks whether current state matches desired state. [file:7]

### Declarative and imperative deployment
The lecture gives two approaches:
- **Declarative**: create a YAML file and apply it with `kubectl apply -f deployment.yaml`. [file:7]
- **Imperative**: use a command such as `kubectl run nginx --image=nginx:1.15.8 --replicas=2 --port=80`. [file:7]

## Desired state model
Kubernetes is based on a **desired state** model. [file:7]

If the current state differs from the desired state, Kubernetes acts to reduce the difference, such as creating missing replicas or updating running replicas to a newer image version. [file:7]

## Services
Pods are mortal and unreliable because they can die and be replaced with different IP addresses, especially during scaling and failure recovery. [file:7]

A **Service** provides reliable networking for a set of Pods. [file:7]

The lecture says Services give a stable front-end with a DNS name, IP address, and port, while load balancing traffic across a dynamic back-end set of Pods. [file:7]

Services operate at the TCP and UDP layers, so they do not provide application-layer routing intelligence. [file:7]

## Connecting Pods to Services
Services use **labels** and a **label selector** to determine which Pods should receive traffic. [file:7]

A Pod must have all required labels in the selector to be part of the Service’s back-end set. [file:7]

## Fast memory table
| Topic | What to remember |
|---|---|
| Orchestrator | Manages hosts and containers across a cluster and handles scheduling and scaling. [file:7] |
| Major tools | Kubernetes, Mesos, Docker Swarm. [file:7] |
| Swarm node roles | Managers and workers. [file:7] |
| Swarm scheduling unit | Service. [file:7] |
| Swarm HA | Powered by Raft consensus. [file:7] |
| Kubernetes cluster | Masters/control plane + worker nodes/data plane. [file:7] |
| Smallest K8s deployable unit | Pod, not container. [file:7] |
| Pod | Atomic scheduling unit and sandbox for containers. [file:7] |
| Deployment | Adds scaling, zero-downtime updates, rollbacks, desired-state control. [file:7] |
| Service | Adds stable networking and load balancing for changing Pods. [file:7] |

## What is most likely to appear in short answers
### 1) Why use orchestration?
Possible points:
- Simplifies container management at scale. [file:7]
- Handles availability, scaling, networking, and service discovery. [file:7]
- Supports self-healing, security, and rolling updates. [file:7]

### 2) Why does Swarm need Raft?
- Manager high availability needs a consensus mechanism. [file:7]
- Raft helps managers agree on one source of truth. [file:7]
- Leadership can continue despite some node failures. [file:7]

### 3) Why are Pods used instead of raw containers in Kubernetes?
- Pod is the atomic scheduling unit. [file:7]
- It supports all-or-nothing deployment of tightly coupled containers. [file:7]
- Containers in a Pod can share memory, volumes, and networking. [file:7]

### 4) Why are Services needed?
- Pods can die and be replaced. [file:7]
- Pod IPs change. [file:7]
- Services provide a stable DNS name, IP, port, and load balancing. [file:7]

### 5) Why are Deployments needed?
- They maintain desired state. [file:7]
- They support scaling, updates, rollbacks, and self-healing. [file:7]

## Sample multiple-choice questions
### Set 1
1. An orchestrator mainly helps with:  
A. Manual file editing only  
B. Managing and organizing hosts and containers across a cluster  
C. Replacing all operating systems  
D. Encrypting hard drives only  
**Answer: B** [file:7]

2. The main scheduling issue mentioned in the lecture is:  
A. Choosing coding style  
B. Resource allocation based on CPU, RAM, and disk requirements  
C. Choosing a web browser  
D. Deciding Linux vs Windows desktop themes  
**Answer: B** [file:7]

3. Which is an example of a container orchestration tool in the lecture?  
A. Kubernetes  
B. PostgreSQL  
C. Flask  
D. TensorFlow  
**Answer: A** [file:7]

4. Which feature is listed for orchestration tools?  
A. Rolling updates  
B. Printer calibration  
C. BIOS flashing  
D. Spreadsheet formatting  
**Answer: A** [file:7]

5. According to the lecture, Swarm is better suited to:  
A. Only the largest clusters in the world  
B. Small or medium clusters  
C. No clusters  
D. Only mobile devices  
**Answer: B** [file:7]

6. At a high level, Docker Swarm has two major components:  
A. A secure cluster and an orchestration engine  
B. A compiler and linker  
C. A browser and database  
D. A hypervisor and TLB  
**Answer: A** [file:7]

7. Swarm nodes can be configured as:  
A. Master and slave  
B. Manager and worker  
C. Client and browser  
D. Host and guest OS only  
**Answer: B** [file:7]

8. Swarm uses ___ to secure communications and roles.  
A. RAID  
B. TLS  
C. YAML  
D. NAT only  
**Answer: B** [file:7]

9. Which mode means a Docker host is participating in a swarm?  
A. Single Engine Mode  
B. Swarm Mode  
C. BIOS Mode  
D. Safe Mode  
**Answer: B** [file:7]

10. In Swarm, the atomic unit of scheduling is the:  
A. Pod  
B. Service  
C. Volume  
D. Dockerfile  
**Answer: B** [file:7]

11. A Swarm service adds features such as:  
A. Scaling and rolling updates  
B. Only local file editing  
C. BIOS configuration  
D. ISA translation  
**Answer: A** [file:7]

12. When a container is wrapped in a Swarm service, it is called a:  
A. Label  
B. Task or replica  
C. Pod sandbox  
D. Namespace  
**Answer: B** [file:7]

13. Swarm manager high availability is powered by:  
A. Docker Compose  
B. Raft  
C. Kubelet  
D. VXLAN only  
**Answer: B** [file:7]

14. Raft is a:  
A. Compression algorithm  
B. Consensus algorithm  
C. Scheduling language  
D. Storage driver  
**Answer: B** [file:7]

15. In a normal Raft arrangement, there is:  
A. No leader  
B. One leader and the rest followers  
C. All leaders  
D. Only candidates  
**Answer: B** [file:7]

16. Time in Raft is divided into:  
A. Threads  
B. Terms  
C. Pages  
D. Labels  
**Answer: B** [file:7]

17. A follower that stops receiving communication will:  
A. Shut down permanently  
B. Start an election after an election timeout  
C. Become a worker node  
D. Delete the cluster store  
**Answer: B** [file:7]

18. Which RPC is used as heartbeat in the lecture?  
A. RequestVote only  
B. AppendEntry  
C. kubectl apply  
D. kube-proxy  
**Answer: B** [file:7]

19. If a Raft candidate receives votes from a majority of servers, it becomes:  
A. Follower  
B. Leader  
C. Worker  
D. Pod  
**Answer: B** [file:7]

20. Typical election timeouts in the slides are:  
A. 1–2 seconds  
B. 100–500 ms  
C. 10–20 minutes  
D. 24 hours  
**Answer: B** [file:7]

### Set 2
21. Which command creates a new swarm?  
A. docker service create  
B. docker swarm init  
C. kubectl apply  
D. docker volume create  
**Answer: B** [file:7]

22. Which command reveals the command and token to join a worker or manager?  
A. docker swarm join-token  
B. docker node ls  
C. docker service ps  
D. docker service rm  
**Answer: A** [file:7]

23. Which command lists all nodes and shows managers and leader?  
A. docker node ls  
B. docker service scale  
C. docker volume inspect  
D. docker swarm inspect  
**Answer: A** [file:7]

24. Which command scales replicas up or down in a Swarm service?  
A. docker service logs  
B. docker service scale  
C. docker node ls  
D. docker swarm init  
**Answer: B** [file:7]

25. Which command removes a service and all its replicas?  
A. docker service rm  
B. docker volume rm  
C. docker swarm leave-token  
D. docker node rm-service  
**Answer: A** [file:7]

26. Swarm nodes may not be on the same LAN, so Docker uses:  
A. RAID  
B. VXLAN overlay networking  
C. BIOS tunneling  
D. TLB routing  
**Answer: B** [file:7]

27. The recommended way to persist container data is with:  
A. Labels  
B. Volumes  
C. Pods  
D. YAML only  
**Answer: B** [file:7]

28. Which command creates a new volume?  
A. docker volume create  
B. docker service create  
C. docker pod create  
D. kubectl volume create  
**Answer: A** [file:7]

29. Kubernetes is maintained by the:  
A. GNU Foundation  
B. CNCF  
C. IEEE only  
D. Apache Foundation only  
**Answer: B** [file:7]

30. Kubernetes was originally designed by:  
A. Amazon  
B. Google  
C. Docker, Inc.  
D. Microsoft  
**Answer: B** [file:7]

31. Kubernetes is described as a platform for automating:  
A. Only networking  
B. Deployment, scaling, and operations of containers across clusters  
C. Only BIOS updates  
D. Only file compression  
**Answer: B** [file:7]

32. A Kubernetes cluster is made up of:  
A. Compilers and linkers  
B. Masters and workers  
C. APIs and browsers  
D. Only Pods  
**Answer: B** [file:7]

33. The control plane of a Kubernetes cluster is made up of:  
A. Worker containers only  
B. Master system services  
C. Labels and selectors only  
D. Volumes only  
**Answer: B** [file:7]

34. All communication between Kubernetes components goes through the:  
A. Scheduler  
B. API server  
C. Pod  
D. Volume driver  
**Answer: B** [file:7]

35. The Kubernetes API server is described as a RESTful endpoint on port:  
A. 80  
B. 22  
C. 443  
D. 8080  
**Answer: C** [file:7]

36. Which master component persistently stores cluster configuration and state?  
A. Scheduler  
B. Cluster store  
C. Kube-proxy  
D. Pod sandbox  
**Answer: B** [file:7]

37. Which component assigns new work to healthy nodes?  
A. Scheduler  
B. Kubelet  
C. Service  
D. Volume  
**Answer: A** [file:7]

38. Which node component watches the API server for work and reports back?  
A. Kubelet  
B. Docker daemon  
C. Controller manager  
D. Cluster store  
**Answer: A** [file:7]

39. Which node component reflects networking services on each node?  
A. Kube-proxy  
B. Kube-store  
C. Kube-cache  
D. Kube-shell  
**Answer: A** [file:7]

40. For an app to run on Kubernetes, it must be wrapped in a:  
A. Service  
B. Pod  
C. Volume  
D. Node  
**Answer: B** [file:7]

41. The atomic unit of scheduling in Kubernetes is the:  
A. Service  
B. Pod  
C. Container runtime  
D. Node  
**Answer: B** [file:7]

42. Can you deploy a container directly in Kubernetes according to the lecture?  
A. Yes, always directly  
B. No, not directly  
C. Only on weekends  
D. Only through Mesos  
**Answer: B** [file:7]

43. Containers inside the same Pod share the same:  
A. Hypervisor  
B. Environment, including network stack and volumes  
C. External DNS domain only  
D. Swarm service token  
**Answer: B** [file:7]

44. All containers in the same Pod share the same:  
A. Host BIOS  
B. Pod IP address  
C. External cloud account  
D. TLS certificate authority  
**Answer: B** [file:7]

45. A single Pod can be scheduled to:  
A. Multiple nodes at once  
B. A single node only  
C. Every node in the cluster  
D. No node directly  
**Answer: B** [file:7]

46. If a Pod dies unexpectedly, Kubernetes:  
A. Does nothing  
B. Starts a new Pod in its place  
C. Permanently disables the node  
D. Converts it to a Service  
**Answer: B** [file:7]

47. A Deployment adds features such as:  
A. Scaling, zero-downtime updates, and rollbacks  
B. BIOS access and disk partitioning  
C. Only static IP assignment  
D. Encryption at the application layer  
**Answer: A** [file:7]

48. Which command is the declarative deployment example from the lecture?  
A. kubectl apply -f deployment.yaml  
B. docker swarm init  
C. docker volume create  
D. kubelet run deployment  
**Answer: A** [file:7]

49. Services are needed because Pods:  
A. Never change IPs  
B. Are mortal and can be replaced with different IPs  
C. Always have stable identities forever  
D. Cannot communicate over TCP  
**Answer: B** [file:7]

50. Services connect to Pods using:  
A. BIOS settings  
B. Labels and label selectors  
C. Hypervisor interrupts  
D. VM snapshots  
**Answer: B** [file:7]

## Sample short-answer questions with model points
### SAQ 1
**Question:** What is container orchestration and why is it needed?  
**Model points:** Container orchestration provides a framework for managing containers at scale. It simplifies management, handles scheduling, availability, scaling, networking, load balancing, health checks, self-healing, security, and rolling updates. [file:7]

### SAQ 2
**Question:** Compare Kubernetes and Docker Swarm briefly.  
**Model points:** Both are orchestration tools, but the lecture positions Kubernetes for complex applications and enterprise-level scale, while Swarm is better suited to small or medium clusters. [file:7]

### SAQ 3
**Question:** Describe Docker Swarm architecture at a high level.  
**Model points:** Swarm consists of a secure cluster plus an orchestration engine. Nodes can be managers or workers, communications are secured with TLS, and managers elect a leader to track the swarm. [file:7]

### SAQ 4
**Question:** What is the atomic scheduling unit in Docker Swarm?  
**Model points:** The atomic unit of scheduling is the service. A service wraps containers and adds scaling, rolling updates, and simple rollback features, and the resulting running instances are tasks or replicas. [file:7]

### SAQ 5
**Question:** Why does Docker Swarm use Raft?  
**Model points:** Swarm uses Raft to provide high availability among managers. Raft lets managers agree on a single source of truth and continue operating even if some nodes fail. [file:7]

### SAQ 6
**Question:** Explain the main Raft states and election process.  
**Model points:** Nodes start as followers, become candidates after timeout without heartbeats, vote for themselves and request votes, and become leaders if they receive a majority. Leaders then send heartbeats to maintain authority. [file:7]

### SAQ 7
**Question:** What is Kubernetes?  
**Model points:** Kubernetes is an open-source container orchestration platform originally designed by Google and maintained by the CNCF. It automates deployment, scaling, and operations of containers across clusters. [file:7]

### SAQ 8
**Question:** What are the two major parts of a Kubernetes cluster?  
**Model points:** A Kubernetes cluster is made of masters, which form the control plane, and worker nodes, which execute workloads and report back. [file:7]

### SAQ 9
**Question:** Explain the main Kubernetes master components.  
**Model points:** The API server is the communication hub, the cluster store holds persistent state, the controller manager watches and reacts to events, and the scheduler assigns work to healthy nodes. [file:7]

### SAQ 10
**Question:** Explain the main Kubernetes node components.  
**Model points:** Kubelet registers the node and watches the API server, the container runtime manages container execution, and kube-proxy implements networking services on the node. [file:7]

### SAQ 11
**Question:** Why is a Pod used in Kubernetes instead of deploying a raw container directly?  
**Model points:** Kubernetes uses Pods as the smallest deployable and schedulable unit. A Pod acts as a wrapper and sandbox for one or more closely related containers that must be kept together. [file:7]

### SAQ 12
**Question:** What properties do containers inside the same Pod share?  
**Model points:** They share the same environment, including memory, volumes, network stack, and the Pod’s IP address, and communicate over localhost ports. [file:7]

### SAQ 13
**Question:** What problem does a Deployment solve?  
**Model points:** Deployments add scaling, zero-downtime updates, rollbacks, and desired-state management through a control loop that keeps current state aligned with desired state. [file:7]

### SAQ 14
**Question:** Why are Services needed in Kubernetes?  
**Model points:** Pods are unreliable long-term endpoints because they can die and be replaced with different IPs. Services provide a stable DNS name, IP, port, and load balancing across dynamic Pods. [file:7]

### SAQ 15
**Question:** How do Services know which Pods to send traffic to?  
**Model points:** Services use labels and label selectors. Only Pods with the required labels are selected into the Service backend. [file:7]

## Likely exam traps
- Do not confuse the atomic unit of scheduling in **Swarm** with that in **Kubernetes**: Swarm uses **services**, Kubernetes uses **Pods**. [file:7]
- Do not say a Kubernetes container is deployed directly; the lecture explicitly says **no, not directly**. [file:7]
- Do not forget that replacement Pods get **new IP addresses**, which is why Services matter. [file:7]
- Do not confuse **Deployment** with **Service**; Deployment manages desired state and replicas, while Service provides stable networking. [file:7]
- Do not confuse **control plane** components with **node** components. [file:7]

## 15-minute revision plan
1. Memorize what orchestration does and the listed orchestration features. [file:7]
2. Memorize Swarm basics: managers, workers, services, Raft, and main commands. [file:7]
3. Memorize Kubernetes architecture: masters/control plane and worker nodes/data plane. [file:7]
4. Memorize Pod, Deployment, and Service definitions and differences. [file:7]
5. Practice writing one short answer on Raft, one on Pods, and one on Services. [file:7]

## Ultra-short cram sheet
- Orchestrator = schedules and manages containers across clusters. [file:7]
- Swarm roles = manager and worker. [file:7]
- Swarm scheduling unit = service. [file:7]
- Swarm HA = Raft consensus. [file:7]
- Kubernetes = open-source orchestrator from Google/CNCF. [file:7]
- Kubernetes cluster = control plane + worker nodes. [file:7]
- Smallest deployable unit = Pod, not container. [file:7]
- Deployment = scaling, updates, rollback, desired state. [file:7]
- Service = stable DNS/IP/port + load balancing for Pods. [file:7]
- Services use labels and selectors to find Pods. [file:7]

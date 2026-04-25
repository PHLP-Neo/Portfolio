# FIT5225 Week 1 Cheat Sheet

Based on the attached Week 1 lecture slides: *1-Principle.pdf* [file:1]

## What this week is about
Week 1 introduces the path from distributed systems to cloud computing, and it links core distributed-system ideas to cloud design choices and service models. [file:1]

## Learning outcomes to remember
- Describe fundamental principles and paradigms of cloud computing. [file:1]
- Identify appropriate design choices when developing real-world cloud computing applications. [file:1]

## Distributed system: key definition
A distributed system is:
- hardware or software components located on networked computers that coordinate by passing messages; or [file:1]
- a collection of independent computers that appears to users as a single coherent system. [file:1]

### Fast exam phrasing
A **computer network** is just interconnected computers exchanging messages using protocols, while a **distributed system** is multiple computers working together as one system and hiding communication details from users. [file:1]

## Why distributed systems exist
Main reason: **resource sharing**. [file:1]

Shared resources include:
- Hardware resources, such as disks, printers, and scanners. [file:1]
- Software resources, such as files and databases. [file:1]
- Other resources, such as processing power, memory, and bandwidth. [file:1]

Benefits of resource sharing:
- Economy. [file:1]
- Reliability. [file:1]
- Availability. [file:1]
- Scalability. [file:1]

## Core consequences of distributed systems
These 3 are highly testable:
- **Concurrency**: multiple clients may access or update the same resource at the same time. [file:1]
- **No global clock**: there is no perfectly shared time reference across all machines. [file:1]
- **Independent failures**: one machine or component can fail while others continue working. [file:1]

### Concurrency handling
- Making access sequential can handle concurrency, but it slows the system down. [file:1]
- Semaphores are a standard mechanism for concurrency control. [file:1]

## Distributed system challenges
Memorize this list:
- Heterogeneity. [file:1]
- Openness. [file:1]
- Security. [file:1]
- Scalability. [file:1]
- Failure handling. [file:1]
- Concurrency. [file:1]
- Transparency. [file:1]
- Quality of Service (QoS). [file:1]

## Heterogeneity
Meaning: distributed systems use different kinds of networks, hardware, operating systems, programming languages, and implementations by different developers. [file:1]

Ways to handle heterogeneity:
- Standard protocols. [file:1]
- Agreed message formats and data types. [file:1]
- Agreed APIs. [file:1]
- Middleware. [file:1]
- Portable code. [file:1]

### Good short-answer justification
Use standards, common message formats, APIs, and middleware to make unlike components interoperate cleanly. [file:1]

## Openness
Openness means the system can be extended by adding hardware or software resources. [file:1]

How to support openness:
- Publish key interfaces. [file:1]
- Use a uniform communication mechanism across published interfaces. [file:1]
- Ensure implementations follow published standards. [file:1]

## Security
Three aspects of security:
- **Confidentiality**: prevent unauthorized disclosure. [file:1]
- **Integrity**: prevent unauthorized alteration or corruption. [file:1]
- **Availability**: protect access to the system and services. [file:1]

Security mechanisms:
- Encryption, such as Blowfish and RSA. [file:1]
- Authentication, such as passwords and public-key authentication. [file:1]
- Authorization, such as access control lists. [file:1]

Unresolved or hard challenges mentioned:
- Denial-of-service attacks. [file:1]
- Security against mobile code, such as executable attachments. [file:1]

## Scalability
A system is scalable if it can handle growth in the number of users. [file:1]

Scalability challenges:
- Physical resource cost should grow roughly with users, ideally O(n). [file:1]
- Algorithms should scale well; O(log n) is scalable, while O(n^2) is not a good scalable example. [file:1]
- Resources should not run out, such as IP addresses. [file:1]
- Avoid performance bottlenecks by preferring decentralized algorithms. [file:1]

### Exam-ready wording
A scalable system grows without unacceptable cost, bottlenecks, or performance collapse as users and workload increase. [file:1]

## Failure handling
Approaches to failure handling:
- **Detecting**: identify some failures, such as corruption detected by checksums. [file:1]
- **Masking**: hide or reduce some failures, such as timeout plus retransmission. [file:1]
- **Tolerating**: report failure to users and keep operating where possible. [file:1]
- **Recovery**: restore the original state after failure, such as rollback. [file:1]
- **Redundancy**: use duplicate components or routes so service continues after failure. [file:1]

## Transparency
Transparency means hiding distributed-system complexity from users and application programmers. [file:1]

Types of transparency:
- Location transparency. [file:1]
- Access transparency. [file:1]
- Concurrency transparency. [file:1]
- Replication transparency. [file:1]
- Failure transparency. [file:1]
- Performance transparency. [file:1]
- Security transparency. [file:1]
- Management transparency. [file:1]

### Easy memory trick
Think: hide **where**, **how**, **who else**, **copies**, **failures**, **speed changes**, **security details**, and **management complexity**. [file:1]

## Quality of Service (QoS)
QoS asks not only whether a service works, but how well it works. [file:1]

Main nonfunctional properties affecting QoS:
- Reliability. [file:1]
- Security. [file:1]
- Performance. [file:1]
- Adaptability. [file:1]
- Availability. [file:1]

## Architectural patterns in distributed systems
Two major architectures:
- **Client-server**: clients invoke services on servers and receive results back. [file:1]
- **Peer-to-peer (P2P)**: each process acts cooperatively as both client and server. [file:1]

### Client-server vs P2P
| Topic | Client-server | Peer-to-peer |
|---|---|---|
| Role structure | Separate client and server roles. [file:1] | Nodes act as both client and server. [file:1] |
| Control style | More centralized. [file:1] | More decentralized. [file:1] |
| Typical risk | Server can become bottleneck or single point of failure. [file:1] | Coordination can be harder across many peers. [file:1] |

## Layering
Software architecture can be abstracted into layers or modules, where each layer provides services to the next. [file:1]

Two important layers for distributed systems in the slides:
- Platform. [file:1]
- Middleware. [file:1]

### Middleware in one line
Middleware helps different distributed components communicate and work together despite heterogeneity. [file:1]

## Trends in distributed systems
The slides mention these trends:
- Pervasive networking technology. [file:1]
- Ubiquitous computing and user mobility support. [file:1]
- Increasing demand for multimedia services. [file:1]
- Viewing distributed systems as a utility. [file:1]

## Distributed computing as utility
Distributed resources can be treated like a utility, similar to water or electricity, and rented from service suppliers rather than owned by end users. [file:1]

This utility view leads directly to the idea of cloud computing. [file:1]

## Cloud computing definitions
The Berkeley view summarizes cloud computing with: the illusion of infinite computing resources, elimination of up-front commitment, and pay-for-use as needed. [file:1]

The NIST definition says cloud computing provides ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources that can be rapidly provisioned and released with minimal management effort or provider interaction. [file:1]

### Simple exam definition
Cloud computing is an IT paradigm that provides rapidly provisioned shared configurable resources as services, often over the Internet, with minimal management effort. [file:1]

## Why cloud computing matters
Cloud computing allows businesses to outsource IT facilities to cloud providers and avoid expensive up-front infrastructure investment. [file:1]

The slides stress these cloud ideas:
- Pay-as-you-go. [file:1]
- Illusion of infinite resources. [file:1]
- No up-front cost. [file:1]

## Cloud vs conventional computing
| Conventional computing | Cloud computing |
|---|---|
| Buy and own infrastructure. [file:1] | Subscribe to services. [file:1] |
| Install, configure, test, verify, evaluate, and manage it yourself. [file:1] | Use services and pay based on usage and QoS. [file:1] |
| Often provision for peak demand. [file:1] | Pay for what you use. [file:1] |
| Very expensive up-front. [file:1] | Lower initial commitment. [file:1] |

## Basic cloud concept
Cloud is the “invisible” backend for many applications such as Dropbox, LinkedIn, GitHub, Office 365, Amazon, and Slack. [file:1]

The cloud symbol abstracts the underlying complexity of hardware, software, network, service, and storage. [file:1]

## Cloud enabling technologies
The slides place cloud computing at the intersection of: [file:1]
- Hardware, including hardware virtualization and multi-core chips. [file:1]
- Distributed computing, including utility and grid computing. [file:1]
- Internet technologies, including SOA, Web 2.0, web services, and mashups. [file:1]
- Systems management, including autonomic computing and data center automation. [file:1]

## Virtualization
Virtualization hides the physical characteristics of a computing platform and presents an abstract computing platform to users. [file:1]

The controlling software is called a **hypervisor** or **virtual machine monitor**, with examples including Xen, KVM, and VMware ESXi. [file:1]

Related factors that increased adoption:
- Multi-core chips. [file:1]
- Paravirtualization. [file:1]
- Hardware-assisted virtualization. [file:1]
- Live migration of VMs. [file:1]

## Economics of cloud users
The slides highlight three economic ideas:
- Over-provisioning causes underutilized resources. [file:1]
- Under-provisioning causes heavy penalties and lost revenue. [file:1]
- Cloud helps match capacity to demand and supports pay-by-use instead of provisioning for peak. [file:1]

### Good short-answer angle
Cloud is economically attractive because it reduces waste from over-provisioning and reduces business loss from under-provisioning. [file:1]

## Cloud deployment models
Memorize these 4:
- **Private cloud**: owned for one organization, on-premise or off-premise. [file:1]
- **Public cloud**: shared with the general public. [file:1]
- **Community cloud**: shared by several entities with a common purpose. [file:1]
- **Hybrid cloud**: any combination of two or more private, community, or public clouds. [file:1]

## Cloud service models
Memorize these 3 and examples:
- **SaaS**: provides software applications accessible through thin clients such as web browsers; example: Salesforce.com. [file:1]
- **PaaS**: provides programming languages and tools to deploy applications on cloud infrastructure; example: Google App Engine. [file:1]
- **IaaS**: provides compute, storage, network, and other fundamental resources such as VMs or containers; examples: Amazon EC2 and S3. [file:1]

### Very short distinction
- SaaS = use application. [file:1]
- PaaS = deploy application. [file:1]
- IaaS = provision infrastructure. [file:1]

## Fast memory table
| Topic | What to remember |
|---|---|
| Distributed system | Independent computers appear as one coherent system. [file:1] |
| Main motivation | Resource sharing. [file:1] |
| 3 consequences | Concurrency, no global clock, independent failures. [file:1] |
| Main challenges | Heterogeneity, openness, security, scalability, failure handling, concurrency, transparency, QoS. [file:1] |
| Main architectures | Client-server and P2P. [file:1] |
| Cloud idea | Utility-style computing over the Internet. [file:1] |
| Cloud economics | Pay-as-you-go, no up-front cost, illusion of infinite resources. [file:1] |
| Deployment models | Private, public, community, hybrid. [file:1] |
| Service models | SaaS, PaaS, IaaS. [file:1] |

## What is most likely to appear in short answers
### 1) Justify cloud over conventional infrastructure
Possible points:
- Lower up-front cost. [file:1]
- Pay only for usage. [file:1]
- Better match between demand and capacity. [file:1]
- Rapid provisioning and release of resources. [file:1]
- Easier scaling. [file:1]

### 2) Justify an architecture choice
- Choose **client-server** when centralized service/control is acceptable and clear server-managed processing is needed. [file:1]
- Choose **P2P** when decentralized cooperation among nodes is beneficial. [file:1]

### 3) Justify middleware / standards
- They reduce heterogeneity problems and improve interoperability. [file:1]

### 4) Explain why transparency matters
- It simplifies system use and programming by hiding location, replication, failure, and other distributed complexities. [file:1]

## Sample multiple-choice questions
### Set 1
1. Which statement best defines a distributed system?  
A. A single powerful computer with many users  
B. A set of networked computers that appears as one coherent system  
C. A database shared by multiple departments  
D. A router connecting many machines  
**Answer: B** [file:1]

2. In the slides, the main motivation for distributed systems is:  
A. Entertainment  
B. Resource sharing  
C. Device miniaturization  
D. Compiler optimization  
**Answer: B** [file:1]

3. Which is **not** one of the three core consequences of distributed systems listed in the lecture?  
A. Concurrency  
B. No global clock  
C. Independent failures  
D. Infinite storage  
**Answer: D** [file:1]

4. Which challenge refers to supporting different hardware, OSs, languages, and implementations?  
A. Transparency  
B. Heterogeneity  
C. QoS  
D. Availability  
**Answer: B** [file:1]

5. Which of the following helps address heterogeneity?  
A. Randomized interfaces  
B. Standard protocols and agreed APIs  
C. Proprietary message formats only  
D. Removing middleware  
**Answer: B** [file:1]

6. Openness is mainly about:  
A. Hiding all interfaces  
B. Extending the system by adding hardware or software resources  
C. Preventing all updates  
D. Encrypting every packet  
**Answer: B** [file:1]

7. Which trio represents the three aspects of security?  
A. Speed, cost, usability  
B. Confidentiality, integrity, availability  
C. Authentication, APIs, auditing  
D. Privacy, portability, pricing  
**Answer: B** [file:1]

8. Which mechanism is associated with authentication?  
A. Access control list  
B. Passwords  
C. Checksum  
D. Replication  
**Answer: B** [file:1]

9. Which of the following is a scalability challenge from the slides?  
A. Reducing monitor size  
B. Avoiding performance bottlenecks  
C. Eliminating all users  
D. Replacing middleware with firmware  
**Answer: B** [file:1]

10. A search algorithm with complexity O(log n) is presented as:  
A. Not scalable  
B. Scalable  
C. Impossible  
D. Equivalent to O(n^2)  
**Answer: B** [file:1]

11. Making access sequential is one way to handle concurrency, but it:  
A. Improves transparency  
B. Slows down the system  
C. Removes failures  
D. Increases heterogeneity  
**Answer: B** [file:1]

12. Which is a well-accepted mechanism for handling concurrency?  
A. Semaphores  
B. DNS  
C. Firewalls  
D. Hypervisors  
**Answer: A** [file:1]

13. Which failure-handling approach uses checksums to identify corrupted data?  
A. Recovery  
B. Detecting  
C. Redundancy  
D. Tolerating  
**Answer: B** [file:1]

14. Timeout and retransmission are examples of:  
A. Masking failures  
B. Publishing interfaces  
C. Virtualization  
D. Under-provisioning  
**Answer: A** [file:1]

15. Rollback is associated with:  
A. Openness  
B. Recovery  
C. Replication transparency  
D. Pay-as-you-go  
**Answer: B** [file:1]

16. Redundancy improves failure tolerance by:  
A. Removing all network links  
B. Using duplicate components or paths  
C. Disabling users  
D. Eliminating APIs  
**Answer: B** [file:1]

17. Transparency is mainly about:  
A. Showing every implementation detail to the user  
B. Hiding distributed-system complexity from users and programmers  
C. Making interfaces colorful  
D. Encrypting storage  
**Answer: B** [file:1]

18. Which is a type of transparency listed in the slides?  
A. Location transparency  
B. Compiler transparency  
C. Battery transparency  
D. Keyboard transparency  
**Answer: A** [file:1]

19. Which of the following is part of QoS?  
A. Performance  
B. Keyboard layout  
C. IP version only  
D. Processor brand  
**Answer: A** [file:1]

20. Which architecture has clients invoking services on servers?  
A. Peer-to-peer  
B. Client-server  
C. Blockchain only  
D. Mesh-only architecture  
**Answer: B** [file:1]

### Set 2
21. In a peer-to-peer system, each node can act as:  
A. Only a client  
B. Only a server  
C. Both client and server  
D. Only a router  
**Answer: C** [file:1]

22. Which layer is explicitly named as important in distributed systems?  
A. Browser cache layer  
B. Middleware  
C. GPU driver layer only  
D. BIOS interface layer  
**Answer: B** [file:1]

23. “Pervasive” networking means:  
A. Limited to labs  
B. Diffused throughout every part  
C. Used only in cloud security  
D. Controlled only by one vendor  
**Answer: B** [file:1]

24. “Ubiquitous” computing means:  
A. Everywhere  
B. Optional  
C. Centralized  
D. Offline  
**Answer: A** [file:1]

25. Distributed resources viewed like water or electricity refers to:  
A. Grid instability  
B. Utility computing  
C. Local-only computing  
D. Single-user systems  
**Answer: B** [file:1]

26. According to the Berkeley view, cloud computing includes:  
A. Mandatory up-front investment  
B. Illusion of infinite computing resources  
C. No network access  
D. Fixed hardware ownership  
**Answer: B** [file:1]

27. Which phrase is central to the NIST definition?  
A. Offline standalone access  
B. On-demand network access to shared configurable resources  
C. Physical-only server ownership  
D. Manual provisioning by default  
**Answer: B** [file:1]

28. Which is **not** a cloud benefit highlighted in the lecture?  
A. No up-front cost  
B. Pay-as-you-go  
C. Illusion of infinite resources  
D. Guaranteed zero failures forever  
**Answer: D** [file:1]

29. Conventional computing often provisions to meet:  
A. Minimum needs only  
B. Peak needs  
C. No needs  
D. Academic examples only  
**Answer: B** [file:1]

30. Cloud computing is the invisible backend to many applications such as:  
A. Only calculators  
B. Dropbox and Slack  
C. Only desktop BIOS  
D. USB drivers  
**Answer: B** [file:1]

31. Which is part of the cloud-computing intersection diagram?  
A. Systems management  
B. Agriculture  
C. Quantum optics only  
D. Manual paperwork  
**Answer: A** [file:1]

32. Virtualization mainly hides:  
A. User passwords  
B. Physical characteristics of the platform  
C. Network cables only  
D. Application bugs  
**Answer: B** [file:1]

33. Another name for a hypervisor is:  
A. Message broker  
B. Virtual machine monitor  
C. Load balancer  
D. API gateway  
**Answer: B** [file:1]

34. Which is named as a hypervisor example?  
A. KVM  
B. PostgreSQL  
C. Flask  
D. Hadoop  
**Answer: A** [file:1]

35. Over-provisioning mainly leads to:  
A. Underutilized resources  
B. Better peak matching without cost  
C. Zero waste  
D. Infinite performance  
**Answer: A** [file:1]

36. Under-provisioning may lead to:  
A. Lost revenue  
B. Lower latency always  
C. No penalties  
D. Better utilization without risk  
**Answer: A** [file:1]

37. Which deployment model is shared with the general public?  
A. Private cloud  
B. Public cloud  
C. Community cloud only for one firm  
D. Hybrid cloud only on-premise  
**Answer: B** [file:1]

38. Which deployment model combines two or more cloud types?  
A. Public  
B. Private  
C. Hybrid  
D. Dedicated bare metal only  
**Answer: C** [file:1]

39. Which service model provides software through a web browser or thin client?  
A. IaaS  
B. PaaS  
C. SaaS  
D. FaaS only  
**Answer: C** [file:1]

40. Which service model provides programming languages and tools for deploying applications?  
A. SaaS  
B. PaaS  
C. IaaS  
D. LAN  
**Answer: B** [file:1]

41. Which service model provides processing, storage, network, and other basic resources?  
A. SaaS  
B. PaaS  
C. IaaS  
D. DNSaaS  
**Answer: C** [file:1]

42. Which example is given for PaaS?  
A. Salesforce.com  
B. Google App Engine  
C. Amazon S3 only as SaaS  
D. Microsoft Word desktop  
**Answer: B** [file:1]

43. Which example is given for IaaS?  
A. Amazon EC2/S3  
B. Salesforce.com  
C. Google Docs in browser  
D. Local compiler  
**Answer: A** [file:1]

44. Which statement best distinguishes distributed systems from computer networks?  
A. Distributed systems always use one computer  
B. Distributed systems hide communication and separation from users  
C. Computer networks always hide all details  
D. There is no difference  
**Answer: B** [file:1]

45. Which item belongs to QoS rather than security mechanisms?  
A. Authorization  
B. Reliability  
C. Encryption  
D. Access control list  
**Answer: B** [file:1]

## Sample short-answer questions with model points
### SAQ 1
**Question:** Explain the difference between a computer network and a distributed system.  
**Model points:** A computer network is a set of spatially separated interconnected computers exchanging messages using protocols, while a distributed system is multiple computers working together as one coherent system and hiding communication/separation details from users. [file:1]

### SAQ 2
**Question:** Why are distributed systems used?  
**Model points:** They support resource sharing across hardware, software, processing power, memory, and bandwidth, and they improve economy, reliability, availability, and scalability. [file:1]

### SAQ 3
**Question:** Name and explain the three key consequences of distributed systems.  
**Model points:** Concurrency means many clients may access/update a resource simultaneously; no global clock means there is no single perfect shared time source; independent failures means one component may fail while others continue. [file:1]

### SAQ 4
**Question:** How can heterogeneity be handled in distributed systems?  
**Model points:** Use standard protocols, agreed message formats, agreed APIs, middleware, and portable code so unlike systems can interoperate. [file:1]

### SAQ 5
**Question:** What is openness, and how is it supported?  
**Model points:** Openness is the ability to extend a system by adding hardware or software resources; it is supported by publishing interfaces, using uniform communication mechanisms, and enforcing published standards. [file:1]

### SAQ 6
**Question:** Explain confidentiality, integrity, and availability.  
**Model points:** Confidentiality protects against unauthorized disclosure, integrity protects against alteration/corruption, and availability protects access to services and resources. [file:1]

### SAQ 7
**Question:** What makes a system scalable?  
**Model points:** It can handle user growth without unacceptable resource cost, performance loss, resource exhaustion, or centralized bottlenecks. [file:1]

### SAQ 8
**Question:** Explain five approaches to failure handling.  
**Model points:** Detecting identifies some failures; masking reduces visible impact; tolerating reports failure while continuing where possible; recovery restores system state; redundancy uses extra components or routes for resilience. [file:1]

### SAQ 9
**Question:** Why is transparency important in distributed systems?  
**Model points:** It hides complexity such as location, replication, concurrency, and failures, making systems easier to use and program. [file:1]

### SAQ 10
**Question:** What is QoS in distributed systems?  
**Model points:** QoS concerns how well a service works, especially reliability, security, performance, adaptability, and availability. [file:1]

### SAQ 11
**Question:** Compare client-server and peer-to-peer architectures.  
**Model points:** In client-server, clients request services from servers; in peer-to-peer, nodes cooperate as equals and can act as both client and server. [file:1]

### SAQ 12
**Question:** What is cloud computing?  
**Model points:** Cloud computing is an IT paradigm that provides access to shared configurable resources as services that can be rapidly provisioned and released with minimal management effort, often over the Internet. [file:1]

### SAQ 13
**Question:** Why is cloud computing economically attractive?  
**Model points:** It avoids expensive up-front investment, reduces waste from over-provisioning, reduces penalties from under-provisioning, and supports pay-as-you-go usage. [file:1]

### SAQ 14
**Question:** Explain virtualization and its role in cloud computing.  
**Model points:** Virtualization hides physical platform details and presents abstract computing resources, enabling flexible provisioning and management; it is controlled by a hypervisor or virtual machine monitor. [file:1]

### SAQ 15
**Question:** Distinguish private, public, community, and hybrid cloud deployment models.  
**Model points:** Private is for one organization, public is shared with the general public, community is shared by several entities with a common purpose, and hybrid combines two or more cloud types. [file:1]

### SAQ 16
**Question:** Distinguish SaaS, PaaS, and IaaS.  
**Model points:** SaaS provides complete applications, PaaS provides app-development/deployment platforms, and IaaS provides basic computing infrastructure like VMs, storage, and networking. [file:1]

## Likely exam traps
- Do not confuse **computer network** with **distributed system**. [file:1]
- Do not confuse **security mechanisms** (encryption, authentication, authorization) with **security goals** (CIA). [file:1]
- Do not confuse **deployment models** (private/public/community/hybrid) with **service models** (SaaS/PaaS/IaaS). [file:1]
- Do not say cloud means “just virtualization”; the slides show cloud as a convergence of multiple areas. [file:1]
- Do not forget that **transparency** is about hiding complexity. [file:1]

## 15-minute revision plan
1. Memorize: definitions of distributed system, cloud computing, virtualization. [file:1]
2. Memorize: 8 distributed-system challenges. [file:1]
3. Memorize: 3 distributed-system consequences. [file:1]
4. Memorize: deployment models and service models with one example each. [file:1]
5. Practice writing 4-5 sentence justifications for cloud adoption, architecture choice, and transparency. [file:1]

## Ultra-short cram sheet
- Distributed system = many independent computers appearing as one coherent system. [file:1]
- Main reason = resource sharing. [file:1]
- 3 consequences = concurrency, no global clock, independent failures. [file:1]
- Challenges = heterogeneity, openness, security, scalability, failure handling, concurrency, transparency, QoS. [file:1]
- Architectures = client-server, P2P. [file:1]
- Cloud = on-demand shared configurable resources over network with minimal management. [file:1]
- Cloud benefits = pay-as-you-go, no up-front cost, illusion of infinite resources. [file:1]
- Deployment = private, public, community, hybrid. [file:1]
- Service = SaaS, PaaS, IaaS. [file:1]

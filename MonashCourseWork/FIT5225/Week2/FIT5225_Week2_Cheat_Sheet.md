# FIT5225 Week 2 Cheat Sheet

Based on the attached Week 2 lecture slides: *2-Virtualization.pdf* [file:3]

## What this week is about
Week 2 focuses on virtualization, especially hardware virtualization, hypervisors, CPU/memory/I/O virtualization, VM migration, and the link between virtualization and cloud computing. [file:3]

## Learning outcomes to remember
- Describe fundamental principles and paradigms of cloud computing. [file:3]
- Demonstrate a comprehensive understanding of virtualization and container technologies. [file:3]

## Virtualization: core definition
Virtualization is the creation of a virtual version of something, such as hardware, a software environment, storage, or a network. [file:3]

### Hardware virtualization
Hardware virtualization, often used synonymously with system virtualization, hides the physical characteristics of computing resources and allows multiple virtual machines to run on one physical machine, with each VM running its own operating system instance. [file:3]

### Fast exam phrasing
Virtualization abstracts physical resources so multiple isolated virtual environments can share the same underlying hardware. [file:3]

## History of virtualization
The slides mention IBM VM/370 as a VMM for IBM mainframes in the 1960s, where virtualization was useful because hardware was expensive and machines were few. [file:3]

It was a popular research topic in the 1960s and 1970s, then interest declined in the 1980s and 1990s because hardware became cheaper and operating systems became more powerful. [file:3]

## Why virtualization matters
Motivations for virtualization:
- It is highly relevant to cloud computing and multi-tenancy. [file:3]
- It supports storage, computation, and network as a service. [file:3]
- It allows VMs to be created and destroyed quickly with little overhead. [file:3]
- It helps handle dynamic demand, such as multiplayer online games. [file:3]
- It supports suitable resource-allocation policies to meet QoS requirements. [file:3]
- It allows several OS environments on one desktop machine. [file:3]
- It enables VM migration. [file:3]
- It can reduce server investment and energy consumption. [file:3]

### Good short-answer justification
Virtualization matters because it improves resource sharing, elasticity, consolidation, multi-tenancy, and operational efficiency in cloud environments. [file:3]

## Key virtualization features
Memorize these 4:
- **Isolation**: fault, performance, and software isolation between VMs. [file:3]
- **Encapsulation**: capture VM state cleanly, enabling snapshots, cloning, and copying. [file:3]
- **Portability**: independence from specific hardware, enabling live and cold migration. [file:3]
- **Interposition**: transformations on instructions, memory, and I/O, enabling overcommitment, encryption, compression, and replication. [file:3]

### Easy memory trick
Think: separate VMs, package their state, move them around, and intercept/control resource use. [file:3]

## Hypervisor and VM basics
A **hypervisor** or **virtual machine monitor (VMM)** is the thin layer of software on top of physical hardware that implements hardware virtualization. [file:3]

A **virtual machine** is a representation of a real machine that can host a guest operating system, a **guest OS** runs inside the VM, and the **host** is the original environment in which the guest OS is managed. [file:3]

### VMM implementation goals
The VMM should: [file:3]
- Efficiently virtualize hardware. [file:3]
- Provide the illusion of multiple machines. [file:3]
- Retain control of the physical machine. [file:3]

Subsystems to virtualize:
- Processor. [file:3]
- Memory. [file:3]
- I/O devices. [file:3]

## Processor virtualization
Processor virtualization makes the processor behave as if it were multiple individual CPUs. [file:3]

Since multiple VMs may compete for CPU resources, the VMM must multiplex VMs across CPUs. [file:3]

## ISA, ABI, API
The reference model in the slides includes: [file:3]
- **ISA**: Instruction Set Architecture. [file:3]
- **ABI**: Application Binary Interface. [file:3]
- **API**: Application Programming Interface. [file:3]

For operations at the application level, ABI and ISA help make them happen underneath the API. [file:3]

## Privileged vs nonprivileged instructions
Nonprivileged instructions run in **user mode** and do not interfere with shared resources, such as arithmetic instructions or reading processor status. [file:3]

Privileged instructions run in **kernel mode** and are used for sensitive operations, such as I/O instructions, halting, disabling interrupts, setting timers, context switching, clearing memory, removing a process from memory, or modifying device-status tables. [file:3]

These privileged instructions trap when attempted from user mode, but not in kernel mode. [file:3]

## Privilege modes
Modern systems support at least two execution modes: **supervisor mode** and **user mode**. [file:3]

Hypervisors run in supervisor mode, and if code in user mode invokes privileged instructions, hardware interrupts trap the dangerous execution. [file:3]

## Sensitive instructions and x86 virtualization issue
Sensitive instructions are instructions the VMM wants to trap and emulate so an unmodified OS believes it owns the hardware. [file:3]

A VMM can be constructed if sensitive instructions are a subset of privileged instructions, but classical x86 was not classically virtualizable because it had sensitive instructions that were not privileged. [file:3]

The slides state x86 had 17 instructions that were sensitive but not privileged, including LAR and LSL, and VMware addressed this in 1998 with a layer of emulation for all instructions, known as **full virtualization**. [file:3]

### Exam-ready line
Classical virtualization is cleanest when all sensitive instructions trap, but x86 broke that condition, so VMware used emulation and translation techniques. [file:3]

## Virtualization types
### Full virtualization
- The guest OS is unaware it is virtualized. [file:3]
- The hypervisor presents virtual hardware that mimics physical hardware. [file:3]
- It supports unmodified guest OSs. [file:3]
- It may have higher overhead because of hardware emulation. [file:3]
- Examples: VMware and VirtualBox. [file:3]

### Paravirtualization
- The guest OS is aware it is virtualized. [file:3]
- It interacts with the hypervisor through special paravirtualized drivers. [file:3]
- It avoids full hardware emulation and can improve performance. [file:3]
- It requires guest-OS modification. [file:3]
- Example: Xen. [file:3]

### Full vs para
| Topic | Full virtualization | Paravirtualization |
|---|---|---|
| Guest OS awareness | Guest OS is unaware. [file:3] | Guest OS is aware. [file:3] |
| OS modification | Not required. [file:3] | Required. [file:3] |
| Compatibility | Broad compatibility with unmodified OSs. [file:3] | Less compatible because OS must support it. [file:3] |
| Performance overhead | Can be higher due to emulation. [file:3] | Lower overhead than full virtualization. [file:3] |
| Example | VMware, VirtualBox. [file:3] | Xen. [file:3] |

## Hypervisor types
### Type 1 / bare metal
- Runs directly on hardware. [file:3]
- Higher performance. [file:3]
- Examples: ESX, Xen, Hyper-V. [file:3]

### Type 2 / hosted
- Runs on top of a host OS. [file:3]
- Easier to install. [file:3]
- Leverages host device drivers. [file:3]
- Examples: VMware Workstation, VirtualBox. [file:3]

### Type 1 vs Type 2
| Topic | Type 1 | Type 2 |
|---|---|---|
| Position | Directly on bare metal hardware. [file:3] | On top of a host OS. [file:3] |
| Performance | Higher. [file:3] | Usually lower than Type 1. [file:3] |
| Ease of setup | Less simple for casual users. [file:3] | Easier to install. [file:3] |
| Driver use | Hypervisor-oriented. [file:3] | Uses host OS device drivers. [file:3] |

## Memory virtualization
The slides describe three abstractions of memory: [file:3]
- **Machine memory**: the actual hardware memory, such as 2 GB of DRAM. [file:3]
- **Physical memory**: an OS-managed abstraction of hardware memory. [file:3]
- **Virtual (logical) memory**: the virtual address space. [file:3]

A guest OS assumes it controls memory management and mapping, but the VMM actually partitions memory among VMs and must control mapping for isolation. [file:3]

The VMM must assign hardware pages to VMs and cannot allow the guest OS to map any logical page directly to any machine page. [file:3]

### Why memory virtualization is hard
The slides point to hardware-managed TLBs as a difficulty, since x86 memory management uses a TLB to map virtual page addresses to physical page addresses. [file:3]

## I/O virtualization
Writing device drivers for all I/O devices directly in the VMM is not feasible because there are too many devices. [file:3]

The solution described is to present virtual I/O devices to guest VMs and channel I/O requests to a trusted host VM. [file:3]

I/O remains complicated because operating systems use many short fast paths for I/O, so it is often better if the hypervisor does less work for guest I/O. [file:3]

Possible techniques include: [file:3]
- Direct device access. [file:3]
- DMA pass-through. [file:3]
- Direct interrupt delivery, with hardware support. [file:3]

### Network access in virtualized environments
For networking, the VMM and all guests need network access. [file:3]

The VMM can bridge guests directly to the network or use NAT, where the guest has a local address and the VMM performs address translation. [file:3]

## Other kinds of virtualization
The lecture also lists: [file:3]
- Programming language-level virtualization. [file:3]
- Application-level virtualization. [file:3]
- Storage virtualization. [file:3]
- Network virtualization. [file:3]
- Desktop virtualization. [file:3]
- Application server virtualization. [file:3]

## Programming language-level virtualization
This is used mainly for portability and easier deployment across platforms and OSs. [file:3]

Programs are compiled to bytecode, then at runtime the bytecode is interpreted or compiled on the fly against the hardware instruction set. [file:3]

The key example is the **Java Virtual Machine (JVM)**. [file:3]

## Application-level virtualization
This allows applications to run in environments that do not natively support all required features, such as Windows applications on Linux. [file:3]

Two main techniques in the slides:
- **Interpretation**: minimal startup cost but high runtime overhead, because every instruction is emulated. [file:3]
- **Binary translation**: higher initial cost, but better later performance because translated blocks are cached and reused. [file:3]

A named example is **Wine**. [file:3]

## Virtualization and cloud computing
The lecture links virtualization to cloud computing through customization, security, isolation, and manageability. [file:3]

Virtualization supports **consolidation**, because multiple isolated VMs can share the same resources without interfering with one another, reducing the number of active resources. [file:3]

This enables aggregation of VMs on fewer physical resources and strengthens resource efficiency in cloud systems. [file:3]

## VM migration
Two major migration types:
- **Cold migration**: migrating a turned-off or suspended VM. [file:3]
- **Live migration**: moving a running VM from one physical host to another without interrupting user access or applications. [file:3]

### Why live migration is useful
Uses mentioned in the slides:
- Hardware maintenance. [file:3]
- Load balancing and consolidation. [file:3]
- Energy saving. [file:3]
- Disaster recovery. [file:3]

### Live migration steps
1. Source VMM connects to target VMM. [file:3]
2. Target VMM creates a new guest. [file:3]
3. Source sends read-only guest memory pages. [file:3]
4. Source sends read/write pages and marks them clean. [file:3]
5. Source repeats transfer because some pages become dirty again. [file:3]
6. When the cycle becomes short, the source freezes the guest, sends final CPU and state details plus final dirty pages, and tells the target to start the guest. [file:3]
7. Target acknowledges the guest is running and the source terminates the old guest. [file:3]

### Live migration styles
- **Pre-copy**: iteratively migrates dirty pages to minimize downtime. [file:3]
- **Post-copy**: moves minimal execution state first, then transfers pages during resumed execution. [file:3]
- **Hybrid-copy**: combines pre-copy and post-copy to balance downtime and data integrity concerns. [file:3]

## Pros and cons of virtualization
### Advantages
- Isolation. [file:3]
- Encapsulation. [file:3]
- Portability. [file:3]
- Interposition. [file:3]

### Disadvantages
- Performance degradation. [file:3]
- Inefficiency and degraded user experience. [file:3]
- Security holes and new threats. [file:3]

## Technology examples
### Xen
Xen is an open-source virtualization platform based on paravirtualization, and parts of the guest OS must be modified. [file:3]

It originated at the University of Cambridge and is now under the Linux Foundation, with support from organizations including Intel, Citrix, Arm, Huawei, AWS, Alibaba Cloud, AMD, Bitdefender, and EPAM. [file:3]

The Xen VMM can support up to several hundred VMs on a single machine and supports IA-32, x86-64, and ARM instruction sets. [file:3]

### Xen architecture
- The hypervisor runs at the highest privilege level. [file:3]
- Control-plane software runs in **Domain 0**. [file:3]
- Privileged instructions are rewritten as **hypercalls** that trap into the hypervisor. [file:3]

### Xen scheduling
The slides mention the concept of **virtual CPU (VCPU)** and two schedulers: [file:3]
- Xen’s Simple Earliest Deadline First (SEDF) scheduler. [file:3]
- Xen’s Credit scheduler. [file:3]

### Xen device management
Xen uses **split device drivers**. [file:3]

A back-end driver runs in Domain 0, while a front-end driver runs in the guest OS, and communication can use a shared-memory **I/O ring**. [file:3]

## VMware
VMware is known for virtualizing x86 architectures while allowing unmodified guest OSs to run on top of its hypervisors. [file:3]

Before hardware-assisted virtualization became available in 2006 through Intel VT-x and AMD-V, VMware used dynamic binary translation. [file:3]

### VMware desktop virtualization
Examples include VMware Workstation for Windows and VMware Fusion for macOS. [file:3]

The hosted VM architecture uses the memory space of a single application and supports creating new images, pausing execution, taking snapshots, and rolling back to earlier VM states. [file:3]

### VMware server virtualization
VMware ESX and ESXi can be installed on bare-metal servers. [file:3]

Remote management uses the CIM Broker and local management uses the Direct Client User Interface (DCUI), described as BIOS-like. [file:3]

### VMware cloud solutions
The slides list: [file:3]
- **vSphere** for managing a pool of virtualized servers. [file:3]
- **vCenter** for centralized administration of vSphere. [file:3]
- **vCloud** for on-demand virtual computing environments. [file:3]
- **vFabric** for scalable web-app development on virtualized infrastructure. [file:3]
- **Zimbra** for office automation, messaging, and collaboration. [file:3]

## Fast memory table
| Topic | What to remember |
|---|---|
| Virtualization | Creating a virtual version of hardware, software environment, storage, or network. [file:3] |
| Hardware virtualization | Multiple VMs on one physical machine, each with its own OS. [file:3] |
| 4 key features | Isolation, encapsulation, portability, interposition. [file:3] |
| Core controller | Hypervisor / VMM. [file:3] |
| VMM goals | Efficiency, illusion of multiple machines, control of hardware. [file:3] |
| 2 main virtualization styles | Full virtualization and paravirtualization. [file:3] |
| 2 hypervisor types | Type 1 bare metal and Type 2 hosted. [file:3] |
| 3 memory abstractions | Machine, physical, virtual memory. [file:3] |
| Migration types | Cold and live migration. [file:3] |
| Key examples | Xen = para, VMware = full. [file:3] |

## What is most likely to appear in short answers
### 1) Explain why virtualization is important for cloud computing
Possible points:
- Supports multi-tenancy. [file:3]
- Enables resource sharing and consolidation. [file:3]
- Allows rapid VM provisioning and destruction. [file:3]
- Improves manageability, isolation, and elasticity. [file:3]
- Supports migration, maintenance, and load balancing. [file:3]

### 2) Justify full virtualization vs paravirtualization
- Choose **full virtualization** when compatibility with unmodified guest OSs matters. [file:3]
- Choose **paravirtualization** when lower overhead and better performance matter and guest modification is acceptable. [file:3]

### 3) Justify Type 1 vs Type 2 hypervisors
- Choose **Type 1** for higher performance and server/cloud environments. [file:3]
- Choose **Type 2** when easier setup and host-driver reuse are more important, such as local desktop testing. [file:3]

### 4) Explain why migration is useful
- It supports maintenance without downtime, load balancing, consolidation, energy saving, and disaster recovery. [file:3]

## Sample multiple-choice questions
### Set 1
1. Virtualization refers to:  
A. Only splitting hard disks  
B. Creating a virtual version of resources such as hardware, storage, network, or software environments  
C. Only running Linux  
D. Only compressing data  
**Answer: B** [file:3]

2. Hardware virtualization allows:  
A. One OS only per machine forever  
B. Multiple VMs on a physical machine  
C. No abstraction of hardware  
D. Only network virtualization  
**Answer: B** [file:3]

3. IBM VM/370 is mentioned as:  
A. A database engine  
B. A VMM for IBM mainframes  
C. A cloud-native container  
D. A firewall  
**Answer: B** [file:3]

4. Which is a motivation for virtualization?  
A. Preventing all QoS planning  
B. Supporting multi-tenancy for cloud computing  
C. Eliminating migration  
D. Removing isolation  
**Answer: B** [file:3]

5. Which is a virtualization feature?  
A. Fragmentation  
B. Isolation  
C. Serialization  
D. Defragmentation  
**Answer: B** [file:3]

6. Capturing all VM state cleanly is called:  
A. Interposition  
B. Encapsulation  
C. Translation  
D. Segmentation  
**Answer: B** [file:3]

7. Independence from physical hardware that enables migration is:  
A. Portability  
B. Availability  
C. Authorization  
D. Consolidation  
**Answer: A** [file:3]

8. Which feature enables transformations on instructions, memory, and I/O?  
A. Interposition  
B. Encapsulation  
C. Fault isolation  
D. NAT  
**Answer: A** [file:3]

9. A hypervisor is also called a:  
A. Device mapper  
B. Virtual machine monitor  
C. Packet inspector  
D. Storage array  
**Answer: B** [file:3]

10. A guest operating system is:  
A. The host firmware  
B. An OS running inside a VM  
C. The hypervisor itself  
D. A physical processor  
**Answer: B** [file:3]

11. Which is one VMM implementation goal?  
A. Remove control from hardware  
B. Provide illusion of multiple machines  
C. Prevent VM execution  
D. Eliminate memory management  
**Answer: B** [file:3]

12. Which subsystem is listed for virtualization?  
A. Processor  
B. Campus Wi-Fi only  
C. Keyboard layout  
D. Browser tabs  
**Answer: A** [file:3]

13. Processor virtualization requires the VMM to:  
A. Destroy all CPUs  
B. Multiplex VMs on CPUs  
C. Disable user mode  
D. Remove scheduling  
**Answer: B** [file:3]

14. Which stands for Instruction Set Architecture?  
A. API  
B. ABI  
C. ISA  
D. I/O  
**Answer: C** [file:3]

15. Which stands for Application Binary Interface?  
A. ABI  
B. API  
C. ISA  
D. TLB  
**Answer: A** [file:3]

16. Arithmetic instructions are an example of:  
A. Privileged instructions  
B. Nonprivileged instructions  
C. Hypercalls  
D. Dirty pages  
**Answer: B** [file:3]

17. I/O instructions are an example of:  
A. Nonprivileged instructions  
B. Privileged instructions  
C. User-mode only instructions  
D. Network-only instructions  
**Answer: B** [file:3]

18. Hypervisors run in:  
A. User mode  
B. Supervisor mode  
C. Compatibility mode only  
D. Sleep mode  
**Answer: B** [file:3]

19. Classical x86 was difficult to virtualize because:  
A. It had no memory  
B. It had sensitive instructions that were not privileged  
C. It had no user mode  
D. It lacked any ISA  
**Answer: B** [file:3]

20. VMware addressed x86 virtualization using:  
A. A firewall layer only  
B. A layer of emulation for all instructions  
C. Manual scheduling  
D. No hypervisor  
**Answer: B** [file:3]

### Set 2
21. In full virtualization, the guest OS is:  
A. Aware of virtualization  
B. Unaware of virtualization  
C. Replaced by the hypervisor  
D. Always modified  
**Answer: B** [file:3]

22. Full virtualization is attractive because it supports:  
A. Only modified guest OSs  
B. Unmodified guest OSs  
C. No guest OSs  
D. Only Windows apps on Linux  
**Answer: B** [file:3]

23. Paravirtualization requires:  
A. No changes to the guest OS  
B. Modifications to the guest OS  
C. No hypervisor  
D. Bare-metal only CPUs  
**Answer: B** [file:3]

24. Which is an example of paravirtualization?  
A. Xen  
B. VirtualBox  
C. VMware Workstation  
D. JVM  
**Answer: A** [file:3]

25. Which is an example of full virtualization?  
A. Xen only  
B. VMware  
C. Domain 0  
D. SEDF  
**Answer: B** [file:3]

26. A Type 1 hypervisor is also called:  
A. Hosted  
B. Bare metal  
C. Bytecode-based  
D. Application-level  
**Answer: B** [file:3]

27. Which is an example of Type 2 virtualization?  
A. ESX  
B. Xen  
C. VMware Workstation  
D. Hyper-V Server Core only  
**Answer: C** [file:3]

28. Type 2 hypervisors are generally:  
A. Harder to install  
B. Easier to install  
C. Always faster than Type 1  
D. Not dependent on host drivers  
**Answer: B** [file:3]

29. Which is one memory abstraction?  
A. Social memory  
B. Machine memory  
C. Browser memory only  
D. Human memory  
**Answer: B** [file:3]

30. Which hardware component makes memory virtualization harder according to the lecture?  
A. SSD cache  
B. TLB  
C. USB bus  
D. GPU fan  
**Answer: B** [file:3]

31. Presenting virtual I/O devices to guest VMs is used because:  
A. VMMs can easily write every possible device driver  
B. Writing drivers for all devices in the VMM is not feasible  
C. Guests should never perform I/O  
D. Device drivers are unnecessary  
**Answer: B** [file:3]

32. NAT in VM networking means the guest:  
A. Has direct public hardware control  
B. Uses a local address and the VMM performs translation  
C. Cannot access the network  
D. Becomes the hypervisor  
**Answer: B** [file:3]

33. Which is an example of programming language-level virtualization?  
A. Xen  
B. JVM  
C. ESXi  
D. VCPU scheduler  
**Answer: B** [file:3]

34. Which is an example of application-level virtualization?  
A. Wine  
B. TLB  
C. Domain 0  
D. Hyper-V  
**Answer: A** [file:3]

35. Interpretation in application-level virtualization has:  
A. Minimal startup cost but high runtime overhead  
B. No overhead at all  
C. Better long-term performance than binary translation in all cases  
D. No emulation  
**Answer: A** [file:3]

36. Binary translation has:  
A. No initial cost  
B. High initial cost but improved later performance due to cached translated blocks  
C. Lower performance than interpretation forever  
D. No translation of instructions  
**Answer: B** [file:3]

37. Consolidation means:  
A. Increasing active servers regardless of need  
B. Aggregating VMs on fewer physical resources  
C. Preventing multi-tenancy  
D. Deleting snapshots  
**Answer: B** [file:3]

38. Cold migration is the migration of:  
A. A running VM without interruption  
B. A turned-off or suspended VM  
C. Only containers  
D. Only storage devices  
**Answer: B** [file:3]

39. Live migration means:  
A. Migrating a running VM without interrupting user access  
B. Shutting down the VM before every move  
C. Copying only source code  
D. Reinstalling the OS on another host  
**Answer: A** [file:3]

40. Which is a use of live migration?  
A. Hardware maintenance  
B. Removing portability  
C. Eliminating scheduling  
D. Disabling disaster recovery  
**Answer: A** [file:3]

41. Which live migration style iteratively transfers dirty pages?  
A. Post-copy  
B. Pre-copy  
C. Hybrid-copy only after shutdown  
D. NAT-copy  
**Answer: B** [file:3]

42. Which live migration style resumes execution earlier and transfers pages afterward?  
A. Pre-copy  
B. Post-copy  
C. Cold-copy  
D. Bare-metal copy  
**Answer: B** [file:3]

43. Which of the following is listed as a disadvantage of virtualization?  
A. Portability  
B. Encapsulation  
C. Performance degradation  
D. Isolation  
**Answer: C** [file:3]

44. Xen is based on:  
A. Full virtualization only  
B. Paravirtualization  
C. Application-level virtualization only  
D. No hypervisor  
**Answer: B** [file:3]

45. In Xen, privileged instructions are rewritten as:  
A. API calls  
B. Hypercalls  
C. User interrupts  
D. NAT rules  
**Answer: B** [file:3]

46. Domain 0 in Xen is associated with:  
A. Control-plane software  
B. User-mode arithmetic only  
C. Physical DRAM chips  
D. API bytecode  
**Answer: A** [file:3]

47. Which scheduler is listed for Xen?  
A. Round robin only  
B. Credit scheduler  
C. CFS only  
D. Lottery scheduler only  
**Answer: B** [file:3]

48. Xen device management uses:  
A. Split device drivers  
B. One single universal driver in each guest only  
C. No drivers  
D. Only BIOS calls  
**Answer: A** [file:3]

49. Before Intel VT-x and AMD-V, VMware used:  
A. Hypercalls only  
B. Dynamic binary translation  
C. JVM bytecode  
D. NAT-only execution  
**Answer: B** [file:3]

50. ESX and ESXi are examples of:  
A. VMware server virtualization on bare metal  
B. Application-level virtualization tools  
C. Programming language-level VMs  
D. NAT devices  
**Answer: A** [file:3]

## Sample short-answer questions with model points
### SAQ 1
**Question:** Define virtualization and hardware virtualization.  
**Model points:** Virtualization is the creation of a virtual version of resources such as hardware, software environments, storage, or networks. Hardware virtualization hides physical computing resources and allows multiple VMs to run on one physical machine, each with its own OS. [file:3]

### SAQ 2
**Question:** Why is virtualization important in cloud computing?  
**Model points:** It supports multi-tenancy, allows rapid VM creation and destruction, improves resource allocation, enables consolidation, reduces hardware investment and energy use, and supports migration and QoS management. [file:3]

### SAQ 3
**Question:** Explain the four main features of virtualization.  
**Model points:** Isolation separates faults and performance effects; encapsulation captures VM state for snapshots and cloning; portability allows migration across hardware; interposition lets the system intercept and transform operations on instructions, memory, and I/O. [file:3]

### SAQ 4
**Question:** What is the role of a hypervisor?  
**Model points:** A hypervisor or VMM is the software layer that virtualizes hardware, provides the illusion of multiple machines, and retains control of the physical resources while supporting guest OSs. [file:3]

### SAQ 5
**Question:** Distinguish host, guest OS, and VM.  
**Model points:** The VM is the virtualized machine representation, the guest OS runs inside the VM, and the host is the original environment in which the virtualization is managed. [file:3]

### SAQ 6
**Question:** Explain privileged and nonprivileged instructions.  
**Model points:** Nonprivileged instructions run in user mode and avoid unsafe access to shared resources, while privileged instructions run in kernel mode for sensitive operations and trap if attempted from user mode. [file:3]

### SAQ 7
**Question:** Why was x86 difficult to virtualize classically?  
**Model points:** Because some sensitive x86 instructions were not privileged, they did not always trap, which broke the classical condition needed for straightforward trap-and-emulate virtualization. [file:3]

### SAQ 8
**Question:** Compare full virtualization and paravirtualization.  
**Model points:** Full virtualization supports unmodified guest OSs that are unaware of virtualization but may incur more overhead; paravirtualization requires guest modification and awareness but reduces emulation overhead and improves performance. [file:3]

### SAQ 9
**Question:** Compare Type 1 and Type 2 hypervisors.  
**Model points:** Type 1 runs directly on hardware and gives higher performance, while Type 2 runs on top of a host OS, is easier to install, and can use host device drivers. [file:3]

### SAQ 10
**Question:** Why is memory virtualization difficult?  
**Model points:** A guest OS assumes full control over memory, but the VMM must partition machine memory among VMs and enforce isolation, while hardware features like the TLB complicate address translation management. [file:3]

### SAQ 11
**Question:** Explain the main challenge in I/O virtualization.  
**Model points:** There are too many I/O devices to implement all their drivers inside the VMM, so systems often present virtual I/O devices to guests and forward requests to trusted host components. [file:3]

### SAQ 12
**Question:** Compare interpretation and binary translation in application-level virtualization.  
**Model points:** Interpretation has low startup cost but high runtime overhead because each instruction is emulated, while binary translation has higher initial overhead but better later performance because translated blocks are reused. [file:3]

### SAQ 13
**Question:** What is live migration, and why is it useful?  
**Model points:** Live migration moves a running VM between physical hosts without interrupting user access, helping with maintenance, load balancing, consolidation, energy saving, and disaster recovery. [file:3]

### SAQ 14
**Question:** Distinguish cold migration and live migration.  
**Model points:** Cold migration moves a turned-off or suspended VM, while live migration moves a running VM with minimal interruption to users and applications. [file:3]

### SAQ 15
**Question:** What are pre-copy, post-copy, and hybrid-copy migration?  
**Model points:** Pre-copy repeatedly sends dirty pages before switchover, post-copy resumes execution earlier and transfers pages afterward, and hybrid-copy combines both approaches to balance downtime and integrity. [file:3]

### SAQ 16
**Question:** Explain Xen in brief.  
**Model points:** Xen is an open-source paravirtualization platform in which parts of the guest OS are modified, the hypervisor runs at the highest privilege level, Domain 0 handles control functions, and privileged operations are converted into hypercalls. [file:3]

### SAQ 17
**Question:** Explain VMware in brief.  
**Model points:** VMware is known for full virtualization of x86 systems with unmodified guest OSs; it used dynamic binary translation before hardware-assisted virtualization, and products include desktop tools like Workstation and server tools like ESX/ESXi. [file:3]

## Likely exam traps
- Do not confuse **full virtualization** with **paravirtualization**. [file:3]
- Do not confuse **Type 1 / Type 2** with **full / para**; they are different classifications. [file:3]
- Do not forget that **x86 was not classically virtualizable** because of sensitive nonprivileged instructions. [file:3]
- Do not mix up **cold migration** and **live migration**. [file:3]
- Do not say virtualization only means VMs; the lecture also covers application-level and language-level virtualization. [file:3]

## 15-minute revision plan
1. Memorize definitions: virtualization, hardware virtualization, hypervisor, guest OS, host. [file:3]
2. Memorize the 4 features: isolation, encapsulation, portability, interposition. [file:3]
3. Understand full vs para and Type 1 vs Type 2. [file:3]
4. Review memory, CPU, and I/O virtualization challenges. [file:3]
5. Memorize migration types and Xen vs VMware differences. [file:3]

## Ultra-short cram sheet
- Virtualization = creating a virtual version of resources. [file:3]
- Hardware virtualization = multiple VMs on one physical machine. [file:3]
- Hypervisor/VMM = software layer controlling virtualization. [file:3]
- 4 features = isolation, encapsulation, portability, interposition. [file:3]
- Full virtualization = unmodified guest OS; para = modified aware guest OS. [file:3]
- Type 1 = bare metal; Type 2 = hosted. [file:3]
- Memory challenge = guest thinks it owns memory, but VMM must isolate and control mappings. [file:3]
- I/O challenge = too many device drivers, so virtual devices and forwarding are used. [file:3]
- Migration = cold or live; live helps maintenance and balancing. [file:3]
- Xen = para; VMware = full. [file:3]

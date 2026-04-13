# FIT5225 Week 5 Cheat Sheet

Based on the attached Week 5 lecture slides: *5-Web-Services-and-Service-Oriented-Architecture.pdf* [file:9]

## What this week is about
Week 5 focuses on web services, data representation formats such as XML and JSON, communication and service referencing basics, SOAP and REST web services, and service-oriented architecture (SOA), with a short link to microservices. [file:9]

## Learning outcomes to remember
- Describe fundamental principles and paradigms of cloud computing. [file:9]
- Identify appropriate design choices when developing real-world cloud computing applications. [file:9]
- Apply different cloud programming methods and tools. [file:9]

## Lecture agenda to memorize
The lecture covers: [file:9]
- Introduction to web services. [file:9]
- Overview of different data representation schemes. [file:9]
- XML and JSON. [file:9]
- Travel agent use case scenario. [file:9]
- SOAP-based web services. [file:9]
- RESTful web services. [file:9]
- Service-oriented architecture. [file:9]

## What a web service is
A web service provides an interface that lets clients interact with remote servers in a general way. [file:9]

Web service interactions happen through request and reply messages, usually transmitted over HTTP, with data represented and marshalled using XML or JSON. [file:9]

The lecture also says web services support richer interoperability, secure CRUD over the Internet, cross-organization program-to-program interaction without human supervision, and they enable SOA. [file:9]

### Fast exam phrasing
A web service is a network-accessible software interface that allows client-server interaction through message exchange, often over HTTP using XML or JSON. [file:9]

## History and implementations
The lecture mentions BizTalk in 1999 and the broader goal of enabling software in different places, languages, and platforms to interoperate. [file:9]

It identifies three implementation styles: **SOAP-based web services**, **REST**, and **Web APIs**. [file:9]

## External data representation
Programs store data internally in different machine-specific formats, such as different integer sizes, floating-point formats, or character encodings like ASCII and Unicode. [file:9]

To communicate across different systems, data can be converted to an agreed external format before transmission or sent in sender format along with format information. [file:9]

### Key terms
- **External data representation**: an agreed standard for representing data structures and primitive data. [file:9]
- **Marshalling**: converting data into a form suitable for transmission. [file:9]
- **Unmarshalling**: disassembling the transmitted data at the receiver. [file:9]

## XML
XML is a markup language defined by the W3C. [file:9]

The lecture says XML is extensible, uses tags that describe logical data structure, is self-describing, can use namespaces for meaning, is human-readable and platform independent, but produces large textual messages that increase processing, transmission time, and storage needs. [file:9]

### XML elements and attributes
- An **element** is data surrounded by tags, such as `<name>Smith</name>`. [file:9]
- Elements can be nested, which supports hierarchical representation. [file:9]
- Empty tags can end with `/>`. [file:9]
- **Attributes** are optional name-value pairs in a start tag, such as `id="12345678"`. [file:9]

### XML namespaces and schemas
- An **XML namespace** names a collection of element types and attributes and is referenced by a URL. [file:9]
- The namespace can be specified using the `xmlns` attribute. [file:9]
- An **XML Schema** defines which elements and attributes can appear in a document. [file:9]

## JSON
JSON is a lightweight data-interchange format and a syntax for storing and exchanging data. [file:9]

The lecture describes JSON as an easier-to-use alternative to XML, based on a subset of JavaScript, text-based, and language independent. [file:9]

## JSON vs XML
This comparison is very likely to appear. [file:9]

| Topic | JSON | XML |
|---|---|---|
| Simplicity | Lightweight and simple to read and write. [file:9] | Less simple than JSON. [file:9] |
| Arrays | Supports array data structures. [file:9] | Does not support arrays directly. [file:9] |
| Human readability | More human readable. [file:9] | Less human readable. [file:9] |
| Display capability | No display capabilities. [file:9] | Can display data because it is a markup language. [file:9] |
| Types | Provides scalar data types and structured data via arrays and objects. [file:9] | No built-in notion of data types; relies on XML Schema for type information. [file:9] |
| Object support | Has native object support. [file:9] | Objects must be expressed by conventions using attributes and elements. [file:9] |

### Short-answer line
JSON is generally lighter and easier to use, while XML is more verbose but supports rich markup structure and schema-based description. [file:9]

## Communication patterns
Processes communicate with **send** and **receive** message functions, with a queue associated with each destination. [file:9]

Communication may be: [file:9]
- **Synchronous**: send and receive are blocking. [file:9]
- **Asynchronous**: send is non-blocking and transmission proceeds in parallel. [file:9]

### Exam-ready distinction
Synchronous communication blocks the sender and receiver, while asynchronous communication allows the sender to continue after placing the message into a local buffer. [file:9]

## Message transmission and ports
Messages are sent to an **(Internet address, local port)** pair. [file:9]

A port usually has exactly one receiver, though it can have multiple senders, and the lecture notes recent changes allowing multiple processes to listen to the same port for performance reasons. [file:9]

## Referencing services
A **URI** identifies a resource. [file:9]

A **URL** is a subset of URI that includes a network location, while a **URN** is a subset of URI that gives a name in a namespace without location. [file:9]

The lecture states that a web service endpoint is a **web address (URL)**. [file:9]

### Quick distinction
- URI = general identifier. [file:9]
- URL = identifier with location. [file:9]
- URN = identifier by name without location. [file:9]

## Combining web services
A web service interface usually contains a collection of operations that a client can use over the Internet. [file:9]

Providing an interface makes it possible to combine operations from multiple services to create new functionality. [file:9]

## Travel agent scenario
The travel-agent example is important because it shows service composition. [file:9]

The client asks a travel agent service for flights, car hire, and hotel options; the travel agent collects prices and availability; the client may refine the query, make reservations, or quit; if reservations are available, deposits are taken and a reservation number is returned; later modifications or cancellations may also occur. [file:9]

The service breakdown shows the travel agent combining flight booking, car booking, and hotel booking services. [file:9]

## Mashup requirements and challenges
The lecture lists these requirements and challenges for web-service mashups and choreographies: [file:9]
- Hierarchical and recursive composition. [file:9]
- Adding new instances of existing services and new services. [file:9]
- Concurrent and alternative paths and repetition. [file:9]
- Variable timeouts. [file:9]
- Exception handling. [file:9]
- Asynchronous interactions and callbacks. [file:9]
- Reference passing. [file:9]
- Human-readable documentation. [file:9]

## SOAP-based web services
SOAP stands for **Simple Object Access Protocol**. [file:9]

The lecture says SOAP is an XML-based protocol for exchanging information between applications over a protocol such as HTTP, it was popular in the early 2000s, is language independent, may be synchronous or asynchronous, and is based on packaging single one-way messages. [file:9]

Originally SOAP was based on HTTP, but the current version may also use SMTP, TCP, UDP, or HTTP. [file:9]

SOAP-based services also use: [file:9]
- **WSDL** as an interface definition language. [file:9]
- **UDDI** as a registry for lookup. [file:9]

## SOAP message format
A SOAP message is carried inside an **envelope**. [file:9]

Inside the envelope there may be an optional **header** and a **body**. [file:9]

Headers can establish context or keep logs and audits, while the body carries the XML document for the web service. [file:9]

The lecture also says the body encloses the procedure name, namespace URI, and any arguments, while faults are returned in a **fault element** in the response body when a request fails. [file:9]

### SOAP structure to memorize
Envelope -> optional header -> body -> procedure name + namespace + arguments / results / fault. [file:9]

## Service description with WSDL
A service description is the basis of agreement between a client and a server about the offered service. [file:9]

The primary way to describe a web service is **WSDL**. [file:9]

The lecture says WSDL describes operations, may use XML Schema for input and output parameters, contains how and where the service may be accessed, and can be used by tools to auto-generate client proxy code or server skeletons. [file:9]

### Key WSDL ideas
- WSDL is an **IDL** for web services. [file:9]
- It includes abstract and concrete parts. [file:9]
- It describes operations, bindings, services, and access details. [file:9]

## Main WSDL elements
The slides list the main description elements as: [file:9]
- Definitions. [file:9]
- Types. [file:9]
- Message. [file:9]
- Interface. [file:9]
- Bindings. [file:9]
- Services. [file:9]

The lecture also notes that a **binding** chooses the protocol and a **service** gives the endpoint address. [file:9]

## UDDI
UDDI stands for **Universal Description, Discovery and Integration**. [file:9]

The lecture says it provides both a name service and a directory service, allowing WSDL descriptions to be looked up by name or attribute. [file:9]

It supports `get_xxx` operations for retrieving by key and `find_xxx` operations for searching by criteria. [file:9]

## XML security requirements
The lecture notes that XML security may need support for encrypting all or part of a document, signing all or part of a document, adding to already signed or encrypted documents, and authorizing different users to view different sections. [file:9]

## REST
REST stands for **Representational State Transfer** and originates from Roy Fielding’s 2000 PhD dissertation. [file:9]

The lecture describes REST as an approach with a very constrained operational style where clients use URLs and HTTP methods such as GET, PUT, DELETE, and POST to manipulate resources. [file:9]

RESTful web services allow systems to access and manipulate representations of web resources using a uniform, predefined, and stateless set of operations. [file:9]

The lecture also stresses that REST is a **set of design criteria**, not the physical architecture itself. [file:9]

## REST principles
REST architecture principles from the lecture: [file:9]
- The **resource** is the highest abstraction and each resource should have a URI. [file:9]
- Use a constrained and uniform set of methods such as GET, PUT, DELETE, and POST. [file:9]
- Client and server exchange resource representations. [file:9]
- PUT and POST send representations to the server; GET retrieves them. [file:9]
- The application may have state, but the server stores no client session data. [file:9]
- Any session-specific data should be maintained by the client and sent with each request when needed. [file:9]

### REST pros and cons
- **Pros**: scalability and easier session handling. [file:9]
- **Cons**: data overhead and the need to reconstruct state on the server side for each request. [file:9]

## REST HTTP methods
This is very likely to appear in MCQs. [file:9]

| Method | Meaning in lecture | Idempotent? | Safe? |
|---|---|---|---|
| GET | Read-only operation; may include parameters in URI. [file:9] | Yes. [file:9] | Yes. [file:9] |
| PUT | Store message body; insert or update. [file:9] | Yes. [file:9] | No. [file:9] |
| DELETE | Delete resources. [file:9] | Yes. [file:9] | No. [file:9] |
| POST | Parameters in request body. [file:9] | No. [file:9] | No. [file:9] |

Other less frequently used methods listed are HEAD, OPTIONS, TRACE, and CONNECT. [file:9]

### Why REST can scale well
The lecture highlights that GET can be cached because it is safe and idempotent, and PUT and DELETE being idempotent simplify duplicate-message handling. [file:9]

## REST vs SOAP
Even though the extracted text does not provide a full bullet table, the lecture clearly positions REST as a constrained, stateless, HTTP-method-based design style and SOAP as an XML-based messaging protocol with envelopes, headers, WSDL, and optional registry lookup. [file:9]

### Quick comparison
| Topic | SOAP | REST |
|---|---|---|
| Nature | XML-based messaging protocol. [file:9] | Design style / set of constraints. [file:9] |
| Data style | Strongly tied to XML in the lecture. [file:9] | Uses resource representations over HTTP. [file:9] |
| Interface | Uses WSDL and can use UDDI. [file:9] | Uses uniform HTTP methods on URIs. [file:9] |
| State handling | Can be synchronous or asynchronous; not presented as stateless-first. [file:9] | Stateless interactions emphasized. [file:9] |

## Service-oriented architecture (SOA)
SOA is a set of design principles for building distributed systems from **loosely coupled services**. [file:9]

These services can be dynamically discovered and communicate or be coordinated through choreography to provide enhanced services. [file:9]

The lecture says the main way to realize SOA is through web services because web services naturally support loose coupling, interoperability, and flexible architecture inside organizations. [file:9]

SOA also encourages a **mashup** style of development, where a third party creates a new service by combining multiple existing services. [file:9]

### Exam-ready definition
SOA is an architectural style in which distributed functionality is organized as loosely coupled interoperable services that can be discovered, combined, and reused. [file:9]

## Microservices
The lecture describes microservices as an application architecture where each application function becomes its own service. [file:9]

These services are typically run inside containers and communicate through APIs such as web services, RPC, or events. [file:9]

Microservices are presented as loosely coupled, reusable, specialized, cloud-native components that can be updated independently, built with different stacks, and scaled independently to reduce waste and cost. [file:9]

### Microservices vs monolith intuition
Microservices let teams scale and update one part of an application independently instead of scaling the whole application when only one feature is under heavy load. [file:9]

## Fast memory table
| Topic | What to remember |
|---|---|
| Web service | Client-server interaction via request/reply over HTTP using XML or JSON. [file:9] |
| Marshalling | Convert data to transmissible external form. [file:9] |
| XML | Extensible, self-describing, human-readable, verbose. [file:9] |
| JSON | Lightweight, easier, array/object support. [file:9] |
| SOAP | XML-based protocol with envelope/header/body; uses WSDL and possibly UDDI. [file:9] |
| WSDL | Service description / IDL describing operations and access details. [file:9] |
| UDDI | Registry for discovery by name or attributes. [file:9] |
| REST | Stateless design style using URIs and HTTP methods. [file:9] |
| SOA | Loosely coupled services combined for interoperability and reuse. [file:9] |
| Microservices | Small independent services communicating through APIs. [file:9] |

## What is most likely to appear in short answers
### 1) Explain why web services matter
Possible points:
- Cross-platform and cross-organization interoperability. [file:9]
- Request/reply interaction over HTTP. [file:9]
- XML/JSON for data interchange. [file:9]
- Foundation for SOA. [file:9]

### 2) Compare XML and JSON
- JSON is lighter and easier to read/write. [file:9]
- XML is more verbose but richer as a markup language. [file:9]
- JSON supports arrays and objects natively. [file:9]
- XML often relies on schema and conventions. [file:9]

### 3) Compare SOAP and REST
- SOAP is an XML-based protocol with formal service description via WSDL. [file:9]
- REST is a stateless resource-oriented design style using uniform HTTP methods. [file:9]

### 4) Explain SOA
- SOA organizes systems as loosely coupled discoverable services. [file:9]
- Services can be composed and reused. [file:9]
- Web services are a common realization of SOA. [file:9]

### 5) Explain why Services/Mashups composition is hard
- Need choreography, concurrency, alternatives, timeouts, exceptions, callbacks, and reference passing. [file:9]

## Sample multiple-choice questions
### Set 1
1. A web service provides:  
A. A local-only file system  
B. An interface for clients to interact with remote servers  
C. A compiler for XML only  
D. A hypervisor for containers  
**Answer: B** [file:9]

2. Web service messages in the lecture are usually transmitted over:  
A. BIOS calls  
B. HTTP  
C. HDMI  
D. SATA  
**Answer: B** [file:9]

3. The lecture says web service data is commonly represented using:  
A. XML or JSON  
B. Only binary blobs  
C. Only HTML  
D. Only CSV  
**Answer: A** [file:9]

4. Web services help support:  
A. Only graphics rendering  
B. Interoperability between clients and servers  
C. Hardware cooling  
D. CPU microcode updates  
**Answer: B** [file:9]

5. Web services enable:  
A. SOA  
B. Only local execution  
C. Removal of networking  
D. BIOS programming  
**Answer: A** [file:9]

6. Marshalling is the process of:  
A. Deleting old data  
B. Converting data into a transmission-suitable form  
C. Scheduling containers  
D. Assigning TCP ports  
**Answer: B** [file:9]

7. Unmarshalling is the process of:  
A. Encrypting the message only  
B. Disassembling the data at the receiver  
C. Creating a URI  
D. Compiling source code  
**Answer: B** [file:9]

8. XML is defined by the:  
A. CNCF  
B. W3C  
C. Docker Foundation  
D. Linux Foundation  
**Answer: B** [file:9]

9. XML tags describe the:  
A. GPU firmware  
B. Logical structure of data  
C. Disk geometry  
D. CPU schedule  
**Answer: B** [file:9]

10. XML is considered self-describing because:  
A. It contains machine code  
B. Its tags describe the data  
C. It is always compressed  
D. It needs no parser  
**Answer: B** [file:9]

11. A downside of XML mentioned in the lecture is that:  
A. It cannot represent structure  
B. Textual messages are large and slower to process/transmit  
C. It cannot be read by humans  
D. It cannot use namespaces  
**Answer: B** [file:9]

12. XML attributes are:  
A. Optional name-value pairs in a start tag  
B. Always whole child documents  
C. Only used in JSON  
D. Required on every element  
**Answer: A** [file:9]

13. An XML Schema defines:  
A. Docker image layers  
B. Which elements and attributes can appear in a document  
C. Only REST methods  
D. Only URI formats  
**Answer: B** [file:9]

14. JSON is described as:  
A. Heavyweight and XML-only  
B. A lightweight data-interchange format  
C. A binary-only format  
D. A SOAP registry  
**Answer: B** [file:9]

15. JSON is based on a subset of:  
A. Java  
B. JavaScript  
C. Python  
D. XML  
**Answer: B** [file:9]

16. According to the lecture, JSON is generally:  
A. Harder to use than XML  
B. Easier to use than XML  
C. Not text based  
D. Only for web browsers  
**Answer: B** [file:9]

17. Which statement about JSON vs XML is correct?  
A. JSON has no array support  
B. XML natively supports arrays  
C. JSON has native object support  
D. XML is always more human readable  
**Answer: C** [file:9]

18. In synchronous communication:  
A. Send is non-blocking  
B. Both send and receive are blocking  
C. No messages are queued  
D. Only receiver blocks  
**Answer: B** [file:9]

19. In asynchronous communication:  
A. The send is non-blocking  
B. The send always waits for receive  
C. No buffer is used  
D. HTTP cannot be used  
**Answer: A** [file:9]

20. Messages are sent to a pair consisting of:  
A. Filename and extension  
B. Internet address and local port  
C. Username and password  
D. URI and XML schema only  
**Answer: B** [file:9]

### Set 2
21. A URL is a subset of URI that includes:  
A. Only a symbolic name  
B. A network location  
C. Only an XML namespace  
D. Only a port number  
**Answer: B** [file:9]

22. A URN is a subset of URI that includes:  
A. A name in a space but no location  
B. A network path only  
C. A TCP header  
D. A SOAP envelope  
**Answer: A** [file:9]

23. A web service endpoint is a:  
A. YAML file  
B. Web address (URL)  
C. Local process ID  
D. CPU register  
**Answer: B** [file:9]

24. Combining operations from multiple services can provide:  
A. New functionality  
B. Less interoperability  
C. Only lower security  
D. No composition  
**Answer: A** [file:9]

25. In the travel-agent scenario, the service combines:  
A. Only flight bookings  
B. Flight, hotel, and car booking services  
C. DNS and routing tables  
D. BIOS and storage drivers  
**Answer: B** [file:9]

26. SOAP stands for:  
A. Service Object Access Platform  
B. Simple Object Access Protocol  
C. Secure Operation Access Process  
D. Standard Object API Platform  
**Answer: B** [file:9]

27. SOAP is primarily described as:  
A. A JSON-only protocol  
B. An XML-based protocol  
C. A hardware interface  
D. A container runtime  
**Answer: B** [file:9]

28. SOAP services use which IDL?  
A. WSDL  
B. YAML  
C. JSON Schema only  
D. DNS  
**Answer: A** [file:9]

29. SOAP services may be looked up in which registry?  
A. UDDI  
B. GitHub  
C. Docker Hub  
D. Route 53  
**Answer: A** [file:9]

30. A SOAP message is carried inside an:  
A. Array  
B. Envelope  
C. Pod  
D. Container  
**Answer: B** [file:9]

31. Which parts are inside a SOAP envelope?  
A. Optional header and body  
B. Only a footer  
C. Only a checksum  
D. Only an API token  
**Answer: A** [file:9]

32. In SOAP, faults are returned in a:  
A. Cookie  
B. Fault element  
C. URI parameter  
D. Port selector  
**Answer: B** [file:9]

33. WSDL mainly describes:  
A. Hypervisor state  
B. Web service operations and access details  
C. Only database schemas  
D. Only TCP windows  
**Answer: B** [file:9]

34. A binding in WSDL indicates the:  
A. File owner  
B. Choice of protocol  
C. CPU architecture  
D. Number of replicas  
**Answer: B** [file:9]

35. A service definition in WSDL includes the:  
A. Endpoint address  
B. Monitor resolution  
C. BIOS version  
D. Integer size  
**Answer: A** [file:9]

36. UDDI provides:  
A. A name service and directory service  
B. A Linux shell only  
C. A memory allocator  
D. A load balancer only  
**Answer: A** [file:9]

37. REST stands for:  
A. Remote Execution Service Transfer  
B. Representational State Transfer  
C. Resource Endpoint Service Template  
D. Reliable External Schema Transport  
**Answer: B** [file:9]

38. REST originated from the PhD dissertation of:  
A. Solomon Hykes  
B. Roy Fielding  
C. Tim Berners-Lee  
D. Bill Gates  
**Answer: B** [file:9]

39. RESTful services manipulate resources using:  
A. Only XML schemas  
B. URLs and HTTP methods such as GET, PUT, DELETE, POST  
C. Only TCP raw sockets  
D. Only UDDI APIs  
**Answer: B** [file:9]

40. REST is described in the lecture as:  
A. The physical architecture of the system  
B. A set of design criteria  
C. A binary transport format  
D. A WSDL registry  
**Answer: B** [file:9]

41. In REST, each resource should be addressable via a:  
A. Pod  
B. URI  
C. Hypervisor  
D. Volume  
**Answer: B** [file:9]

42. Which REST method is safe and idempotent?  
A. POST  
B. GET  
C. CONNECT  
D. TRACE only  
**Answer: B** [file:9]

43. Which REST methods are idempotent but not safe according to the lecture?  
A. PUT and DELETE  
B. GET and POST  
C. POST and OPTIONS  
D. HEAD and CONNECT  
**Answer: A** [file:9]

44. Which REST method is neither idempotent nor safe?  
A. GET  
B. PUT  
C. DELETE  
D. POST  
**Answer: D** [file:9]

45. One REST benefit mentioned is:  
A. No interoperability  
B. HTTP is widely supported  
C. Mandatory server-side session storage  
D. Lack of caching  
**Answer: B** [file:9]

46. SOA is based on sets of:  
A. Tightly coupled monoliths  
B. Loosely coupled services  
C. Hardware drivers  
D. Only XML documents  
**Answer: B** [file:9]

47. A mashup in SOA is:  
A. A hypervisor bug  
B. A new service created by combining two or more existing services  
C. A JSON syntax rule  
D. A TLS certificate  
**Answer: B** [file:9]

48. Microservices are described as:  
A. One huge application unit only  
B. Small independent services communicating through APIs  
C. A SOAP registry format  
D. A replacement for all containers  
**Answer: B** [file:9]

49. Microservices can be scaled:  
A. Only as a whole application  
B. Independently by component  
C. Only through XML Schema  
D. Only with UDDI  
**Answer: B** [file:9]

50. According to the lecture, microservices are a:  
A. Legacy-only approach  
B. Cloud-native architectural approach  
C. Hardware virtualization method  
D. SOAP transport protocol  
**Answer: B** [file:9]

## Sample short-answer questions with model points
### SAQ 1
**Question:** Define a web service.  
**Model points:** A web service is an interface that allows clients to interact with remote servers through request and reply messages, usually over HTTP, with data represented using XML or JSON. [file:9]

### SAQ 2
**Question:** Why are external data representation and marshalling needed?  
**Model points:** Different machines represent data differently, so data must be converted into a standard external format for transmission and then converted back at the receiver. Marshalling prepares the data for transmission and unmarshalling reconstructs it. [file:9]

### SAQ 3
**Question:** Compare XML and JSON.  
**Model points:** XML is extensible, self-describing, and schema-friendly but more verbose. JSON is lightweight, easier to read and write, supports arrays and objects natively, and is often simpler for data interchange. [file:9]

### SAQ 4
**Question:** Explain synchronous vs asynchronous communication.  
**Model points:** In synchronous communication, send and receive are blocking. In asynchronous communication, the sender continues after copying the message to a local buffer while transmission proceeds in parallel. [file:9]

### SAQ 5
**Question:** Distinguish URI, URL, and URN.  
**Model points:** A URI is a general identifier, a URL is a URI that includes location, and a URN is a URI that gives a name without location. A web service endpoint is typically a URL. [file:9]

### SAQ 6
**Question:** Explain the travel-agent example and what it shows.  
**Model points:** The travel-agent service coordinates several underlying services such as flights, car hire, and hotel booking. It demonstrates service composition and orchestration of multiple service interactions. [file:9]

### SAQ 7
**Question:** What is SOAP?  
**Model points:** SOAP is an XML-based protocol for exchanging information between applications. It uses request/reply messaging, can work over several transports, and commonly relies on WSDL for service description. [file:9]

### SAQ 8
**Question:** Describe the structure of a SOAP message.  
**Model points:** A SOAP message has an envelope, an optional header, and a body. The body contains the operation details and arguments or response data, while faults are reported in a fault element. [file:9]

### SAQ 9
**Question:** What is WSDL and why is it useful?  
**Model points:** WSDL is the Web Services Description Language and acts as an IDL for web services. It describes operations, data types, bindings, and service access details, and tools can use it to generate client or server code. [file:9]

### SAQ 10
**Question:** What is UDDI?  
**Model points:** UDDI is a directory and discovery service for web services. It allows service descriptions to be looked up by name or by attributes. [file:9]

### SAQ 11
**Question:** What is REST?  
**Model points:** REST is a constrained design style for web services in which resources are identified by URIs and manipulated using stateless HTTP methods such as GET, PUT, DELETE, and POST. [file:9]

### SAQ 12
**Question:** Explain statelessness in REST.  
**Model points:** REST does not keep client session state on the server. Any request-specific or session-specific information should be maintained by the client and sent with each request as needed. [file:9]

### SAQ 13
**Question:** Explain the difference among GET, PUT, DELETE, and POST.  
**Model points:** GET reads resources and is safe and idempotent. PUT inserts or updates and is idempotent but not safe. DELETE removes resources and is idempotent but not safe. POST is neither idempotent nor safe. [file:9]

### SAQ 14
**Question:** Define SOA.  
**Model points:** SOA is a design style in which distributed systems are built from loosely coupled services that can be discovered, coordinated, and combined to provide richer functionality and interoperability. [file:9]

### SAQ 15
**Question:** What are microservices and how do they relate to cloud-native systems?  
**Model points:** Microservices are small specialized services, often containerized, that communicate through APIs and can be updated and scaled independently. This makes them agile, scalable, reusable, and cloud-native. [file:9]

## Likely exam traps
- Do not confuse **marshalling** with **unmarshalling**. [file:9]
- Do not confuse **URI**, **URL**, and **URN**. [file:9]
- Do not forget that **REST is a design style**, not a message format or physical architecture. [file:9]
- Do not say **POST is idempotent**; the lecture explicitly says it is not. [file:9]
- Do not confuse **SOAP envelope/header/body** with **WSDL**; WSDL describes the service, SOAP carries the messages. [file:9]
- Do not confuse **SOA** with **microservices**; they are related but not identical concepts in the lecture. [file:9]

## 15-minute revision plan
1. Memorize the web service definition and marshalling/unmarshalling. [file:9]
2. Memorize the XML vs JSON comparison. [file:9]
3. Memorize URI vs URL vs URN. [file:9]
4. Memorize SOAP basics: envelope, header, body, WSDL, UDDI. [file:9]
5. Memorize REST methods and idempotent/safe properties, then review SOA and microservices. [file:9]

## Ultra-short cram sheet
- Web service = remote client-server interaction via messages over HTTP using XML/JSON. [file:9]
- Marshalling = convert for transmission; unmarshalling = reconstruct on receipt. [file:9]
- XML = extensible, self-describing, verbose. [file:9]
- JSON = lightweight, easier, arrays/objects built in. [file:9]
- SOAP = XML protocol with envelope/header/body, WSDL, optional UDDI. [file:9]
- REST = stateless design style using URIs + GET/PUT/DELETE/POST. [file:9]
- GET is safe + idempotent. [file:9]
- PUT and DELETE are idempotent, not safe. [file:9]
- POST is neither safe nor idempotent. [file:9]
- SOA = loosely coupled discoverable services; microservices = small independent API-connected services. [file:9]

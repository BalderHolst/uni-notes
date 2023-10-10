# Network Layer
See [[KOM - lecture 6 - Itslearning.pdf#page=3|slides]].

Responsible for host-to-host delivery of datagrams. Is can control communication across *multipule networks*.

Responsible for *routing* (find the fastest route).

#### Fragmentation
Do route packets, sometimes the packets have to be repackaged to be sent over a different network. This process is called fragmentation.

#### Routing
*Create* a table (routing table) of where incoming packets should be sent.

#### Forwarding
The *act* of redirecting incoming packets.

#### Error Checking
No error checking because if the posibility of fragmentation.

#### Flow Control
No flow control.

#### Congestion Control
Congestion: when there is too much traffic in a part of the network. This results in dropped packets.

#### Quality of Service
Especially for Audio and Video Streaming.

This is **not implemented here**, but in the upper layers.

#### Security
A layer called ipSEC can be implemented.

---

#### Datagram Approach / Connectionless Service
Packages may arrive out of order, as they may take different routes.
#### Virtual-Circuit Approach / Connection Oriented Service
See [[KOM - lecture 6 - Itslearning.pdf#page=13|slides]].

A route is chosen, and all packets are send along the same route. This means that the packets arrive in order with no need to be sorted.

This means that communication happens in three phases
1. Setup: Sender sends a request packet through the route to the destination, and generate all the labels required for the transmission.
2. Communication
3. Tear-down

---

## Perf

---
#datacommunication
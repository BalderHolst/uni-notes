# Network Layer
See [[KOM - lecture 6 - Itslearning.pdf#page=3|slides]].

Responsible for host-to-host delivery of datagrams. Is can control communication across *multipule networks*.

Responsible for *routing* (find the fastest route).

### Ip-Address
See [[KOM - lecture 6 - Itslearning.pdf#page=35|slides]].

#### IPv4
A 32-bit address.


---

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
Packages may arrive out of order, as they may take different routes. The packets therefore have to be sorted after getting received.
#### Virtual-Circuit Approach / Connection Oriented Service
See [[KOM - lecture 6 - Itslearning.pdf#page=13|slides]].

A route is chosen, and all packets are send along the same route. This means that the packets arrive in order with no need to be sorted.

This means that communication happens in three phases
1. Setup: Sender sends a request packet through the route to the destination, and generate all the labels required for the transmission.
2. Communication
3. Tear-down: Remove labels from routers.

---

## Performance
### Delay
The delay consists of four parts:
**Transmission Delay**: The time it takes to actually transmit the data
$$\text{delay}_{transmittion} = \frac{\text{packet length}}{\text{transmission speed}}$$
**Propagation Delay**
**Processing Delay**
**Queing Delay**

### Throughput
How much parallel data can be sent through a link. In practice most throughput issues are in the connection (in the local network) to the main internet backbone.

### Packet Loss
Routers have buffers to store packets, but they can be overwhelmed.

When a packet is lost, it will cause the sender to resend the packet, which worsens the situation.

### Congestion Control 
#### Open-loop Congestion Control
**Re-transmission Policy**: Make sure senders wait a certain amount of time before sending again.

**Window Policy**
- *Selective Repeat Window*: Only re-transmit lost packages. This can mean that packets are received out of order though.
- *Go-Back-N*: Re-transmit all packets from the lost packet.
- *Acknowledgement Policy*: The receiver only sends ONE ACK-packet per $N$ received packets.
- *Discarding Policy*: The router discards less sensitive packets.
- *Admission Policy*: Create a special channel for important packets.

#### Closed Look Congestion Control
See [[KOM - lecture 6 - Itslearning.pdf#page=32|slides]].

*back-pressure*: propagate *back-pressure* to stop the incoming flow of packets.
*choke-packer*: send choke packet to the source to stop it sending packets.
*Implicit Signalling*: The sender notices a choke by itself and slows down packet transmission.
*Explicit Signalling*: Include a choke-packet in another packet, to notify the sender of the congestion



---
#datacommunication

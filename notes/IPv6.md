# IPv6
Successor to [[IPv4]]. See [[KOM - lecture 8a - Itslearning.pdf#page=3|slides]].

Addresses are 128 bit.

Addresses can be either
- Unicast: Address of one specific computer
- Anycast: Address of a group of computers, **only one** will receive the packet.
- Multicast: Address of a group of computers, **all** will receive the packet.

![[Pasted image 20231031123001.png|600]]

## Benefits
- Better header format
- New options for additional functionality
- Possibility of extension
- Resource allocation support

![[Pasted image 20231031131449.png|600]]

### Global Unicast Addressing
![[Pasted image 20231031123135.png|600]]
- Global routing prefix: Website/Domain
- Subnet: Ex: Sections of a company
- Interface Identifier: The physical plug

### Special Addresses
![[Pasted image 20231031123917.png]]
**Compatible**: Used when IPv4 devices want to communicate with each other
**Mapped**: Used when IPv6 devices want to communicate IPv4 devices

---
## Network Layer
![[Pasted image 20231031124237.png]]

#### Unique Local Unicast
For packets that do not leave the organisation. Randomness used to minimise the likelihood of identical addresses.

#### Link Local
Private organisation addresses

#### Multicast
Access multiple machines

### Auto-configuration
See [[KOM - lecture 8a - Itslearning.pdf#page=19|slides]]. Automatically generated addresses.

### Flow Packets
See [[KOM - lecture 8a - Itslearning.pdf#page=29|slides]].

Flow packets allow for data streaming. Handles by the *flow label table*. It works by allocating resources for a stream in advance.

### Extension Headers
See [[KOM - lecture 8a - Itslearning.pdf#page=32|slides]].

For setting options in all routers that the packet traverses
![[Pasted image 20231031130021.png]]

##### Fragmentation
**ONLY THE SENDER CAN PERFORM FRAGMENTATION**.

Instead we find the bottleneck and use the minimum MTU.

### ICMPv6
See [[KOM - lecture 8a - Itslearning.pdf#page=40|slides]].

---

## Transport Layer
See [[KOM - lecture 8b - Itslearning.pdf#page=4|slides]].

Process to Process communication.

**Port numbers** designate the destination process.

Port numbers for server processes must be know. Otherwise the client does not know where to connect.

##### Socket Address
Ip address + port number = Socket address
Ex: 200.23.56.8:69

---
#datacommunication
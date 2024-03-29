# NAT
Network Address Translation
See [[KOM - lecture 7 - Itslearning.pdf#page=4|slides]].

Assign a few addresses to a local network, and have a large number of internal addresses.

### Translation Table
A *mapping* between local and public addresses. These **mappings are temporary**.

![[Pasted image 20231024122734.png]]

NAT routers can have more than one external address.

### Forwarding Table
**DIFFERENT FROM TRANSLATION TABLE**
See [[KOM - lecture 7 - Itslearning.pdf#page=11|slides]].

Where to send received packets.

#### Address Aggregation
Avoid long forwarding tables.

![[Pasted image 20231024124505.png|500]]

Always choose the address with the longest mask address, as it will be physically closer to the router.

#### Hierarchical Routing
![[Pasted image 20231024125231.png|500]]


---
#datacommunication 
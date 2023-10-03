# Ethernet
See [[KOM - lecture 5b - Itslearning.pdf#page=3|slides]].

### Standard Ethernet
There are **4 generations** that are all faster than the last.

Does not acknowledge received frames.

#### Parts
- Preamble: 7 alternating ones and zeroes to alert receiver
- SFD: Start frame delimiter
- Length/type of data
- Data: data (size: 46-1500 bytes) padded with zeros if it is smaller than the minimum data size. The minimum size is to make sure the transmission is at least double propagation time.
- Addressing: All ones means broadcasting. ...

#### Physical Layer (Cables)
Hub = physical layer

A bridge can be used to can split a shared medium to increase the data rate because of reduced likelihood of collisions.
##### 10Base5
10 Mbps, digital, max 500 m

Bus typology
##### 10Base2
Mbps, digital, max 185 m

Cheaper than 10Base5

##### 10Base-T
Mbps, digital, max 100 m
Twisted pair cable
##### 10Base-F
Fiber-optic cables

---
#datacommunication
# Media Access 
See [[KOM - lecture 5a - Itslearning.pdf|slides]].

>[!tip]
>[[#CSMA/CD]] is the best, as it has the hightest throughput.

---
### Random Access
See [[KOM - lecture 5a - Itslearning.pdf#page=7|slides]].

All nodes can send whenever they want, therefore conflicts can occur.

### Pure ALOHA
See [[KOM - lecture 5a - Itslearning.pdf#page=8|slides]].

Time is divided into time slots, but the time slots are not synchronised between nodes. Each node sends all its data within a random time slot. This leads to collisions.between nodes. Each node wait for the transmission medium to be free and sends all its data within the time slot. This leads to collisions.

### Slotted ALOHA
See [[KOM - lecture 5a - Itslearning.pdf#page=13|slides]].

Frames must be sent within time slots, doubling throughput.

### Carrier Sense Multiple Access (CSMA)
See [[KOM - lecture 5a - Itslearning.pdf#page=15|slides]].
Sense whether the transmission medium is free. Only send if it is.

**Collisions can still occur** because of delay.

### CSMA/CD
See [[KOM - lecture 5a - Itslearning.pdf#page=21|slides]].

Same as CSMA but with a description of how to handle collisions.

To be able to detect collisions and abort sending a frame, while still sending it. The frame time ($T_{fr}$) must be at least double the propagation time ($T_{p}$).
$$T_{fr} \geq 2 \cdot T_{p}$$
### CSMA/CA
See [[KOM - lecture 5a - Itslearning.pdf#page=28|slides]].

The sender "asks" is the receiver (RTS-frame) is ready to receive data. The receiver replies with a CTS (clear-to-send), is also sends it to the other devices in the network. They are not allowed to send anything until the receiver notifies the other devices that the transmission has ended.

Can prioritize frames by changing IFS-value.

This also uses a timer + ACK frames.

---

## Controlled Access
See [[KOM - lecture 5a - Itslearning.pdf#page=37|slides]].

### Reservation
Send a frame that describes the destination of the next $n$ frames.

### Select
First send a SEL (select) frame, which determines the destination of the following data frame.

### Poll
Send Poll frame to other devices to find out if they are ready to send to primary device.

### Token Passing
Circulate a "token". The device with the token has permission to send. After the data is send, the token is passed on.

##### Rules
- The time a device has a token must be limited
- The token must be monitored to make sure it is not lost
- ...

### Logical Ring
...

---
## Channelization
See [[KOM - lecture 5a - Itslearning.pdf#page=43|slides]].

### Frequency-Division Multiple Access (FDMA)
Divide the bandwidth into frequency band for parallel communication.

### Time-Division Multiple Access (TDMA)
Each station gets its own time slot to send data. *Syncronication between stations is hard* because of propagation delay.

### Code-Division Multiple Access (CDMA)
See [[KOM - lecture 5a - Itslearning.pdf#page=48|slides]].

We send codes (cheap sequences) with the following properties:
- If we multiply a code with another the result is $0$
- If we multiply a code with itself we get the sender id

#### Data Representation
- A bit that is $0$ is represented as $-1$
- A bit that is $1$ is represented as $1$
- If nothing is sent it is represented as $0$

---
#datacommunication

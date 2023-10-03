# Media Access 
See [[KOM - lecture 5a - Itslearning.pdf|slides]].

>[!tip]
>[[#CSMA/CD]] is the best, as it has the hightest throughput.

---
### Random Access
All nodes can send whenever they want, therefore conflicts can occur.

### Pure ALOHA

### Slotted ALOHA
Frames must be sent within time slots, doubling throughput.

### Carrier Sense Multipule Access (CSMA)
Sense whether the transmission medium is free. Only send if it is.

**Collisions can still occur** because of delay.

### CSMA/CD
Same as CSMA but with a description of how to handle collisions.

To be able to detect collisions and abort sending a frame, while still sending it. The frame time ($T_{fr}$) must be at least double the propagation time ($T_{p}$).
$$T_{fr} \geq 2 \cdot T_{p}$$
### CSMA/CA

Can prioritize frames by changing IFS-value.

This also uses a timer + ACK frames.

---
#datacommunication

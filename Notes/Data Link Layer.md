## Framing
See slides [[KOM - lecture 4a - Itslearning.pdf#page=6|here]] and more [[KOM - lecture 4b - Itslearning.pdf#page=3|here]].

Ways of dividing data into packets for transmission.

### Character-oriented framing
![[Pasted image 20230926123006.png]]

Escape characters are used to send the flag without it being interpreted as a flag by the receiver.

### Bit-oriented framing
![[Pasted image 20230926123459.png]]

## Flow and Error Control Protocols
See [[KOM - lecture 4a - Itslearning.pdf#page=14|slides]].

### Automatic Repeat reQuest (ARQ)
The sender listens for a confirmation packet from the receiver. If it does not receive a confirmation, it simply resends the frame. 

### Stop-and-Wait
After a frame is sent, the sender waits for an ACK (acknowledgement) packet.
![[Pasted image 20230926124212.png]]

This can be implements as two state machines:
![[Pasted image 20230926124500.png]]

The **data-frames and ACK's are numbered** to ensure that the receiver does not send the data twice, if the ACK is lost/corrupted.

It is sometimes quite wasteful to transmit ACK packets, as it results in double the messages. [[Piggybacking]] solves this by inserting ACK packets into the messages from the receiver to the sender.
### High-Level Data Link Control (HDLC)
*bit oriented.*

[[KOM - lecture 4b - Itslearning.pdf#page=3|slides]]

### Point-to-Point
[[KOM - lecture 4c - Itslearning.pdf|slides]].

![[Pasted image 20230926133743.png|450]]

---
#datacommunication 

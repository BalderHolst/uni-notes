# Transport Layer
See [[KOM - lecture 9a - Itslearning.pdf|slides]].

### Protocols
- [[KOM - lecture 9a - Itslearning.pdf#page=9|stop-and-wait]]
	- Only *one packet* in the channel at a time
	- Reliable but inefficient
	- just go-back-N where N=1
- [[KOM - lecture 9a - Itslearning.pdf#page=16|go-back-N]]:
	- Idea: acknowledge more than one packer at a time
	- We still have to resend correctly received packets if the sender times out
- [[KOM - lecture 9a - Itslearning.pdf#page=28|selective-repeat]]
	- Only resend corrupted packets
	- Always same ACK as received number
 - [[TCP-IP#Transport Layer|TCP]]
	 - Reliable
	 - Connection Oriented
 - [[KOM - lecture 9a - Itslearning.pdf#page=43|UDP]]
	 - Unreliable
	 - Connectionless
	 - Continuous data stream
	 - No flow control
	 - No error control

We can use [[piggybacking]] in bidirectional communication.

---
#datacommunication
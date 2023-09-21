# TCP/IP

##### Example of the logic inside a single router
![[Pasted image 20230919124703.png|450]]

$L$: Data Link Address (mac addresses), each router has a local and a public address.
$N$: IP of the sender and final receiver of a packet.
## Data Link Layer
See [[KOM - Lecture 3_a - Itslearning.pdf#page=3|slides]].

#### Sublayers
- Data Link Control (DLC) : this layer takes care of all the issues common to both point-to-point and broadcast links. 
- Media Access Control (MAC) : Only deals with the issues specific to broadcast links.

![[Pasted image 20230919122516.png]]

#### Addressing
See [[KOM - Lecture 3_a - Itslearning.pdf#page=8|slides]].

![[Pasted image 20230919123314.png|450]]

Each router uses a [[Forwarding Table]] to determine where to relay the packet.

##### Types of addressing
- Unicast Addressing: Sener and reciever are known
- Multicast Addressing: One to many communication *within local network*
- Broadcast Addressing: One to all

### Errors
See [[KOM - Lecture 3_b - Itslearning.pdf#page=3|slides]].

Error detection is of cause easier than error correction.

**Burst Error**: Two or more bits are flipped

#### Block Coding
Message is divided into blocks (*"datawords"*), and add **redundant bits** to each packet to create *"codewords"*.

>[!example]- Diagram 
>![[Pasted image 20230919130937.png]]

The sender makes sure that the codeword is a *correct codeword*. Determining if a codeword is current, requires a table for validating the codeword, which is **shared by sender and receiver**.

*The minimum [[Hamming Distance]] between valid codewords should be $2$,* to make sure a bit-flip does not result in another valid codeword. This is the case in [[Parity-Check Code]].

>[!warning] Limitations
> If both the datawords and codewords are corrupted, it might also result in a "correct" codeword. 
##### Linear Block Coding
You can $\text{XOR}$ two valid codewords to get another valid codeword.
$$A \,\, \text{XOR} \,\, B= C $$
Where $A$, $B$ and $C$ are all valid.

##### Cyclic Coding
Se [[KOM - Lecture 3_b - Itslearning.pdf#page=15|slides]].

The redundant bit "rotate" for each dataword.
![[Pasted image 20230919133343.png|450]]

$$s(x) = e(x) \,\,\text{mod} \,\, g(x)$$
$x$: Dataword
$s(x)$: Syndrome - should be $0$ in a valid codeword
$e(x)$: The error
$g(x)$: The generated codeword

Generators with a factor of $(x+1)$ can detect all odd number of bit-flips.

---
#datacommunication 
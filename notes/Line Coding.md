# Line Coding Schemes
Ways to **convert digital data to an analog signal** in a "good way", making it easy for the receiver to interpret the signal.

The receiver must be able to convert the received signal in a *relative way*, as absolute voltages may not be preserved.

![[Pasted image 20230912132701.png|500]]
### Unipolar NRZ (NON-RETURN-TO-ZERO)
![[Pasted image 20230912125654.png|450]]

##### Problems
- A lot of power to send one bit
- Synchronisation has to be perfect
- *Baseline Wandering*: Many ones will shift the running average (baseline for the reciever)

### Polar NRZ-L(=level) and NRZ-I(=invert)
Fixes the baseline wandering of [[#Unipolar NRZ (NON-RETURN-TO-ZERO)]].
![[Pasted image 20230912130024.png|450]]

### Polar RZ
You HAVE to change the signal half way through a data unit. Therefore the reciever can deduce the frequency.
![[Pasted image 20230912130248.png|450]]

##### Problems
- Three signal levels -> need higher [[bandwidth]].

### Polar Manchester and Differential Manchester
Invented to fix the problems of the three others.
![[Pasted image 20230912130525.png|450]]
Notice: The signal passes through GND once for every bit.

### Bipolar AMI
Used for long distance communication.
![[Pasted image 20230912131022.png|450]]
##### Problems
- Sync issues with many zeroes

### Multilevel: 2B1Q
Two bits, one [[Signal element|signal element]] -> $4$ levels.
![[Pasted image 20230912131428.png|450]]

### Multilevel: 8B6T
![[Pasted image 20230912131746.png]]
Here there are many redundant signal element meaning, the [[signal element]] could contain more than $8$ bits of data. These extra patters can be used as control patterns for the receiving hardware.

### Multilevel: 4D-PAM5
4 Dimensional Pulse Amplitude Modulation 5 levels (4D-PAM5):
- As can be seen, 4 wires are used simultaneously!
- 5 levels of -2, -1, 0, 1, 2 voltages are used.
- 0 voltage is only used in connection with error detection.
- On each wire, it transmits a pulse of the corresponding magnitude.
![[Pasted image 20230912132128.png]]

### Multitransition: MLT-3
Uses a state machine for parsing to keep the baseline close to GND.
![[Pasted image 20230912132439.png]]

Multi Line Transmission 3 levels (+, 0, -). The following 3 
transition rules are used:
1. If the next bit is 0, stay at the same signal level.
2. If the next bit is 1 and the current signal level is not 0, then go to 
signal level 0.
3. If the next bit is 1 and the current signal level is 0, then go to the

---
#datacommunication 
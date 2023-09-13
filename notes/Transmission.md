# Transmission

### Signal Impairment
##### Attenuation: Loss of energy
$$dB  = 10 \cdot \log_{10}\left(\frac{P_{2}}{P_{1}}\right)$$
$P_{1}$: Initial power
$P_{2}$: Final power

$$dB  = 20 \cdot \log_{10}\left(\frac{V_{2}}{V_{1}}\right)$$
$V_{1}$: Initial Voltage
$V_{2}$: Final Voltage

##### Distortion
Different frequencies will be warped (in phase) differently as the signal travels. Therefore the receiver signal will be distorted.
![[Pasted image 20230912120722.png|450]]

##### Noise
- *Thermal noise*: From random movements of electrons in the conductor.
- *Induced noise*: Electromagnetic (motors, machines...)
- *Crosstalk*: Another wire affects this line
- *Impule noise*: lightning, thunderstorms...


### Signal-to-Noise ratio
$$SNR=\frac{\text{average signal power}}{\text{average noise power}}$$
$$SNR_{dB}  = 10 \cdot \log_{10}(SNR)$$
![[Pasted image 20230912121313.png|450]]

### Data rate limit

Depends on three factors
- Available bandwidth
- Level of the signals we use
- Quality of the channel (noise level, SNR)

[[Shannon Formula]]

---
#datacommunication 
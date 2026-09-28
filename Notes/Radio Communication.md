# Radio Communication
Electromagnetic waves, therefore the same properties and light.

A good antenna has a length of half the wave length.

Propagates in straight lines until it hits a mass. Here it can reflect or refract.
![[Pasted image 20260925085954.png|400]]

$$
f \cdot \lambda = \mu \overset{\mathrm{usually}}{=} c
$$
$f$: Frequency ($\mathrm{Hz}$)
$\lambda$: Wavelength ($m$)
$\mu$: Propagation Speed
$c$: Speed of light ($\approx 3\cdot 10^{-8}$)

#### Polarizatoin
The orientation of the *electric field oscillation*. Antennas have to be oriented the same, to transmit data because of this.

#### Circular Polarization
We make the polarization turn as it propagates. It can be *clockwise* or *counterclockwise*.

The rotation is reversed when the wave hits a mass.

#### Radio Spectrum
**VLF**: 3kHz - 30kHz
**LF**: 30kHz - 300kHz **MF**: 300kHz - 3Mhz **HF**: 3Mhz - 20Mhz
**VHF**: 30Mhz - 300Mhz
**UHF**: 300Mhz - 3Ghz
**SHF**: 3Ghz - 30Ghz
**EHF**: 30Ghz - 300Ghz

#### ISM
Free for use frequencies with certified hardware.

#### Power
Power dB is *scaled diffrently* than voltage and curent. We multiply by $10$, not $20$ as usual.
$$
\mathrm{dB} = 10 \cdot \log_{10} \frac{P_{1}}{P_{2}}
$$

#### Antennas
An antenna should be half the wavelength of the desired wave. It also has to be correctly polerized.

The electric field ocillation enduces a current in the antenna. 

Gain for transmission = Gain for reception.

Strength decreases with the *square of the distance*.
##### Point Antenna
Theoretical antenna, an unfinetly small point. Transmits signals in a sphere, therefore it is *isotropic*. $0\ \mathrm{dBi}$.

##### Dipole Antenna
It transmits more power in one direction.
$$ 0\ \mathrm{dBd} = 2.15\ \mathrm{dBi}$$
##### Ground Place Antenna
Works exactly like the dipole.
 
Good for when you don't know where you are receiving/transmitting to.

##### Reflector (Yagi-Uda Antenna) 
Directional antenna. Good when you *know* where your recipient is.

#### Radio Link Budget
You have a transmitter (Tx) and a receiver (Rx).

*QUESTION*: Do we have enough signal strength to reveive the signal?

1. Cable loss
2. Antenna gain
3. Transmission loss (FSPL - Free Space Path Loss)
4. Receiver antenna loss
5. Cable

To answer the question, look at *signal-to-noise-ratio* (SNR) on the receiver. 


---
#drones

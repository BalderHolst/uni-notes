# Global Navigation Satellite System (GNSS)
GPS is an implementation of GNSS.

$5\%$ of the time, accuracy is *worse* than $\pm 15$ meters.

Absolute position changes *slowly* over time.

#### Functionallity
Satelites (four or more) are broadcasting their time using *very accurate clocks*.

We need **four** satelites, as our drone does not have an accurate clock. We use a fourth satelite to get another equation. Four satelites, four equatioins, four unknowns: $x$, $y$, $z$ and $t_{\mathrm{drone}}$.

A GPS needs some time to get the "almanac" from the satelites.  "GPS fix" is when the GPS has a map of available satelites, and has recognised four satelite signals.

The drone **only recieves** signals!

The satelites send an "almanac", which contains the locations of all satelites.

Satelites send "chips" which are recognisable units of noise. These chips are so long, about 300m, that the distance to the satelite can be determined by finding the position in the sequency.

##### 3 Satelite Navigation
If only three satelites are available, a 2D position can be acuired by using a height map to remove the $z$ unknown.

##### Frequency Bands
We choose frequency bands *least affected by water*.


- $L_1$: 1575 MHz
- $L_2$: 1227 MHz

There are more frequencies $L_3$, $L_4$, $L_5$, $\dots$
These can be used to correct for signal latency due to the atmosphere.

##### Satelite "holes"
It happens that an area of the sky contains no satelites at some times of day. This can be a problem in confined spaces.

##### Ground Stations (DGPS)
A ground station with an *known absolute position*, can be used to increase the accuacy of the GPS. The ground station is sending the *error for each satelite*. The drone subtracts the error for each satelite before doing calculations.

**Not all GPS's support this.**

DGPS has accuacy of $\pm 1$ meters.

##### Higher Accuacy (RTK)
We sample the **carrier** wave ($L_*$). This can provide centimeter precision.
Needs more satelites (6 or more).

1. **RTK float**: Running but has not determined its place down fixed presicion
2. **RTK fixed**: Abount 2 cm precision

We can't always get an RTK fixed position. It will cut out sometimes.

##### Coordinate System
![[Pasted image 20260911095035.png]]

---
#drones
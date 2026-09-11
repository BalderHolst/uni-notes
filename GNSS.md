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

---
#notag
# Global Navigation Satellite System (GNSS)
GPS is an implementation of GNSS.

#### Functionallity
Satelites (four or more) are broadcasting their time using *very accurate clocks*.

We need **four** satelites, as our drone does not have an accurate clock. We use a fourth satelite to get another equation. Four satelites, four equatioins, four unknowns: $x$, $y$, $z$ and $t_{\mathrm{drone}}$.

The drone **only recieves** signals!

The satelites send an "almanac", which contains the locations of all satelites.
##### 3 Satelite Navigation
If only three satelites are available, a 2D position can be acuired by using a height map to remove the $z$ unknown.



---
#notag
# Transuesse Mercator Projection
We divide the globe into "slices" and create a coordinate system on each. The coordinate system is more accurate closer to its [[Latitude and Longitude|longitude]] line.

$$
\mathrm{UTM} \underbracket{32}_\mathrm{slice\ nr.} \cancel{\mathrm{U}}\ \mathrm{E}\ 590756 \mathrm{m} \ \mathrm{N}\ 6136691\mathrm{m}
$$
$U$: is an offset of the slice. This is not used anymore.

There are *many* ways to slice the globe.
![[Pasted image 20260911102028.png]]

> [!warning] Not at the poles
> UTM cannot be used at poles, as it is too inaccurate. It is undefined at 85 degrees at the north pole, and 80 degrees at the south pole.

---
#drones
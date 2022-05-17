# Integration med Substidution

Dette er udtrykket vi forsøger at [[Integralregning|integrere]].
$$\int sin(2t + \pi) dt$$

Vi definerer u som den inderste funktion. Hvis det er en brøk er $u$ altid nævneren.
$$u = 2t + \pi$$

Vi [[Differentialregning|differentierer]]
$$u' = \frac{du}{dt} = 2$$

Isolerer $dt$
$$dt = \frac{1}{2}du$$

Sætter $u$ og $du$ ind i formlen
$$\int sin(u) \cdot \frac{1}{2}du \arrows \frac{1}{2} \cdot \int sin(u) du \arrows \frac{1}{2} \cdot (-cos(u)+k)$$

Vi sætter ind på $u$'s plads
$$\frac{1}{2} \cdot (-cos(u)+k)$$

Dette er det [[Integralregning|intregrerede]] udtryk.

---
#matematik 
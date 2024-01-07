## Matched z-transformation
See [[lektion 8 - Introduktion til IIR filtre.pdf#page=11|slides]].

Poler og nulpunkter overføres direkte til z-domænet med formlen:
$$z = e^{sT}$$
![[Pasted image 20231102085545.png|300]]

## Procedure
1. Bestem den frekvensnormerede og faktoriserede overføringsfunktion
2. Find poler og nulpunkter
3. Find [[Filters#Frekvensnormering|denormerede]] poler og nulpunkter (gange med cutoff/center frekvens)
4. Overfør poler og nul-punkter til z-domæne. Sæt poler og nul-punkter ind i stedet for $s$ for at finde det tilsvarende i $z$-domænet
$$z=e^{sT}$$


6. Opskriv overføringsfunktionen og gang en konstant på for at få constant DC forstærkning.Find konstanten med ligningen:
$$H(s)|_{s=0} = H(z)|_{z=1}$$
7. Opskriv den endelige løsning

>[!example]- Eksempel på Procedure
>![[Lessons/Semester 3/signalbehandling/Exercises/lektion8.pdf|lektion8#page=1]]

>[!example]- Eksempel på Procedure af Kasper
>![[lektion8-kasper.pdf#page=1]]


---
#signalprocessing 

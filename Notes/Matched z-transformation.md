## Matched z-transformation
See [[lektion 8 - Introduktion til IIR filtre.pdf#page=11|slides]].

Poler og nulpunkter overføres direkte til z-domænet med formlen:
$$z = e^{sT}$$
![[Pasted image 20231102085545.png|300]]

## Procedure
1. Find poler og nulpunkter
2. Find [[Filters#Frekvensnormering|normerede]] poler og nulpunkter
3. Overfør poler og nul-punkter til z-domæne
$$z=e^{sT}$$
4. Opskriv overføringsfunktionen og gang en konstant på.
5. Find konstanten med ligningen:
$$H(s)|_{s=0} = H(z)|_{z=1}$$
6. Opskriv den endelige løsning

>[!example]- Eksempel på Procedure
>![[Lessons/Semester 3/signalbehandling/Exercises/lektion8.pdf|lektion8#page=1]]

>[!example]- Eksempel på Procedure af Kasper
>![[lektion8-kasper.pdf#page=1]]


---
#signalprocessing 
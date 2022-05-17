# Skrå kast 
I et skråt kast bevæger projektilet sig som udgangspunkt i en [[Andengradspolynomier|parabelformet]] bue.

## Position som Funktion af Tid
![|500](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fdetskraakast.weebly.com%2Fuploads%2F9%2F6%2F4%2F1%2F9641803%2F3182464_orig.png&f=1&nofb=1)

#### Uafhængighedsprincippet
Man kan beskrive projektilets bevægelse i x- og y-retningen uafhængigt af hinanden, og lægge dem sammen til sidst for at så den totale bevægelse i to dimmensioner.

#### x-retninen
Det er ingen kræfter der påvirker projektilet i x-retningen, og da vi ved fra [[Newtons Love#Newtons 1 lov Inertiens Lov|Newtons 1. lov]], så vil et legme der ikke påvirkes af en kraft bevare sin hastighed. Derfor må dette være en funktion for projektilets acceleration i x-retningen.

$$a_x(t) = 0$$

Ved at [[Integralregning|integrere]] kan vi gå fra en funktionene for acceleration til en funktion for hastighed i x-retningen. Bruger [[Integraler Regneregler|regneregler]].

$$v_x(t) = \int a_x(t)\,dt = v_{0x}$$

Når man integrerer $0$ bliver det bare til en konstant $k$. Denne konstant er i dette tilfælge starthastigheden i x-retningen.

Vi kan nu integrere for at finde en funktion for sted i x-retningen

$$s_x(t)=\int v_x(t)\,dt = \iint a_x(t)\,dt = v_{0x}t + s_{0x}$$

Denne gang er konstanten bagerst startposition i x-retningen

#### y-retninen
I y-retningen bliver projektilet påvirket af [[Tyngdekraften|tyngtekraften]]. (op er positiv)

$$a_y(t) = -9.8\frac{m}{s^2}$$

Vi integrerer

$$v_y = \int a_y(t)\,dt = -9.8\frac{m}{s^2} t + v_{0y}$$

Vi integrerer igen

$$s_y(t) = \int v_y(t) = \iint a_y(t)\,dt = -9.8 \frac{m}{s^2} \frac{t^2}{2}  + v_{0y}t + s_{0y} = -4.9 \frac{m}{s^2} t^2  + v_{0y}t + s_{0y}$$

Nu har vi funktioner for positionen, [[Hastighed og Fart|hastigheden]] og accelerationen i y-retningen over tid

## Y som Funktion af X
#todo













---
##### Tags
#fysik 
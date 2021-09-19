Formålet med forsøgene er at undersøge stående bølger i åbne- og
halvåbne resonansrør (blæseinstrumenter).

+-----------------------------------------------------------------------+
| **Opgaver før forsøget\                                               |
| **                                                                    |
+=======================================================================+
| I en orgelpibe sætter man luften inde i piben i svingning ved at      |
| blæse en luft­strøm gennem en åbning i den ene ende - luften svinger  |
| frit i denne ende.                                                    |
|                                                                       |
| +--------------------------------------+--------------------------+   |
*der var et billede her engang*
| | e1.emf){width="3.1979166666666665in" | mage3.emf){width="2.0in" |   |
| | height="0.5in"}                      | height                   |   |
| |                                      | ="0.5208333333333334in"} |   |
| | Åben orgelpibe                       |                          |   |
| |                                      | Lukket orgelpibe         |   |
*der var et billede her engang*
*der var et billede her engang*
| +======================================+==========================+   |
| +--------------------------------------+--------------------------+   |
|                                                                       |
| **Opgave a:**                                                         |
|                                                                       |
| For et "rør", der er åbent eller lukket i begge ender (fx en åben     |
| orgelpibe), er der resonans for følgende bølgelængder                 |
*der var et billede her engang*
*der var et billede her engang*
| *n* er ordenen (grundtone, 1. overtone, 2. overtone, osv....)         |
|                                                                       |
| Begrund formlen ved at undersøge gyldigheden for *n* = 1, 2 og 3      |
| (tegn, idet knuder angives med • og buge med = ):                     |
|                                                                       |
|   -----------------------------------                                 |
| --------------------------------------------------------------------- |
|                                                                       |
|                ***n***   ***L***                 $$\mathbf{\lambda}$$ |
|   ------- ---------------------------                                 |
| ------ ---- --------- ----------------------- ----------------------- |
|   **=**   • **=**                                                     |
*der var et billede her engang*
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
|                                              (Udfyld)                 |
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
|   -----------------------------------                                 |
| --------------------------------------------------------------------- |
|                                                                       |
| **Opgave B:**                                                         |
|                                                                       |
| For et halvåbent "rør" (fx en lukket orgelpibe) er der resonans for   |
*der var et billede her engang*
| (2) $L = n \cdot \frac{\lambda}{2} - \frac{\lambda}{4}$, hvor *L* ca. |
| svarer til rørets længde, og *n* er ordenen (grundtone, 1. overtone,  |
| 2. overtone, osv....)                                                 |
|                                                                       |
| Begrund formlen ved at undersøge gyldigheden for *n* = 1, 2 og 3      |
| (tegn igen):                                                          |
|                                                                       |
|   -----------------------------------                                 |
| --------------------------------------------------------------------- |
|                                                                       |
|                ***n***   ***L***                 $$\mathbf{\lambda}$$ |
|   ------- ---------------------------                                 |
| ----- ---- --------- ----------------------- ------------------------ |
|   **=**   •                                                           |
*der var et billede her engang*
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
|                                              (Udfyld)                 |
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
|   -----------------------------------                                 |
| --------------------------------------------------------------------- |
|                                                                       |
| Hvilken type pibe (åben eller lukket) giver den dybeste tone?         |
|                                                                       |
| **Opgave C:**                                                         |
|                                                                       |
| Find et udtryk for resonansfrekvenserne for de to typer af resonanser |
| (1) og (2), og vis herved, at der bliver en lineær sammenhæng mellem  |
| frekvenserne *f* og ordenen *n*. Vis også, at der gælder følgende     |
| forhold mellem grundtonens og overtonernes frekvenser:                |
|                                                                       |
*der var et billede her engang*
|                                                                       |
*der var et billede her engang*
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Eksperiment**                                                       |
+=======================================================================+
| **\                                                                   |
| **                                                                    |
|                                                                       |
| Vi kan simulere et blæseinstrument ved hjælp af et rør. Røret kan     |
| være enten åbent i begge ender, lukket i begge ender eller åbent i    |
| den ene ende og lukket i den anden ende.                              |
|                                                                       |
| **[Halvt åbent rør]{.ul}** (tilfælde B): Vælg måleperiode til 2       |
| sekunder og start ved triggering.                                     |
|                                                                       |
*der var et billede her engang*
| > height="1.4791666666666667in"}                                      |
|                                                                       |
| Mikrofonen anbringes i et stativ, og når der slås på røret, holdes    |
| rørets anden ende tæt på mikrofonen. Pas på, at I ikke rammer         |
| mikrofonen med røret.                                                 |
|                                                                       |
| -   Mål lyden fra røret ved gentagne gange at slå på røret, så der    |
|     måles på flere slag, gerne 4-6 slag i løbet af de 2 sekunder.     |
|                                                                       |
| -   Lav en FFT-analyse ved at trykke "Insert Additional Graphs FFT    |
|     Graph".                                                           |
|                                                                       |
| -   Frekvensen findes nu ved at tilføje "Gaussian"-regression ved at  |
|     trykke på "Curve Fit" og scrolle ned.                             |
|                                                                       |
| -   B-værdien angiver nu frekvensen, som sammenlignes med (4).        |
|                                                                       |
|   --------------------------------------                              |
| --------------------------------------------------------------------- |
*der var et billede her engang*
*der var et billede her engang*
|   height="1.57291                                                     |
| 66666666667in"}                        height="1.5833333333333333in"} |
|   --------------------------------------                              |
| --------------- ----------------------------------------------------- |
*der var et billede her engang*
|   height="1.5729166666666667in"}                                      |
|                                                                       |
|   --------------------------------------                              |
| --------------------------------------------------------------------- |
|                                                                       |
| Gentag forsøget med et rør af en anden længde.                        |
|                                                                       |
| Indfør resultaterne i skemaet på næste side (husk at måle rørenes     |
| længde).                                                              |
|                                                                       |
|   --------------------------------------------                        |
| --------------------------------------------------------------------- |
*der var et billede her engang*
*der var et billede her engang*
|                 Hz                                                    |
|                  Hz                       Hz                       Hz |
|   ------------- ------------------------ -----                        |
| ------------------- ------------------------ ------------------------ |
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
|   --------------------------------------------                        |
| --------------------------------------------------------------------- |
|                                                                       |
| **[Åbent rør]{.ul}** (tilfælde A): Som ovenfor, men lyden frembringes |
| ved at blæse på tværs af rørets åbning.                               |
|                                                                       |
|   --------------------------------------------                        |
| --------------------------------------------------------------------- |
*der var et billede her engang*
*der var et billede her engang*
|                 Hz                                                    |
|                  Hz                       Hz                       Hz |
|   ------------- ------------------------ -----                        |
| ------------------- ------------------------ ------------------------ |
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
|   --------------------------------------------                        |
| --------------------------------------------------------------------- |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Efterbehandling eksperimenter**                                     |
+=======================================================================+
| -   Hvordan passer jeres resultater med teorien?                      |
|                                                                       |
| -   Kommenter usikkerhed og fejlkilder                                |
|                                                                       |
| -   Perspektiver til instrumenter og toneskala.                       |
+-----------------------------------------------------------------------+

Journalen skrives til jer selv, og kan indgå i en evt. eksamen.

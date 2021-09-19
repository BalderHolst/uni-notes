  -----------------------------------------------------------------------
  Begreb            Forklaring
  ----------------- -----------------------------------------------------
  Graf              En *graf* G består af to mængder: En mængde af
                    hjørner og en mængde af kanter.

  Delgraf           En *delgraf* af en graf G består af nogle af
                    hjørnerne i G og nogle af kanterne mellem de udvalgte
                    hjørner i G.

  Hjørner           Punkter/destinationer

  Kanter            forbindelser mellem *hjørner*

  Lykker            an *kant* der startder og slutter i samme hjørne

  Dobbelkanter      to *kanter* mellen de samme to hjørner

  Vandring          en sekvens af *hjørner*, der er forbundet af kanter.

  Tur               en *vandring*, der består af *kanter*, der hver kun
                    kan være med én gang

  Sti               en *tur*, hvor samme hjørne ikke besøges flere gange

  Kreds             En *kreds* er en *tur*, der starter og slutter i det
                    samme *hjørne*, mens de andre *hjørner* er
                    forskellige.

  Grad              Antallet af *kanter*, som udgår fra et *hjørne*

  Eulertur          en *tur*, som gennemløber alle *kanter* i *grafen*

  Lukket Eulertur   *Eulertur*, som starter og slutter samme sted

  Eulergraf         En graf der har en *lukket Eulertur*

  Træ               en sammenhængende *graf* eller *delgraf* uden
                    *kredse*.

  Udspændende Træ   et *træ*, hvor alle hjørnerne i grafen er en del af
                    *træet*.

  Vægtede grafter   En *graf* med værdier på kanterne

  Prims Algoritme   En algoritme der finder det minimale *udspændende
                    træ*

  A                 

  A                 

  A                 
  -----------------------------------------------------------------------

# Eulerture og Grader

Dette er grafen:

*der var et billede her engang*
height="1.1644313210848645in"}

Det er ikke muligt finde en tur det går gennem alle punkterne på grafen
(en Eulertur). Dette er fordi der er mere end to punker med ulige
grader. Både E, F, B og A har ullige grader. For at gøre det muligt, kan
vi slette en kant, så to af punkterne med ulige grader, får lige grader.
Dette kan gøres ved at fjerne en af disse kanter.

*der var et billede her engang*
height="1.173555336832896in"}

Hvis en af disse kanter fjernes, kan man altid tegne en tur der starter
og slutter i de to punkter med ullige grad.

**Dvs.**

[Hviset hjørne har en ullige grad, skal hjørnet være enten star- eller
sluthjørnet i en Eulertur. Hvis Eulerturen starter i et hjørne med en
lige grad, skal den også slutte der]{.ul}

# Udspændende træer

Antallet af kanter i et udspændende træ kan beskrives med formlen *H -*
1, hvor *H* er antallet af hjørner i træet.

# Tabeller og Grafer

Tabeller viser de forbundende hjørner med x'er. Kun halfdelen af
tabellen er udfyldt, da den ville være synetrisk.

*der var et billede her engang*
height="1.7083333333333333in"}

Vægtede grafer kan også opskrives i et skema på følgende måde

*der var et billede her engang*
height="1.7426301399825022in"}

# Prims Algoritme 

Man finder et hjørne at starte på. Herefter udføre man følgende punkter
til alle hjønerne er forbundet.

1.  Find delgrafens mindst vægtede kant til et nyt hjørne, der ikke
    allerede er en del af delgrafen.

2.  Tilføj den nye kant og punkt til delgrafen

3.  Repeat

*der var et billede her engang*

En lille sandhed: " et minimale udspændende træ, som man finder ved
Prims algoritme, afhænger ikke af, hvilket hjørne i grafen algoritmen
startes i."

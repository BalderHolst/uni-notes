**[OPTIMERING.]{.ul}**

*Kartoner til f.eks. mælkeprodukter kan have forskellig form. Dåser har
forskelligt forhold mellem radius og højden (tænk på majs, tun og
Cult).*

*I begge tilfælde kunne det være interessant at vide, hvilken form der
er optimal i den forstand, at den bruger **mindst** mulig emballage i
forhold til volumen.*

*Har man 100 meter hegn, vil det indesluttede areal afhænge af den form
man laver indhegningen i. Hvilken form giver **størst** areal?*

***Emnet "optimering"** går netop ud på, at finde ud af hvornår noget er
optimalt, det være sig mindst muligt eller størst muligt.*

***Her kommer differentialregning ind i billedet!***

I de følgende opgaver bliver I guidet frem til en forståelse af, hvordan
man griber sådanne opgaver an.

**[OPLÆG:]{.ul}** Gårdmand Bjørn har 200 meter hegn og vil lave en
rektangulær indhegning. Han vil gerne have indhegningen så stor som
mulig.

Vi starter med at lave en skitse af situationen og vi kalder siderne for
f.eks x og y:

*der var et billede her engang*
height="2.316666666666667in"}

Da der slet ikke er nogen indhegning hvis x = 0 eller x =100, **må der
gælde: 0 \< x \< 100.**

(Naturligvis kan man argumentere for, at indhegningen mindst skal være
bred nok til et dyr (!), men det vil vi se bort fra i den matematiske
behandling).

To vigtige ting er i spil: Omkredsen O og Arealet A:

Omkredsen: Vi må have, at O = 2x +2y. Da der var 200 m hegn, må der
gælde at **Omkreds:** **200 = 2x + 2y.**

Arealet A må være **A = x^.^y , 0 \< x \< 100**.

***Ideén*** er nu, at vi vil lave A til en funktion kun af x, hvor vi så
kan finde dens maksimum vha. differentialregning. ***Derfor*** isolerer
vi y i formlen for omkreds og indsætter i formlen for A:

Omkreds: 200 = 2x + 2y 200 -2x = 2y $y = \ \frac{200 - 2x}{2}$ **y = 100
-x.**

Dette indsættes så i stedet for y i formlen for A:

A = x^.^(100 - x) **A(x) = 100^.^x- x^2^** , **Dm(A) = \]0 ; 100 \[**

**Da A således kun afhænger af x, kan vi skrive A(x) (altså areal som
funktion af x).**

Vi kan nu finde monotoniforholdene for A ved at differentiere: A'(x)
=100 - 2x.

Dvs. A'(x) = 0 **[x = 50]{.ul}**

Blot fordi A'(x) = 0 er vi ikke i mål: Der kunne være minimum eller
vendetangent, så vi skal **vise** at det **ER** maksimum ved at finde
monotoniforholdene**:**

Vi finder en tal på hver side af 50, og HUSKER ikke at komme under 0
eller over 100 (det er jo udenfor definitionsmængden!):

A'(25) = 100 - 2^.^25 = 50 (+), A'(75) = 100 - 2^.^75 = -50 (-).

Monotoniforholdene bliver altså:

***[i.d:]{.ul}** Står for "Ikke Defineret".*

**[KONKLUSION:]{.ul}** Det ses altså at der **er** maksimum for **x =
50** og dermed også y = 100 -50 = 50. **Gårdmand Bjørn får altså størst
areal ved at vælge x = y = 50 m, dvs. et kvadrat! Det samlede areal
bliver x^.^y = 50 m ^.^50 m = [2500 m^2^]{.ul}**

(Kunne også være udregnet udfra areal-funktionen A(50) = 100^.^50 -50^2^
= [2500 m^2^]{.ul} ).

Dvs. han skal vælge en KVADRATISK indhegning!

**[NOTE:]{.ul}** Nu kræves der en rektangulær indhegning. Ellers er en
*cirkel* det der giver størst indesluttede areal med en given omkreds:

200 = 2π^.^r => r = $\frac{200}{2\pi}\ \  \approx 31,83$ Det giver et
areal på A = π^.^r^2^ **[= 3183,1 m^2^.]{.ul}**

Men nu er en cirkel jo ikke på tale i opgaven .

**[TIL DE EFTERFØLGENDE OPGAVER SKAL DER SOM UDGANGSPUNKT IKKE BENYTTES
CAS (WordMat eller Maple). PRØV I STEDET AT KOMME SÅ LANGT SOM MULIGT
UDEN, OG BRUG FØRST CAS NÅR DU GÅR I STÅ.]{.ul}**

[OPGAVE 1.]{.ul} Gårdmand Bjørn har igen 200 m hegn, men denne gang vil
han lave indhegningen langs væggen af en lade, dvs. den ene af y-siderne
oven over bliver erstattet af en væg.

Igen vil han finde en rektangulær indhegning.

a)  Lav en tegning som i eksemplet, hvor den ene y-side er blevet til en
    væg (tegn en tyk streg).

b)  Gør rede for at 0 \< x \< 100. Gør rede for at 200 m = 2x + y og gør
    rede for at A = x^.^y

c)  Isolér y i formlen 200 = 2x +y og indsæt det på y's plads i formlen
    for A. **Det skulle gerne ende med funktionen A(x) = 200x - 2x^2^**

d)  Løs nu A'(x) = 0 og lav monotonilinie som ovenfor.

e)  **Gør rede for, at det ER et maksimum du har fundet. Hvad er x og y
    her?**

[OPGAVE 2.]{.ul} En åben kasse uden låg skal have kvadratisk bund og
rumfanget 3000 cm^3^. Hvordan skal kassen dimensioneres (dvs. find x og
h) så overfladen bliver **mindst** mulig.

a)  Prøv at lave en tegning.

Gør rede for at rumfanget er: V = x^2.^h (dvs. 3000 = x^2^h) og at
overfladen er A = x^2^ + 4xh.

b)  Det er Overflade vi skal have fat i, så isolér h i V-formlen og
    indsæt det på h's plads i A.

(Du skulle gerne nå frem til h =3000/x^2^ og A(x) = x^2^ + 12000/x ).

c)  Gør rede for, at Dm(A) = \]0 ; ∞ \[ (Igen: Vi er matematisk set
    ligeglade med, om kassen bliver så flad eller smal, at der
    overhovedet ikke kan være noget i den....)

d)  Find nu monotoniforholdene for A ved at differentiere og sætte A'(x)
    = 0. Lav så en figur som i eksemplet med Gårdmand Bjørn (HUSK at den
    er i.d. op til og med 0).

e)  **Gør rede for at det ER et minimum du har fundet og angiv x og h.**

[OPGAVE 3.]{.ul} **Gårdmand Bjørn igen!**

Denne gang har han igen 200 m hegn og vil lave en rektangulær indhegning
langs en væg som som i opgave 1. Denne gang skal der være plads til en
10 m bred åbning, der skal være modsat væggen.

Han vil finde x og y, så arealet A igen bliver **størst** muligt.

a)  Gør rede for, at Omkreds denne gang giver ligningen 200 = 2x +
    y- 10.

b)  Gør nu de samme overvejelser og beregninger som i opgave 1.

c)  Hvilke dimensioner skal x og y have, for at arealet denne gang er
    **størst** mulig?

[OPGAVE 4.]{.ul} **(Skotøjsæske?)**

En æske uden låg skal være dobbelt så lang som den er bred. Den skal
rumme 4 liter.

Æsken skal dimensioneres, så overfladen A er **mindst** mulig.

a)  Lav en skitse som i opgave 2.

b)  Gør nu det samme som i opgave 2, blot med de andre tal i denne
    opgave.

c)  Hvilke dimensioner skal x og h have, for at overfladen er **mindst**
    mulig?

[OPGAVE 5.]{.ul}

Løs følgende opgave.

*der var et billede her engang*
height="2.0506944444444444in"}

**[TIL DE EFTERFØLGENDE OPGAVER SKAL DER BENYTTES CAS (WordMat eller
Maple):]{.ul}**

*Når du bruger CAS-værktøjer og skal genbruge lange udtryk, så gør
flittigt brug af Copy-Paste, i stedet for at skrive en lang smøre igen:
det mindsker også risikoen for fejlindtastning.*

[OPGAVE 6.]{.ul} Besvar følgende opgave ved hjælp af CAS-værktøj:

*der var et billede her engang*
height="2.7424037620297463in"}

1)  Brug CAS til at isolere h i formlen for V og indsæt dette udtryk på
    h's plads i formlen for A. Herved fås A som funktion af r, dvs.
    A(r).

2)  Der **skal** redegøres for, at der er minimum:

```{=html}
<!-- -->
```
a)  Brug derfor CAS til at finde A'(r)

b)  benyt CAS til at løse A'(r) = 0

> Lav nu **enten** et fortegnskema for A'(r) **eller** tegn grafen for
> A(r) og **se** at der er et minimum for det r der blev fundet i 2 b).

[OPGAVE 7.]{.ul} Besvar følgende opgave:

*der var et billede her engang*

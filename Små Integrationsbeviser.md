# Små Integrationsbeviser              
Her er beviser for de følgende regneregler: $\int k \cdot f(x)\, dx = k \cdot \int f(x)\, dx$ , $\int f(x)+g(x)\,dx = \int f(x)\,dx + \int g(x)\,dx$, og ideen om at en given funktion ($f(x)$) har flere stamfunktioner (($F(x)$)).


### Bevis at $f(x)$ har to forskellige stamfunktioner: $F_1(x)$ og $F_2(x)$.

$$\int f(x)\,dx = F_1(x) + k = F_2(x) + k$$

Dette skal være sandt hvis begge funktioner er stamfunktioner, da de begge er ens

$$F_1(x) = F_2(x) \Longleftrightarrow F_1(x) - F_2(x) = 0$$


==Da $(k)' = 0$ må dette være sandt== #spørgmike


$$F_1(x) - F_2(x) = k$$


Vi kan ku omskrive udtrykket til

$$F_1(x) = F_2(x) + k$$


Altså er vores bevis gennemført
 
---

### Bevis for ligningen $\int k \cdot f(x)\, dx = k \cdot \int f(x)\, dx$

I dette bevis gør vi brug af [[Integrationsprøven]]

Vi differenciere

$$(\int k \cdot f(x)\, dx)' = (k \cdot\int f(x)\, dx)'$$

Vi lader differentialet opløse integrales på venstre side og lader $k$ stå uden for differentialet #spørgmike 

$$k \cdot f(x)\, dx = k \cdot (\int f(x)\, dx)'$$

Vi kan nu lade det sidste integrale gå ud med differentialet

$$k \cdot f(x)\, dx = k \cdot f(x)\, dx$$

done

---

### Bevis for udtrykket $\int f(x)+g(x)\,dx = \int f(x)\,dx + \int g(x)\,dx$

Vi [[Differentialregning|differentierer]] det HELE
$$(\int f(x)+g(x)\,dx)' = (\int f(x)\,dx + \int g(x)\,dx)'$$

Bruger [[Differentialregning Regneregler]]

$$(\int f(x)+g(x)\,dx)' = (\int f(x)\,dx)' + (\int g(x)\,dx)'$$

Nu går alle integralerne ud med mærkerne

$$f(x)+g(x) = f(x) + g(x)$$








---
##### Tags
#matematik 
#bevis
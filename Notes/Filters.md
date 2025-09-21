# Filters
[[Lektion 1 - Filterfunktioner.pdf]]

### Filter Types

>[!example]- Ideal filters
>![[Filters-Filter-Types.png|Pasted image 20230914082441.png]]

We want three things from a filter:
1. *Constant amplification* on the pass band
2. Lots of *dampening after cutoff* frequency
3. **Linear phase*** (see [[#Delay through filter (gruppeløstid)]])

##### Actual filter types
These all only have poles no zero points.

- [[Butterworth Filter]]
- [[Chebyshev Filter]]
- [[Bessel]] (More linear phase)

Plots of the three filters
![[Filters-Actual-filter-types.png|250]]

[[Laplace Transformation#Poles|Poles]] of the filters.
![[Filters-Actual-filter-types-1.png|250]]
**Note:** [[Butterworth Filter|Butterworth]] lies on a circle around $(0, 0)$, with a radius of $j\omega_{a}$.
### Frekvensnormering
Normering: $s \rightarrow s \cdot  \omega_{a}$.
Denormering: $s \rightarrow \frac{s}{\omega_{a}}$.

Used for determining the order of the filter needed (form factor).
$$F = \frac{\omega_{s}}{\omega_{a}}$$
$\omega_{s}$: Stop band frequency
$\omega_{a}$: Cutoff frequency
The result it the $x$-axis on a plot like this:
![[Filters-Frekvensnormering.png|250]]
You select the lowest order, that adheres to the specification, as higher order filter, are more complicated.

### Filter Order ($N$)
Poles = $-20 \frac{\text{db}}{\text{dec}} \cdot N$
Zeros = $+20 \frac{\text{db}}{\text{dec}} \cdot N$

**First order** filter ($k$ and $a$ are constants):
$$H_{1} = \frac{k}{s+a}$$
A **second order** filter could be written like this:
$$H_{2} = \frac{k}{(s+a)(s+b)}$$
You can also multiply filters together to create higher order filters:
$$H_{1} \cdot H_{1} = \frac{k^{2}}{(s+a)^2}$$
In practice this is the same at *putting the filters after each other*.

### Delay through filter (gruppeløstid)
The *delay of different frequencies is different*. We can try to mitigate this in our filter.

The delay can be found as the derivative of phase as a function of frequency $\phi(\omega)$.
$$T_{g} = -\frac{d\phi(\omega)}{d\omega} \s [\text{s}]$$
Because of this we want *linear phase*:
![[Pasted image 20230914085305.png|350]]
![[Pasted image 20230914085353.png|350]]

If not, the [[Step Response]] will ocilate:
![[Pasted image 20230914085447.png|350]]
![[Pasted image 20230914085503.png|350]]

---
#signals #signalprocessing

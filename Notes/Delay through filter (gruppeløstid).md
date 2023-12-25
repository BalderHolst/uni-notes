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
# Rotation

---

- [[Inertimoment]]
- [[Kraftmoment]]

---

$$\theta(t)$$

### Øjeblikkelig vinkelhastighed
$$\vec{\omega} = \frac{d \theta(t)}{dt} \hat{\omega}$$
$\hat{\omega}$ : Enhedsvektor (Peger "op" ad tommelfingeren med højrehåndsmetoden)

### Konstant vinkelhastighed
$$\theta(t) = \theta_{0} + \omega_{0} \cdot t$$

### Vinkelacceleration
$$\vec{\alpha} = \frac{d \omega(t)}{dt} \cdot \hat{\omega} = \frac{d^{2} \theta}{dt^{2}} \cdot \hat\omega$$

[[De kinematiske ligninger]] kan også anvendes til rotation. ([[Lektion 09-FYS__RT_E22.pdf#page=3|slide]]) #TODO
$$
\begin{align}
\omega(t) &= \omega_{0} + \alpha t \\
\theta(t) &= \theta_{0} + \omega_{0}t + \frac{1}{2}\alpha t^{2} \\
\omega^{2} &= \omega...
\end{align}
$$
### Position, Hastighed og Acceleration

##### Sted
$$s=r\theta$$
##### Hastighed
$$v = \frac{ds}{dt} = r \frac{d\theta}{dt} = r\omega$$
##### Acceleration

Tangentacceleration (I bevægelsesretningen)
$$\vec{a_{t}} = \frac{dv}{dt} = \frac{d}{dt}(\omega r) = \frac{d\omega}{dt}r=\alpha r$$

Radialacceleration/Centripetalaccelerationen (Mod omdrejningspunktet)
$$\vec{a_{r}}= \frac{v^{2}}{r} = \omega^{2}r$$

Den *totale* acceleration
$$\vec{a_{total}} = \vec{a_{r}}+ \vec{a_t}$$

### Rotationsenergi
Et objekts [[Kinetisk Energi|kinetiske energi]] i cirkelbevægelse.

$$K= \frac{1}{2} \cdot I \cdot \omega^2$$
$I$ : [[Inertimoment]]

##### Rotationsarbejde ([[Lektion 09-FYS__RT_E22.pdf#page=19]])
$$\Delta K = K_{f}- K_{i}$$

$$W = \int_{\theta_{i}}^{\theta_{f}} \vec{\tau} \cdot d\vec{\theta}$$


>[!Note]- Udledning
>$$K = \frac{1}{2} \cdot m \cdot  v^{2} \s \text{og} \s v = r\omega$$
>$$\Downarrow$$
>$$K= \frac{1}{2} \cdot m r^{2}\omega^{2} =\frac{1}{2} \cdot I \cdot \omega^{2}$$


---
#fysik 
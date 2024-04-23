# Common Mode Rejection Ratio
How good a differential amplifier is at rejecting noise when the impedance on its inputs is the same.

Common mode = average of inputs

$$CMRR \to \infty \Rightarrow A_{cm} \to 0$$

$$
CMRR = 20 \log\left( \frac{|A_d|}{|A_{cm}|} \right)
$$

With a CMRR at 90 dB the amplifier is 31866 times better at amplifying the difference as opposed to the noise.

#### Inverting Op-amp
Add a voltage source on the positive input of an *ideal* op amp with a value of $\frac{V_{in}}{CMRR}$. This is equivalent to the error.


---
#forstærker
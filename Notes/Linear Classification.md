# Linear Classification
See [[lecture11a.pdf|slides]].

**Update Rule**:
$$
w_{i} \leftarrow w_{i} + \alpha (y-h_{w}(x)) \times x_{i}
$$
$\alpha$: Learning Rate
$y$: Correct value (label)
$h_{w}(x)$: Prediction


Reduce learning rate over time in non-deterministic cases.

### Logistic Regression
See [[lecture11a.pdf#page=6|slide]].

WAY better for **non-separable cases**.

Use logistic function as threshold function

$$
\mathrm{Logistic}(z) = \frac{1}{1+e^{-z}}
$$

This results in the following update equation

$$
w_{i} \leftarrow \alpha (y - h_{w}(x)) \times h_{w}(1-h_{w}(x)) \times x_{i}
$$

---
#intelligent-systems
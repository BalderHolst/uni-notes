# Binary Cross Entropy
Binary as $y$ is a binary class, $0$ or $1$.

$$
L = - \Big[
y \log(\hat{y}) + (1 - y) \log(1-\hat{y})
\Big]
$$

$\log$: Natural Logarithm ($\ln$)
$y$: Class ($0$ or $1$)

#### Total Sample Loss
$$
L = - \frac{1}{n} \sum \Big [
y_{i} \log(\hat{y}_{i}) + (1 - y_{i}) \log(1-\hat{y}_{i})
\big]
$$



---
#machine-learning
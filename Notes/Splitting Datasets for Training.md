# Splitting Datasets for Training
We *always* split our date into three buckets:
- Training Data (60%)
- Validation Data (20%)
- Testing Data (20%)

### Training
Establis parameters of the model

### Validation
Hyper parameters
Decission (threshold)

### Test
> "A seperate *holy* dataset"

Validation of the performance of your model.
Evalua tes the **final** output of the model.

##### Confusion Matrix
> [!warning] Dataset could be biased
> A "good" precision and recall does not nessecarilly mean that the model is good. The choice 

![[Basic-Confusion-matrix.webp]]

**Precision**
How many of the detected positives are *actual* ground truth positives.
$$
\mathrm{Precision} = \frac{TP}{TP + FP}
$$
**Recall**
$$
\mathrm{Recall} = \frac{TP}{TP + FN}
$$

**F1 Score**
The balance of precision and recal. Closer to 1, the better.
$$
\mathrm{F1} = \frac{2}{\frac{1}{\mathrm{Precision}} + \frac{1}{\mathrm{Recall}}}
$$

---
#machine-learning

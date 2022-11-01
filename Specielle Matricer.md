# Specielle Matricer
Se [[Matricer]].

### Diagonalmatrix
**Kvadratisk** matrix med nuller pånær diagonalen.
$$
\text{diag}(d_{1},d_{2},\dots,d_{n}) =\left(
\begin{array}{cccc}
 d_1 & 0 & \dots & 0 \\
 0 & d_2 & \dots & 0 \\
 \vdots & \vdots & \ddots & 0 \\
 0 & 0 & 0 & d_n \\
\end{array}
\right)
$$


### Identitetsmartix
**Kvadratisk** matrix fyldt med *nuller*. I diagonalen er den dog $1$. 

En identitetsmatrix er også en [[#diagonalmatrix]].
$$
I_{4\times4} =\left(
\begin{array}{cccc}
 1 & 0 & 0 & 0 \\
 0 & 1 & 0 & 0 \\
 0 & 0 & 1 & 0 \\
 0 & 0 & 0 & 1 \\
\end{array}
\right)
$$

##### Egenskab
$A$ er en matrix og $I$ er en identitetsmartix. Begge er **samme størrelse**.
$$A \cdot I = I \cdot  A = A$$

### Symetriske og Antisymetriske Matricer

##### Symetrisk
$$a_{jk}=a_{kj} \s A^{T} = A$$
>[!Example]- Eksempel
>$$
>\left(
\begin{array}{ccc}
 1 & 3 & -2 \\
 3 & 2 & 5 \\
 -2 & 5 & -1 \\
\end{array}
\right)
$$


##### Antisymetrisk
$$a_{jk}=-a_{kj} \s A^{T} = -A$$
>[!Example]- Eksempel
>$$
>\left(
\begin{array}{ccc}
 1 & 3 & -2 \\
 -3 & 2 & 5 \\
 2 & -5 & -1 \\
\end{array}
\right)
$$

---
#matematik 
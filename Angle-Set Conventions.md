# Angle-Set Conventions
Ways to rotate around an axis with [[Rotational Matrices|rotational matrices]].

---

### Summary
[[#Fixed Angles]]
$$
R_Z(45\deg) \cdot \, ^\text{Base}_\text{TCP}R \Rightarrow \text{Rotate toolhead } 45 \deg \text{round the \textit{base} z-axis}
$$

[[#Euler Angles]]
$$
^\text{Base}_\text{TCP}R \cdot R_Z(45\deg)  \Rightarrow \text{Rotate  toolhead } 45 \deg \text{round the \textit{toolhead} z-axis}
$$

---


## Fixed Angles
The coordinate system stays fixed.

![[Pasted image 20230307091344.png]]

#### [[Rotational Matrices]]
Here we **left-multiply** (from right to left) the rotational matrices.


---

## Euler Angles
> *"Each rotation is performed about an axis of the coordinate system from the last step"*
>\- Iñigo Iturrate

The coordinate system changes whenever you do a rotation.

![[Pasted image 20230307091035.png]]


#### [[Rotational Matrices]]
![[Pasted image 20230307091212.png]]


---
#kinematik 

# QQ-plot
QQ-plot er et plot der viser et datasæt, og hvor tæt de er på at være normalfordelt. 

![[QQ-plot.png]]
```ad-example # Admonition type. See below for a list of available types.
title:                  Maple kode
collapse:               # Create a collapsible admonition.


with(Gym):
X := [25.0, 25.1, 27.7, 25.8, 25.9, 21.7, 22.8, 28.9, 26.4, 22.4]:
QQplot(X)
```
---
## QQ-plot-resudualer

Residualer kan også være normalfordelte, hvilket er en god markør for [[Regressioner|regressionens]] tilnærmelse. Til dette laver man et QQ-plot over regressionens residualer.
![[QQ-plot-residualer.png]]
```ad-example # Admonition type. See below for a list of available types.
title:                  Maple kode
collapse:               # Create a collapsible admonition.

with(Gym):
res := residualer(data, LinReg);
residualQQplot(res, LinReg);
```

---
#matematik 
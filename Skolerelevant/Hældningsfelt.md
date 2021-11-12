# Hældningsfelt
En skabelon til løsningen af en differentialligning. 

>*"Et hældningsfelt består af linjeelementer. Linjeelementer er givet ved $(x_0,y_0,y_0')$"*
>\-Mike

En "pil" i et hældningsfelt, heddet et linjeelement.

### Maple

Definer helst konstanter

```maple
with(DEplot):
l := y'(t) = 0.05*y(t)*(50 - y(t));
DEplot(l, y(t), t = 0 .. 4, [y(2) = 25]);

```

![[Hældningsfelt i maple.png]]
![[Hældningsfelt i maple 2.png]]

---
#matematik 
# Hældningsfelt
En skabelon til løsningen af en differentialligning. 

>*"Et hældningsfelt består af linjeelementer. Linjeelementer er givet ved $(x_0,y_0,y_0')$"*
>\-Mike

En "pil" i et hældningsfelt, heddet et linjeelement.

### Maple


```maple
with(DEplot):
DEplot(D(y)(t) = k*y(t), y(t), t = 0 .. 20, [y(1) = 30])
```

![[Hældningsfelt i maple.png]]
![[Hældningsfelt i maple 2.png]]

---
#matematik 
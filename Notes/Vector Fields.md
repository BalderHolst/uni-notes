---
created: 2026-09-28
tags: [multivariablemath, subject]
---
# Vector Fields
A way of representing functions with $2$- or $3$-dimensional inputs and outputs.
![[Vector-Fields.png|center|400]]

The coordinate system is the input space and the output is shown as vectors from a subset of the infinite points in the input space.

### Conservative Fields
>*"When a scalar function can be converted into a vector field using a [[Gradient|gradient]]."*
>\- Cornelia's Notes

Any [[Line Integrals|line integral]] from point a to point be will always be the same.


$$\nabla f = \mathbf{F}$$
$f$: Potential function

See also this [online resource](https://mathinsight.org/conservative_vector_field_find_potential).

**Conditions for 3 Dimensions:**
$$
\begin{align}
\frac{\partial f_{1}}{\partial y} =  \frac{\partial f_{2}}{\partial x}, \\
\frac{\partial f_{1}}{\partial z} =  \frac{\partial f_{3}}{\partial x}, \\
\frac{\partial f_{2}}{\partial z} =  \frac{\partial f_{3}}{\partial y},
\end{align}
$$

**Conditions for 2 Dimensions:**
$$
\begin{align}
\frac{\partial f_{1}}{\partial y} =  \frac{\partial f_{2}}{\partial x}
\end{align}
$$

>[!video]- Explaination
>![](https://www.youtube.com/watch?v=76nzOtupeRc)

>[!example]- Examples
>- [[lektion6.pdf#page=1]]
>- [[lektion6.pdf#page=2]]
>- [[lektion6.pdf#page=3]]

## Notes
```base
views:
  - type: cards
    name: View
    filters:
      and:
        - file.tags.contains("vectorfields")
    order:
      - file.name
      - file.mtime
    sort:
      - property: file.mtime
        direction: DESC
    imageAspectRatio: 1.1
    cardSize: 210
  - type: table
    name: Table
    filters:
      and:
        - file.tags.contains("vectorfields")
    order:
      - file.name
      - file.ctime
      - file.mtime
    sort:
      - property: file.mtime
        direction: DESC
```

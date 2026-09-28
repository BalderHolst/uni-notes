---
created: 2026-09-28
tags: [subject]
---
# Numerical Methods
### Solving Linear Systems
Algorithms for solving a system of linear equations
$$
Ax = b
$$
They should be considered in the following order. Left most one has faster run time.

[[Cholesky Decomposition]] > [[LU Decomposition]] > [[Notes/Singular Value Decomposition|Singular Value Decomposition]]

```base
views:
  - type: cards
    name: View
    filters:
      and:
        - file.tags.contains("numerical-methods")
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
        - file.tags.contains("numerical-methods")
    order:
      - file.name
      - file.ctime
      - file.mtime
    sort:
      - property: file.mtime
        direction: DESC
```

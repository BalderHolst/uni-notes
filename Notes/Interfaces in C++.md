---
created: 2023-12-25
tags: [cpp]
---
# Interfaces in C++

A *purely virtual class* without variables. An Interface is an [[Abstract Classes in C++|abstract class]].

---

### Example

```cpp
class Creature {
    virtual get_info() =0; // Pure virtual
}
```

The `=0` makes the function a *pure virtual* function. This means that `get_info` does not have to be immediately initialized.


# Pointers
Holds an address of a variable.

The *reference operator* (`&`) is used to get a variable's address in memory.

See also [[Smart Pointers in C++|smart pointers]].

##### Declaration
```cpp
type * name;
```

Example:
```cpp 
// Creates  a points p that holds the address of var
int * p = &var;
```

>[!warning] 
>Pointers **should always point to something**.

## Dereference Operator
> *"What is the pointer pointing at?"*

```cpp
var = *pointer // Reads the data at the pointer location.
```

The dereference operator uses the pointer type (defined at pointer declaration) to interpret the memory.


---
#cpp

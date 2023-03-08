# Memory Management in C++


## Stack
Keeps track of function calls and variables in the called functions.

Uses the [[stack datastructure]].

## Heap
A memory resource that we can manually manipulate.

For this there are two keywords `new` and `delete`.

>[!warning]
>Variables **must be destroyed manually**.
>
>Be carefull with `delete a;` and `delete a[];`. *If the wrong one is used it is undefined behavior.*

```cpp
int *a = new int;
delete a;
```

```cpp
int *a new int[5000] // Allocate space for 5000 integers
delete a[];
```

Sizes of objects on the heap can be dynamically be allocated on the heap.

It is however always faster to assign memory size at compile time.

---
#cpp

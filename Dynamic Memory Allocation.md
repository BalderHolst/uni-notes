# Dynamic Memory Allocation

Allocate memory
```c
void* malloc(size_t size);
```
See also `calloc` (zero-initialize the memory).

Reallocate memory
```c
void* realloc(void *ptr, size_t size);
```

Free memory
```c
void free(void *ptr);
```

Allocate automatically freed memory (allocated at *stack* not heap)

```c
void* alloca(size_t size);;
```

Find end of heap
```c
void* sbrk(0);
```




---
#c

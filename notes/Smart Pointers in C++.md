# Smart Pointers in C++
Automatically deallocates memory on the heap, when no pointer points to it.

There are three types:
- `std::unique_ptr`
- `std::shared_ptr`
- `std::weak_ptr`

---

### Unique Pointers
Ensures that only *one* pointer, points to the shared. This is done by the compiler.

```cpp
#include <memory>
auto myPtr = std::make_unique<int>(); // C++ >= 14
std::unique_ptr<int> mtPtr(new int); // Older c++
```

### Shared Pointer
Keeps track of how many pointers point at some memory. Deallocates the memory when there are no pointers pointing to the memory.

```cpp
#include <memory>
auto myPtr = std::make_shared<int>(); // C++ >= 14
std::shared_ptr<int> mtPtr(new int); // Older c++
```

> [!warning] 
> This can result in circular references, that can make it impossible to free the memory. To get around this use a [[weak pointer]].

---
#cpp

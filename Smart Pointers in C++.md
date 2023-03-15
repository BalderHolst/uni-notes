# Smart Pointers in C++

There are three types:
- `std::unique_ptr`
- `std::shared_ptr`
- `std::weak_ptr`

---

### Unique Pointers

```cpp
#include <memory>
auto myPtr = std::make_unique<int>(); // C++ >= 14
std::unique_ptr<int> mtPtr(new int); // Older c++
```

---
#cpp

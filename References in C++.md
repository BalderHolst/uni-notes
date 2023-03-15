# References in C++
An "alias" for a variable. The memory is still released when the original variable goes out of scope.

```cpp
int i;
int& r = i;
r = 3;
std::cout << i << std::endl; // output: 3
```


---
#cpp

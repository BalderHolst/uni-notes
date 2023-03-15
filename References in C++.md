# References in C++
An "alias" for a variable. The memory is still released when the original variable goes out of scope.

If a reference references a variable that is out of scope, it becomes a "stale reference". Like dangling [[Pointers|pointers]] these "stale references" are usually unwanted.

```cpp
int i;
int& r = i;
r = 3;
std::cout << i << std::endl; // output: 3

```

---

## In Functions
References are a way of making sure you do not copy the variables into a function (useful with large variables). Instead, the function gets direct access to the original data. This also makes it *possible for the function to modify the original data*.
```cpp
// Pass variable by reference
void myFunc(int& var);

// Makes sure the variable is not modified by the function
void myFunc(const int& var); 
```

## In Classes
References are nice as an alternative to classic getters, as they can provide direct access to a private variable, without the ugly pointer syntax.

---

## Differences with Pointers

---
#cpp

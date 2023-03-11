# The C++ Processor

The first part of a c++-file. All commands that interact with the processor are preceded by a '#'.


### Directives

#### Guards

Control flow in the preprocessor. These are mostly used in [[header files]].

>[!tip]
>If you run into errors like: "you have declared this twice", you probably need to guard its declaration.

```c++
#ifndef MY_VARIABLE
#define MY_VARIABLE

#include <import-one>
#include <import-two>
#include <import-three>
#include <import-four>

decrarations...

#endif
```


---
#cpp 

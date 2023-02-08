# Arrays in C++

### Old C-style Arrays
This is the C way of doing arrays.

**WARNING**: The length of the array must be known at compile time!
**WARNING**: Accessing an invalid index results in *undefined behavior*.

##### Allocate then Assign

```cpp
// Allocate memory for three integers. 
int myArray[3]; 

// We can set each value like this
myArray[0] = 0;
myArray[1] = 0;
myArray[2] = 0;
```

##### Assign and Allocate
```cpp
int myArray[] = {1, 2, 3, 4};
```

#### Lengh of Array
You *cannot get the length* of the array directly. 

You can however use the `sizeof(myArray)` function to find out how much memory is allocated.


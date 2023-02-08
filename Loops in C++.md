# Loops in C++

### For Loops
```cpp
for(int i=0; i<10; i++){
	// Run with i values rangeing from 0 to 9
}
```

```cpp
for (int i: {1, 2, 3}){
	// Run assigning i to each value in the list, one by one
}
```


### While Loops

```cpp
while(condition){
	// Run while condition is true
}
```

```cpp
do {
	// Run and keep running while condition is true
} while(condition);
```

## Break and Continue
**WARNING**: please be carefull with these, as they can greatly decrease code readability.

Break out of current loop/control flow.
```cpp
break;
```

Jump to next loop iteration
```cpp
continue;
```

---
#cpp
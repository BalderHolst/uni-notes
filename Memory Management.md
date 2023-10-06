# Memory Management

CPU generates logical addresses: Addresses starting from $0$. The OS the converts them into physical addresses, that point to the actual data in memory.

### Dynamic Loading
Only load parts of the executable when needed. This is useful for parts of your program that are rarely used (ex: Language translations). This is implemented by the programmer (pro tip: Use a library).

### Dynamic Linking (Shared Libraries)
Windows: `.dll`
Linux: `.so`

Link to a library at run time. This means that the same library can be used by multiple libraries. Linked libraries are loaded into a chunk of memory managed by the OS, so multiple processes can use them.

## Types of Memory Management

#### Contiguous Memory Management
All processes have *one chunk of memory*. This will however creates "holes" in memory as processes complete and their space is re-allocated. This results in small holes getting littered all over the system memory. This is called **fragmentation**.

External Fragmentation: Holes between different processes
##### Ways of assigning memory
- First-fit: Allocate the first hole where the process fits
- Best-fit: Allocate the smallest hole where the process fist
- Worst-fit: Allocate the largest hole for the process

##### Dividing into 
##### Compaction


---
#computerarkitecture
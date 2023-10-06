# Memory Management

CPU generates logical addresses: Addresses starting from $0$. The OS the converts them into physical addresses, that point to the actual data in memory.

### Dynamic Loading
Only load parts of the executable when needed. This is useful for parts of your program that are rarely used (ex: Language translations). This is implemented by the programmer (pro tip: Use a library).

### Dynamic Linking (Shared Libraries)
Windows: `.dll`
Linux: `.so`

Link to a library at run time. This means that the same library can be used by multiple libraries. Linked libraries are loaded into a chunk of memory managed by the OS, so multiple processes can use them.

## Types of Memory Management
*External Fragmentation*: Holes between different processes

One way of partly solving the problem of holes is **dividing the memory into blocks** with a fixed size. *The holes between blocks are called **internal fragmentation**.*

#### Contiguous Memory Management
All processes have *one chunk of memory*. This will however creates "holes" in memory as processes complete and their space is re-allocated. This results in small holes getting littered all over the system memory. This is called external **fragmentation**.
##### Ways of assigning memory
- First-fit: Allocate the first hole where the process fits
- Best-fit: Allocate the smallest hole where the process fist
- Worst-fit: Allocate the largest hole for the process

##### Compaction
*Move all processes* up or down to fill all holes, and create one large chunk of allocated memory. This is costly as a lot of data. It is therefore important to use a strategy that moves the least amount of data.

#### Paging
Physical memory is divided into **frames**.

Logical memory is divided into "pages". Each address contains two numbers: *page number and page offset*. A **page table** is used to translate into frame. *The offset stays the same*.

The page table is *process specific* and managed by the OS.

This only create internal fragmentation.
## Segmentation

A program consists of several pieces of memory
- Stack
- Main Program
- ...



---
#computerarkitecture
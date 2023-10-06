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

### Contiguous Memory Management
All processes have *one chunk of memory*. This will however creates "holes" in memory as processes complete and their space is re-allocated. This results in small holes getting littered all over the system memory. This is called external **fragmentation**.
##### Ways of assigning memory
- First-fit: Allocate the first hole where the process fits
- Best-fit: Allocate the smallest hole where the process fist
- Worst-fit: Allocate the largest hole for the process

##### Compaction
*Move all processes* up or down to fill all holes, and create one large chunk of allocated memory. This is costly as a lot of data. It is therefore important to use a strategy that moves the least amount of data.

### Paging
Physical memory is divided into **frames**.

Logical memory is divided into "pages". Each address contains two numbers: *page number and page offset*. A **page table** is used to translate into frame. *The offset stays the same*.

The page table is *process specific* and managed by the OS.

This only create internal fragmentation.

#### Translation Look-aside buffer (TLB)
A small page table held by the CPU (or very close to it), allowing to faster lookup of frequently used pages. The CPU will always look for a page here before the in-memory page table. It the page is found in the TLB, it is called a *TLB-hit*.

Page table is also stored in memory. This means that each time we want to access memory, we actual do it twice: Once for accessing the page table, and once to accessing the data.

Effective access time:
$$EAT = (t_{TLB} + t_{mem}) \alpha + (t_{TLB} + t_{mem} + t_{mem})(1- \alpha )$$
$\alpha$: The percentage of pages stored by CPU.
$t_{TLB}$: Time to lookup in the TLB.
$t_{mem}$: Time to access memory.

#### Protection
The page table can also contain the permissions for the frames.

#### Shared Pages
We only store one copy of a shared library, that can be accessed by different processes. Shared pages contain *read only memory*.

#### Hierarchical Page Table Structure
> *"We want to page a page table"*
>\- Mr. Teacher

Lookup tables can be layered to fill holes in memory with pages of the outer page table.

#### Hashed Page Table
Use a hash-table instead of page table. Entries in the hash table are linked lists.

The hash table is indexed by a hash of the logical pointer. Because more than one logical pointer be hashed to the same hash, the entries have to be a linked list. This list is searched to find the correct entry.

#### Inverted Page Table
Only **one page table in the system**.

Each entry contains the process id (pid) and the page held by the process (p).

Each time you want to find a frame you iterate over the page table and find $p$. The frame number is the index into of the entry containing $p$.

## Segmentation

A program consists of several pieces of memory
- Stack
- Main Program
- ...

## Swap
A loaded program can be "swapped" to memory to save space.


---
#computerarkitecture
# Libraries in C
This note is primarily generated by AI.

### 7.7 Relocation

Once the linker has completed the symbol resolution step, it proceeds to the relocation step, where it merges the input modules and assigns runtime addresses to each symbol. Relocation consists of two steps:

1. Relocating sections and symbol definitions: The linker merges all sections of the same type into a new aggregate section of the same type. Then, it assigns runtime memory addresses to the new aggregate sections, each section defined by the input modules, and each symbol defined by the input modules.
    
2. Relocating symbol references within sections: The linker modifies every symbol reference in the code and data sections to point to the correct runtime addresses. It relies on relocation entries in the relocatable object modules.

### 7.8 Executable Object Files

The result of the linking process is an executable object file, which contains all the information needed to load the program into memory and run it. A typical ELF executable file includes:

-   ELF header: Describes the overall format of the file and the entry point of the program.
-   Program header table: Describes how to map contiguous file sections to runtime memory segments.
-   Text, rodata, and data sections: Relocated to their eventual runtime memory addresses.
-   Init section: Defines a small function called _init that is called by the program's initialization code.

### 7.9 Loading Executable Object Files

To run an executable object file, we type its name to the Linux shell's command line. The shell invokes the loader, which copies the code and data in the executable object file from disk into memory and runs the program by jumping to its entry point. Every running Linux program has a runtime memory image that includes:

-   Code segment: Starts at address 0x400000 on Linux x86-64 systems.
-   Data segment: Follows the code segment.
-   Heap: Follows the data segment and grows upward.
-   Shared modules: Reserved for shared libraries.
-   Stack: Starts below the largest legal user address and grows down.
-   Kernel memory: Reserved for the code and data in the kernel.

### 7.10 Dynamic Linking with Shared Libraries

Shared libraries are object modules that can be loaded at an arbitrary memory address and linked with a program in memory at either runtime or load time. This process is known as dynamic linking and is performed by a dynamic linker. Shared libraries are indicated by the .so suffix on Linux systems. They are "shared" in two ways:

1.  A single .so file for a particular library is shared by all executable object files that reference the library.
2.  A single copy of the text section of a shared library in memory can be shared by different running processes.
    

### 7.11 Loading and Linking Shared Libraries from Applications

Applications can request the dynamic linker to load and link arbitrary shared libraries while the application is running, without having to link the applications against those libraries at compile time. This is done by using the dynamic linker's interface, which includes functions such as dlopen, dlsym, dlclose, and dlerror.

### 7.12 Position-Independent Code (PIC)

Position-independent code (PIC) is code that can be loaded anywhere in memory without having to be modified by the linker. Shared libraries must always be compiled with the -fpic option to GCC to generate PIC code. PIC references to global variables are implemented using the Global Offset Table (GOT), while PIC function calls are implemented using a combination of the GOT and the Procedure Linkage Table (PLT).

### 7.13 Library Interpositioning

Library interpositioning allows you to intercept calls to shared library functions and execute your own code instead. This can be done at compile time, link time, or runtime.

-   Compile-time interpositioning: Uses the C preprocessor to replace calls to target functions with calls to wrapper functions.
-   Link-time interpositioning: Uses the linker's --wrap f flag to resolve references to symbol f as _wrap_f and references to __real_f as f.
-   Runtime interpositioning: Uses the dynamic linker's LD_PRELOAD environment variable to load a shared library before any other shared libraries.

### 7.14 Tools for Manipulating Object Files

-   AR: Creates static libraries.
-   STRINGS: Lists printable strings in an object file.
-   STRIP: Deletes symbol table information.
-   NM: Lists symbols defined in the symbol table.
-   SIZE: Lists names and sizes of sections.
-   READELF: Displays the complete structure of an object file.
-   OBJDUMP: Disassembles binary instructions.
-   LDD: Lists shared libraries needed by an executable at runtime.

### 7.15 Summary

-   Linking can be done at compile time (static) or at load time/runtime (dynamic).
-   Linkers work with object files (relocatable, executable, shared).
-   Key tasks of linkers are symbol resolution and relocation.
-   Static linkers (like GCC) combine relocatable object files into an executable.
-   Loaders put executables into memory for running.
-   Dynamic linkers handle shared libraries.
-   Shared libraries use position-independent code (PIC).
-   Library interpositioning lets you change how shared library functions are called.

### 9.8 Memory Mapping

Linux initializes virtual memory areas by associating them with objects on disk (memory mapping). Areas can be mapped to:

1.  Regular files: Each virtual page is initialized with the contents of a page-sized piece of the file.
2.  Anonymous files: The virtual pages are demand-zero, filled with zeros when first accessed.

Shared objects are mapped into multiple processes' virtual memory, with changes reflected in all. Private objects use copy-on-write, where changes to a page create a new copy, preserving the private address space.

Memory mapping also explains how fork creates a new process with the same virtual memory (copy-on-write) and how execve loads a program by replacing the current process's virtual memory with the new program's.

---
#c
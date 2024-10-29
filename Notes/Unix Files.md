# Unix Files
See [[05.IO.Files.and.Directories.pdf|slides]].

Each process has a **descriptor table** which maps file descriptors to entries in the *open file table*, which is shared among all processes. This table maps to entries in the *v-node table*, which contains the actual [[Vnodes and Inodes|vnodes]].

>[!example]- Table Diagrams
>![[05.IO.Files.and.Directories.pdf#page=13]]


### File Descriptor Manipulatin
Duplicate file descriptor
```c
int dup(int oldfd);
```

Returned `fd` points to same entry in open file table as `oldfd`.

Duplicate file descriptor to specific `fd`
```c
int dup2(int oldfd, int newfd);
```
Entry in `newfd` is overwritten with value in `oldfd`

Retrieve file descriptor of file stream
```c
int fileno(FILE *stream)
```

>[!example]- Graphical Examples
>![[05.IO.Files.and.Directories.pdf#page=17]]

---
#c

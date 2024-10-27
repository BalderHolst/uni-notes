# Unix Files
See [[05.IO.Files.and.Directories.pdf|slides]].

Each process has a **descriptor table** which maps file descriptors to entries in the *open file table*, which is shared among all processes. This table maps to entries in the *v-node table*, which contains the actual [[Vnodes and Inodes|vnodes]].

>[!example]- Table Diagrams
>![[05.IO.Files.and.Directories.pdf#page=13]]


### File Descriptor Manipulatin





---
#c
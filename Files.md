# Files


### Metadata
Data about the file that is not contained within the file.
- Filename
- File type
- File size
- File creation, modification, and access time
- File access permissions
- ...

>[!tip]- The `stat` struct
>```c
>struct stat {
>  dev_t             st_dev;          // device
>  ino_t             st_ino;          // inode
>  mode_t            st_mode;         // protection and file type
>  nlink_t           st_nlink;        // number of hard links
>  uid_t             st_uid;          // user ID of owner
>  gid_t             st_gid;          // group ID of owner
>  dev_t             st_rdev;         // device id (if special file)
>  off_t             st_size;         // total size, in bytes
>  unsigned long     st_blksize;      // preferred blocksize for filesystem 
>I/O
>  unsigned long     st_blocks;       // number of 512b blocks allocated
>  // high-precision timestamps (precision: nanoseconds; since Linux kernel =2.6)
>  struct timespec   st_atim;         // time of last access
>  struct timespec   st_mtim;         // time of last access
>  struct timespec   st_ctim;         // time of last status change
>  // low-precision timestamps  (precision: seconds; always available)
>  time_t            st_atime;        // time of last access
>  time_t            st_mtime;        // time of last modification
>  time_t            st_ctime;        // time of last status change
>};





---
#c

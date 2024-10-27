# Unix IO
Direct mappings to syscalls. Unbuffered, and therefore usually slow compared to buffered alternatives like [[standard IO]].

Kernel devices are all modelled as files.

Files are identified by a **file descriptor** which is *unique withing the process*. A file descriptor is a positive integer.

A process always has access to the following files

| FD  | Definition    | Name            |
| --- | ------------- | --------------- |
| 0   | STDIN_FILENO  | Standard Input  |
| 1   | STDOUT_FILENO | Standard Output |
| 2   | STDERR_FILENO | Standard Error  |

Any other descriptors are obtained by opening new files using the API.

>[!warning] Shortcounts
> Sometimes `read` and `write` returns less bytes than you wanted to read or write. This does not return an error by itself. The **programmer** should therefore detect and handle this themselves.

---

## API

Open and create a new file
```c
int open(const char *pathname, int flags);
int open(const char *pathname, int flags, mode_t mode);
int creat(const char *pathname, mode_t mode);
// Return -1 => error
```
See also `openat`.

Read and write
```c
ssize_t read(int fd, void *buf, size_t count)
ssize_t write(int fd, void *buf, size_t count)
```
See also `pread, readv, pwrite, writev`.

Positioning
```c
off_t lseek(int fd, off_t offset, int whence)
```
The `whence` determines how the `offset` is used:

| Flag | Behavior |
| ---- | -------- |
| SEEK_SET | `filepos = offset` |
| SEEK_CUR | `filepos = filepos + offset` |
| SEEK_END | `filepos = end + offset` (can seek beyond end of file)|



See also `llseek, lseek64`.

Close
```c
int close(int fd)
```

Remove from filesystem
```c
int remove(const char *pathname)
```
See also `unlink, unlinkat, rmdir`.


---

## Examples

#### Opening and Creating files

```c
int fd;
if ((fd = open("/etc/hosts", O_RDONLY)) < 0) {
  perror("Cannot open file");
  exit(EXIT_FAILURE);
}
```

```c
int fd = creat(“log", S_IRUSR|S_IWUSR);
if (fd < 0) {
  perror("Cannot create file");
  exit(EXIT_FAILURE);
}
```

#### Closing Files

```c
int fd;
int retval;

// Open file and do operations …

if ((retval = close(fd)) < 0) {
  perror("Cannot close file");
  exit(EXIT_FAILURE);
}
```
#### Reading Files

```c
char buf[512];
int fd;
ssize_t nbytes;

// Open file …

if ((nbytes = read(fd, buf, sizeof(buf))) < 0) {
  perror("Cannot read from file");
  exit(EXIT_FAILURE);
}
```

Writing files
```c
char buf[512];
int fd;
ssize_t nbytes;

// Open file …

if ((nbytes = write(fd, buf, sizeof(buf)) < 0) {
  perror("Cannot write to file");
  exit(EXIT_FAILURE);
}
```

#### Seeking in Files
```c
int fd;

// Open file …

if (lseek(fd, 100, SEEK_SET) < 0) {
  perror("Cannot seek in file");
  exit(EXIT_FAILURE);
}
```

## Larger Examples

#### Hello, World!
```c
#include <stdlib.h>
#include <unisth.h>
#include <string.h>
char str[] = "Hello, world\n";
int main(void)
{
  write(STDOUT_FILENO, str, strlen(str));
  return EXIT_SUCCESS;
}
```

#### Simple Unix IO
```c
#include <stdlib.h>
#include <unistd.h>
int main(void)
{
  char c;
  while (read(STDIN_FILENO, &c, 1) > 0) {
    write(STDOUT_FILENO, &c, 1);
  }
  return EXIT_SUCCESS;
}
```

---
#c

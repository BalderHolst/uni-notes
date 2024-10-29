# Standard IO
Buffered alternatives to [[Unix IO]]. Usually `f` variants of other C functions.


```c
FILE * fopen(const char *path, const char *mode)
```

Benefits over [[Unix IO]]:
- **Reduces overhead** of IO operation (with buffering)
- Provides *formatted* IO operations

#### Buffering
Use a user-space buffer to reduce calls to `read` and `write` which are direct mappings to syscalls. Files can be opened with differing **buffering modes**.

Works by managing a buffer in user space and only calling [[unix IO]] when the buffer is **flushed**. A buffer is either flushed manually or according the *buffering mode* set for the opened file.

There are three types of buffering:

| Type | Mode | Default for |
| ---- | ---- | ----------- |
| Fully buffered | `_IOFBF` | File descriptor points to a *file* |
| Line buffered | `_IOLBF` | File descriptor connected to a *terminal* |
| Unbuffered | `_IONBF` | *Standard error* or by user request |

Set the buffering mode manually with `setvbuf()`.


#### Formatted IO
- Operates on top of Standard I/O streams
- Independent of buffering mode

---

### Standard Steams
Standard input (`stdin`), output (`stdout`) and error (`stderr`) steams can are defined in `<stdio.h>`.

---

## API

Open and create
```c
FILE * fopen(const char *path, const char *mode);
```
See also `fdopen, fdreopen`.

Read and write
```c
size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);
size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream);
```

Positioning
```c
int fseek(FILE *stream, long offset, int whence);
long ftell(FILE *stream);
```
See also `rewind, fsetpos, fgetpos`

Close
```c
int fclose(FILE *stream);
```
See also `fcloseall`.

Others
```c
int fflush(FILE *stream);
int feof(FILE *stream);
int ferror(FILE *stream);
int fileno(FILE *stream);
```

#### Formatted IO
Read character or line
```c
char *fgets(char *s, int size, FILE *stream)
```
See also `gets`, `fgetc`, `getc`, `getchar`, `ungetch`.

Read formatted input
```c
int fscanf(FILE *stream, const char *format, …)
```
See also `scanf`, `sscanf`, `vscanf` and more.

Write character or line
```c
char fputs(const char *s, FILE *stream)
```
See also `fputc`, `putc`, `putchar`, `puts`.

Write formatted output
```c
int fprintf(FILE *stream, const char *format, …)
```
See also `printf`, `dprintf`, `sprint`, `snprintf`, `vprintf` and more.

---

## Examples

Hello, World!
```c
#include <stdio.h>
#include <stdlib.h>
char str[] = "Hello, world!\n";
int main(void)
{
    // Specify output stream
    fprintf(stdout, "%s", str);

    // Implicitly print to stdout
    printf("%s", str);

    return EXIT_SUCCESS;
}
```

---
#c

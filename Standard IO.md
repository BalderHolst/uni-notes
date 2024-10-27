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


#### Formatted IO
- Operates on top of Standard I/O streams
- Independent of buffering mode

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
```code
int fprintf(FILE *stream, const char *format, …)
```
See also `printf`, `dprintf`, `sprint`, `snprintf`, `vprintf`, …

---
#c

# Directories in C

### API

Open
```c
DIR * opendir(const char *name);
```
See also `fdopendir`.

Read entry

```c
struct dirent* readdir(DIR * dirp)
```

Close

```c
int closedir(DIR * dirp)
```

Retrieve descriptor
```c
int dirfd(DIR * dirp)
```

Make directory

```c
int mkdir(const char * pathname, mode_t mode)
```
See also `mkdirat`.



### Simple Example
```c
#include <…>

int main(int argc, char * argv[]) {
    DIR *dir = opendir(argc > 1 ? argv[1] : ".");
    if (dir == NULL) {
        perror("Cannot open directory");
        return EXIT_FAILURE;
    }
    int dd = dirfd(dir);
    struct dirent * e;
    errno = 0;
    while ((e = readdir(dir)) != NULL) {
        struct stat sb;
        if (fstatat(dd, e->d_name, &sb, 0) < 0) {
            perror("Cannot stat file");
        } else {
            printf("  %-32s %10ld\n", e->d_name, sb.st_size);
        }
        errno = 0;
    }
    if (errno != 0) {
        perror("Cannot enumerate directory");
    }
    closedir(dir);
    return EXIT_SUCCESS;
}
```



---
#c

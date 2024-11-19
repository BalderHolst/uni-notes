# Linux Processes
A linux process can be in five possible states:
- [[#Running or Runnable]] (R)
- [[#Uninterruptible Sleep]] (D)
- [[#Interruptable Sleep]] (S)
- [[#Stopped]] (T)
- [[#Zombie]] (Z)

#### Running or Runnable
The process is ready to be run, but may wait to be scheduled. 

#### Uninterruptible Sleep
The process is waiting on external resources before it can be continued. This could be things like file system operations.

#### Intetrupible Sleep
Process is waiting for a signal before continuing. This is useful when a process should wait for some *non-hardware* event to happen.

#### Stopped
A process can be stopped from the running state by sending either `SIGSTOP` or `SIGTSTP`. `SIGTSTP` cannot be ignored by the process, but `SIGSTOP`can.

#### Zombie
When a child process terminates, it sends the `SIGCHLD` signal to the parent process. The process will remain in the process table until the parent clears it by calling wither `wait()` or `waitpid()`.

---
#linux

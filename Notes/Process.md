# Process
This note is primarily generated by AI.

## 1. Process
- **Program Execution in Modern Systems**:
  - A program appears to be the only one running on the system.
  - It seems like the program uses the processor and memory exclusively.
  - The processor appears to execute the program's instructions sequentially, without interruption.
  - The program's code and data seem to be the only objects in memory.
  
- **Illusion**:
  - The concept of a process provides this illusion.
  
- **Classical Definition of a Process**:
  - An instance of a running program.
  - Each program runs within the context of a specific process.
  
- **Context**:
  - The state required for correct program execution:
    - Program's code and data in memory.
    - Stack.
    - Registers and program counter.
    - Environment variables.
    - Open file descriptors.
  
- **Program Execution**:
  - When the user types an executable file in the shell, a new process is created and executed in its context.

- **Application Programs**:
  - Applications can create new processes to run their code or other programs.
  
- **Implementation of Processes**:
  - Beyond the scope of this text, focusing instead on process abstraction.

- **Key Abstraction**:
  - Processes provide logical control flow and private address space to applications.

    - **Logical Control Flow**:
      - Processes give the illusion that each program exclusively uses the processor, even if multiple programs run simultaneously.
      - Using a Debugger: You can observe a sequence of program counter values, known as logical control flow, during runtime.
    - **Private Address Space**:
      - Process provides the illusion that our program has exclusive use of the memory system.



  
- **User Mode and Kernel Mode**:
  - The processor provides mechanisms to limit instructions and address spaces accessible to applications.
  - In **kernel mode**, a process can execute any instruction and access all memory locations.

- **Context Switch**:
  - The kernel implements multitasking through a context switch, maintaining the state required to restart a process after it has been interrupted, including:
    - General-purpose and floating-point registers
    - Program counter and user stack
    - Status registers and kernel stack
    - Page tables
    - Process and file tables

## 2. Process Control Block (PCB)
- **PCB**:
  - A data structure maintained by the operating system for each process.
  
- **Contents of a PCB**:
  - **Process ID (PID)**: Unique identifier for each process.
  - **Process State**: Current state (e.g., running, waiting, stopped).
  - **Program Counter**: Address of the next instruction.
  - **CPU Registers**: Current values of the registers.
  - **Memory Management Information**: Information like page tables and memory limits.
  - **I/O Status Information**: Allocated I/O devices and open file descriptors.
  - **Accounting Information**: CPU time and scheduling details.
  
- **Role of PCB in Context Switching**:
  - The operating system saves the current process state in its PCB during a context switch, ensuring that processes resume execution from the point where they were interrupted.

## 3. Process Control
- **Unix System Calls**:
  - C programs use system calls to manipulate processes.

- **Process ID**:
  - Each process has a unique PID.
  - `getpid()` returns the process's PID, and `getppid()` returns the parent's PID.

  ```c
  #include <sys/types.h>
  #include <unistd.h>

  pid_t getpid(void);
  pid_t getppid(void);
  ```
- **Process States**:
  - A process can be in one of the following states:
    - **Running**: Actively running or waiting to be scheduled.
    - **Stopped**: Stopped and not scheduled.
    - **Terminated**: Permanently stopped.

- **Process Termination**:
  - A process terminates by:
    1. Receiving a termination signal.
    2. Returning from the `main()` routine.
    3. Calling the `exit()` function.

  ```c
  #include <stdlib.h>
  void exit(int status);
  ```

## 4. Process Termination and Child Process Handling
- **Terminated Process**:
  - A terminated process remains in a terminated state until it is reaped by the parent process.

- **Parent Process Role**:
  - The parent process reaps the terminated child process, at which point the child's exit status is delivered to the parent, and the child is removed from the system.

- **Zombie Process**:
  - A terminated process that has not been reaped is known as a zombie.

## 5. `waitpid()` Function
- **Purpose**:
  - The `waitpid()` function allows a parent process to wait for a specific child process to terminate.

  ```c
  #include <sys/types.h>
  #include <sys/wait.h>

  pid_t waitpid(pid_t pid, int *statusp, int options);
  ```
- **Modifying the Default Behabior**:
    - `WNOHANG`: Returns immediately if the child has not yet terminated.
    - `WUNTRACED`: Waits until the child process is terminated or stopped.
    - `WCONTINUED`: Waits until a stopped process is resumed with SIGCONT.
- **Checking the Exit Status of a Reaped Child**:
    - `WIFEXITED(status)`, `WEXITSTATUS(status)`, `WIFSIGNALED(status)`, `WTERMSIG(status)`, `WIFSTOPPED(status)`, `WSTOPSIG(status)`, `WIFCONTINUED(status)`

## 6. Putting Processes to Sleep
- **Purpose**:
  - The sleep function suspends a process for a specified period of time.
```c
  #include <unistd.h>
  
  unsigned int sleep(unsigned int secs);
  ```

## 7. Loading and Running Programs
- **Purpose**:
  - The execve function loads and runs a new program in the context of the current
process.
```c
  #include <unistd.h>
  
  int execve(const char *filename, const char *argv[],
  const char *envp[]);
  ```

- **Problem**:
  - This simple shell program does not handle background child processes.
- **Solution**:
  - To solve this problem, you need to use signals.

---
#c
# MIC Architecture


## Mic-2
Add bus and IFU.

The new bus allows for less wasted clock cycles

**IFU** allows pre-fetcing the next instruction in parallel with the ALU, meaning that the ALU does not have to carry out this task.

## Mic-3
Introduces *latches* before and after the ALU. This **TRIPPLES** the efficiency, as reading from registers, writing to registers and performing ALU operation, can now *run in parallel*. There can however be other problems with sharing resources.


---
#computerarchitecture
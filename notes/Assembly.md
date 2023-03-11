# Assembly

### The Stack

##### PUSH
*Push* data to the stack and *decrease* the stack pointer by one.

```asm
PUSH register
```

##### POP
*Load* data from the stack and *increase* the stack pointer by one.

```asm
POP register
```

---

### Subrutines
"Functions" in assembly.

##### CALL
Call a subrutine. The stack pointer is reduced by two.

```asm
CALL subrutine
```

##### RCALL
Like [[#CALL]] by with relative a jump instead of absolute.

```asm
RCALL subrutine
```


##### RET
Return from the subrutine. This uses the stack to know where it came from.

```asm
RET
```

---

### Directives
Directives are resolved by the assembler, and therefore *take zero clock cycles to resolve* in the processor.

##### .EQU
A name will be substituted with a number by the assembler.

```asm
.EQU name=address
```

##### .SET
Same as [[#.EQU]] but can be reassigned.

```asm
.SET name=address
```

##### .DEF
Alias for a register.

```asm
.DEF name=register
```

##### .ORG
Sets the code address. The program will now execute from here.

```asm
.ORG address
```

##### .INCLUDE
Include other files. Mostly used to define values with [[#.EQU]].

```asm
.INCLUDE file
```

---

### Instructions

##### LDI - Load Immediate
Load a hardcoded value to a register.

Opcode: $1110\ \text{kkkk}\ \text{dddd}\ \text{kkkk}$

```asm
LDI reg value
```

##### LDS - Load from Data Space
Loads an 8-bit number into a register.


Opcode: $1001\ 000\text{d}\ \text{dddd}\ 0000\ \text{kkkk}\ \text{kkkk}\ \text{kkkk}\ \text{kkkk}$

##### MOV
Copy the content of a register to another.

```asm
MOV addr reg
```
Opcode: $0010\ 11\text{rd}\ \text{dddd}\ \text{rrrr}$

##### INC - Increment
Increment a value in a register

```asm
INC Rd
```

Opcode: $1001\ 010\text{d}\ \text{dddd}\ 0011$

##### ADD
Add two registers togeather and place them in a third register.

---
#microcontrolers 

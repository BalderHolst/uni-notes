# Assembly

### Instructions

##### LDI - Load Immediate
Load a hardcoded value to a register.

Opcode: $1110\,\text{kkkk}\,\text{dddd}\,\text{kkkk}$

##### LDS - Load from Data Space
Loads an 8-bit number into a register.

Opcode: $1001\,000\text{d}\,\text{dddd}\,0000\,\text{kkkk}\,\text{kkkk}\,\text{kkkk}\,\text{kkkk}$

##### MOV
Copy the content of a register to another.

Opcode: $0010\,11\text{rd}\,\text{dddd}\,\text{rrrr}$

##### INC - Increment
Increment a value in a register

```asm
INC Rd
```

Opcode: $1001\,010\text{d}\,\text{dddd}\,0011$

##### ADD
Add two registers togeather and place them in a third register.

---
#microcontrolers 

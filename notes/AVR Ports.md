# AVR Ports

### Naming

`PORT{A, B, C, D}{1 ... 8}`

Letters indicate what port we are talking about, and the numbers denote the pin.



### AVR Ports 
AVR ports are implemented with [[Tri-State Buffer|tri state buffers]].

![[AVR-port.png]]

>[!example]- Setup input/output ports
>```asm
>LDI R16, 0x00		;Loads R16 by 0b00000000
>OUT DDRC,R16		;Setup A as input
>LDI R16, 0xff		;Loads R16 by 0b11111111
>OUT PORTC,R16		;Enable Pull-up resistors
>LDI R16, 0xff
>OUT DDRB,R16		;Loads R16 by 0b11111111
>
>;Setup A as output
>LDI R16, 0x15		;Loads R16 by 0b11111111
>OUT DDRB,R16		;Set output to 0b00010101
```

---
#microcontrolers 

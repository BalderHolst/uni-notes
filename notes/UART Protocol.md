# UART Protocol
See [[Lesson 9.pdf#page=23]]

![[uart.png]]

Data is sent with the [[LSB]] first.

### Common Baud Rates


| Frequency (Hz) |
| :-------:      |
| 4800           |
| 9600           |
| 19200          |
| 115200         |
| 1000000        |

To set the baud rate for AVR use this formula to set the UBRRL register.
$$\text{UBRRL} = \frac{F_{osc}}{16 \cdot baudrate} -1 $$

### Parity
If enabled: adds one extra bit at the end of the message. If the number of ones in the message is **even the parity bit is zero**, and vise versa.

---
#microcontrolers 

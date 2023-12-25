# Interupts
An alternative to [[Pooling|pooling]]. Allows the CPU to run a routine when an external device sends an interrupt request. The CPU will return to the normal program after the interrupt is executed.

Microcontrolers usually have designated interrupt pins.

When an interrupt is triggered, the interrupt handler adds the interrupt to a cue for execution.

All interrupts can be enabled/disabled by the *global interrupt* ([[atmel-0856-avr-instruction-set-manual.pdf#page=161|for atmega32A]]).

>[!example]- AtMega32A Interrupts
>![[ATMEGA32A-interrupts.png]]
>#### Interrupt Priority
>The lower the vector number, the higher the interrupt priority. If interrupts are triggerend at the same time, higher priority interrupts are handled first.



---
#microcontrolers 

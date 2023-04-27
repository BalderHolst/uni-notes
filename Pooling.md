# Pooling
A loop constantly checking for changes on a register, port or other input. An [[Interupts|interupt]] is usually preferred. This method halts the processor when reading the interupt.

#### Example
```cpp
while(1) {
	ADCSRA=0b11000011;          //ADC starts conversion
	while(ADCSRA==0b11000011);  //Check if ADC is done
	PORTB=~ADCH;
}
```




---
#microcontrolers 
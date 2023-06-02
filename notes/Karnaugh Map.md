# Karnaugh Map (K-map)
Alternative way of representing a truth table.

Can be used to generate an expression from a truth table. It is easier than the [[Sum of Products]] method for large truth tables.

Se slides: [[Lesson 3.pdf#page=30]].

The sides of a Karnaugh map "warp" around. 

*The sides count in **gray codes**.*

### Procedure 
1. Draw the ***biggest* rectangles** you can around the $1$'s. The amount of cells in each rectangle should be described by $2^k$. (remember that the table "wraps")
2. For each rectangle write an equivalent equations that would create each rectangle and `OR` them together. (example [[Lesson 3.pdf#page=34|here]])

![[Pasted image 20230602151349.png]]

---
#microcontrolers 

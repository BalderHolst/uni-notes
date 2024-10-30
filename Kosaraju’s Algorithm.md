# Kosaraju’s Algorithm
See [[lecture10.pdf#page=43|slides]].

Algorithm for finding [[Strongly Connected Components|SCCs]] in directed graphs with [[Depth-first Search|DFS]].

#### Procedure
1. Do DFS to create DFS forest
	- Choose starting vertices in any order
	- Keep track of finishing times
2. Reverse all edges of the graph
3. Do DFS again to create *another forest*
	- This time, order the nodes in the reverse order of the finishing times that they had from the first DFS run
4. The **different trees** in the second forrest are the SCCs

>[!example]- Example from Slides
>![[lecture10.pdf#page=45]]


---
#algorithms

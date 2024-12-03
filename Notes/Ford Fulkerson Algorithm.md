# Ford Fulkerson Algorithm
An algorithm for calculating the [[Max Flow|max flow]] of a flow graph.

### Algorithm
1. Create a residual graph
2. Find an augmenting path (unspecified method)
3. Calculate the bottleneck-value of the path
4. Update all edges in the path by adding the bottleneck value to the opposite edges
5. If there are more augmenting paths, *repeat from step 2*.

### Time Complexity
Using [[Breadth-first Search|BFS]] to find augmenting paths:
$$
O(fE)
$$
$f$: Max flow
$E$: Edges

[[Edmonds Karp Algorithm]]: Use a [[Depth-first Search|DFS]] to find augmenting paths:
$$
O(E^{2}V)
$$
$V$: Vetexes
It is better as the time-complexity does not depend on the parameters of the input graph, only its size.

*Capacity Scaling*: Pick larger augmenting paths first! This eliminates most of the drawbacks of [[Breadth-first Search|BFS]] in practice.
$$
O(E^{2}\log(U))
$$

*Dinic's Algorithm*: Uses a combination of [[Breadth-first Search|BFS]] and [[Depth-first Search|DFS]] to find augmenting paths:
$$
O(V^{2}E)
$$

*Push Pelabel*: Uses the "pre-flow" instead of augmenting paths:
$$
O(V^{2}E) \quad\mathrm{or}\quad O(V^{2}\sqrt{E})
$$
Depending on the variant.

>[!note] Don't be afraid!
>Generally, the time complexity of max flow algorithms are very pessimistic. It is therefore hard to say much about the run time of these algorithms solely based on their time complexity.

---

##### Residual Graph
A graph with opposite edges, which start with a capacity of $0$, but get more and more capacity as the original edge capacity fills up.

##### Augmenting Path
A path from $s$ to $t$ with a capacity above $0$. Can only contain edges that are not fully saturated. *The maximum flow is found when there are no more augmenting paths*.

##### Bottleneck
The edge along an augmenting path, which has the smallest capacity, thus limiting the flow through the entire path. The **bottleneck-value** is the capacity of the bottleneck-ing edge.



---

>[!video]- Video Introduction
>![](https://www.youtube.com/watch?v=LdOnanfc5TM)


---
#algorithms
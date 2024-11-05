# Bellman-Ford* Algorithm
Similar to [[Dijkstra’s algorithm]] but can handel (detect) *negative weights*. However, **it is slower**.

```
procedure Bellman-Ford*(G,s):

    Initialize arrays d(0),…,d(n-1) of length n
    d(0)[v] = ∞ for all v in V
    d(0) [s] = 0

    For i=0,…,n-2:
        For v in V:
            d(i+1)[v] ← min( d(i)[v] , min_{u in v.inNbrs} {d(i)[u] + w(u,v)} )

    Now, dist(s,v) = d(n-1)[v] for all v in V.
    (Assuming no negative cycles)
```

>[!tip] Implementation: Don't actually save `n` arrays
>In practice, we only need to keep the track of the last two arrays (entries in `d`). This can drastically minimize memory usage.


>[!example]- Bellman-Ford in Example
>![[lecture12.pdf#page=10]]

#### Detecting Negative Cycles
If there are *no negative cycles* the program, `d[v]` will stabilize within `n-1` rounds.

If there ***negative cycles are present***, `d[v]` will keep changing event after `n-1` rounds. To detect this, run the algorithm for *one more step*. If the values change, the graph contains a negative cycle.



---
#algorithms

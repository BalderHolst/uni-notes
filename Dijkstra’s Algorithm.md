# Dijkstra’s algorithm
Find the distance from node `s` to every other node in graph `G`. See also [[lecture11.pdf|slides]].

```
procedure Dijkstra(G,s):
    Set all vertices to `not-sure`
    d[v] = ∞ for every v in V
    d[s] = 0
    While there are not-sure nodes:
        Pick the not-sure node u with the smallest estimate 
        d[u].
            For v in u.neighbors:
                d[v] ← min( d[v] , d[u] + edgeWeight(u,v))
        Mark u as sure.
    Now d(s, v) = d[v]
```
`G`: Graph
`V`: Vertices of `G`
`s`: The node we want to find the distance from
`d`: Array of shortest distance estimate from `s`

>[!warning] No negative weights
>Dijkstra's algorithm only works on graphs with **positive weights**.

>[!example]- Dijkstra by Example
>![[lecture11.pdf#page=25]]


---
#algorithms

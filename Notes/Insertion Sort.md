# Insertion Sort
Insert the current number correctly in the part left of the current cursor position.

>[!info]- Python Implementation
>```python
>def insertion_sort(l):
>    for i, current in enumerate(l):
>        # initialize new counter from current index
>        j = i - 1
>
>        # shift elements to the right until we find the correct position for the current value
>        while j >= 0 and current < l[j]:
>            l[j + 1] = l[j]
>            j -= 1
>
>        # insert the current value in the correct position
>        l[j + 1] = current
>
>    return l
>```

### Time Complexity
In the worst case, the input is inversely sorted.
$$O(n^2)$$
If the input is **already sorted**, the time complexity is very close to $\Theta(n)$.

---
#algorithms #sorting
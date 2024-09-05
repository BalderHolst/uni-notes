# Mergesort
Divide and concur. This algorithm breaks down the input into smaller and smaller parts *recursively*. Then the algorithm reassembles the sorted array.

>[!example]- Python Implementation
>```python
>def merge_sort(l):
>
>    # Recursive base case
>    if len(l) <= 1: return l
>
>    # Split the list in the middle
>    mid = len(l) // 2
>    left = merge_sort(l[:mid])
>    right = merge_sort(l[mid:])
>
>    # Re-merge into sorted list.
>    return merge(left, right)
>
># Merges two sorted lists into a single sorted list.
>def merge(left, right):
>    result = []
>    i, j = 0, 0
>
>    # Append the elements in order
>    while i < len(left) and j < len(right):
>        if left[i] <= right[j]:
>            result.append(left[i])
>            i += 1
>        else:
>            result.append(right[j])
>            j += 1
>
>    # Append the remaining elements
>    result += left[i:]
>    result += right[j:]
>
>    return result
>```

#### Time Complexity
$$
O(n\cdot \log(n))
$$

---
#algorithms #sorting 

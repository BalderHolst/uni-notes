# Machine Learning

### Classification
Output: Class

### Regression
Ouput: Value

---

## Notes

```base
views:
  - type: cards
    name: View
    filters:
      and:
        - file.tags.contains("machine-learning")
    order:
      - file.name
      - file.mtime
    sort:
      - property: file.mtime
        direction: DESC
    imageAspectRatio: 1.1
    cardSize: 210
  - type: table
    name: Table
    filters:
      and:
        - file.tags.contains("statistics")
    order:
      - file.name
      - file.ctime
      - file.mtime
    sort:
      - property: file.mtime
        direction: DESC
```

---
#subject

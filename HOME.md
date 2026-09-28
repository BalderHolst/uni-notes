## Recent

```base
filters:
  and:
    - file.inFolder("Notes")
views:
  - type: table
    name: Table
    order:
      - file.name
      - file.mtime
    sort:
      - property: file.mtime
        direction: DESC
    limit: 10

```

---

```base
views:
  - type: cards
    name: View
    filters:
      and:
        - file.tags.contains("subject")
    order:
      - file.name
      - file.ctime
    sort:
      - property: file.mtime
        direction: DESC
    imageAspectRatio: 1.1
    cardSize: 210
```

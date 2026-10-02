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
      - created
    sort:
      - property: file.mtime
        direction: DESC
      - property: created
        direction: ASC
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
        - '!file.inFolder("Templates")'
    order:
      - file.name
      - created
    sort:
      - property: created
        direction: DESC
    imageAspectRatio: 1.1
    cardSize: 210

```

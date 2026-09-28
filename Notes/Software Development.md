---
created: 2026-09-28
tags: [subject]
---
# Software Development

```base
views:
  - type: cards
    name: View
    filters:
      and:
        - file.tags.contains("softwaredevelopment")
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
        - file.tags.contains("softwaredevelopment")
    order:
      - file.name
      - file.ctime
      - file.mtime
    sort:
      - property: file.mtime
        direction: DESC
```

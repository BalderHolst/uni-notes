---
created: 2026-09-28
---
# Data Communication
### Aspects of Protocols
**Syntax**: The *format/structure* of the data.
**Semantics**: How the recipient *understands* the data.
**Timing**: How fast data should be sent or recieved.

Protocols are usually organised in *layers*, as it allows for easier debugging. The bottom layer is always physical, meaning wires, components and their connections.

```base
views:
  - type: cards
    name: View
    filters:
      and:
        - file.tags.contains("datacommunication")
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

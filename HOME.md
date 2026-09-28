## Recent

```dataview 
table
file.mtime as "Redigeret"
from "/" and !"External"
sort file.mtime desc
limit 5
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
>```

---
created: 2026-09-25
tags: [subject]
---
# Machine Learning

## Output of Algorithms

#### Classification Algorithms
- [[Perceptron]] -> class
- MPL -> propability -> class (argmax)
- [[Logistic Regression]] -> propability -> class (argmax)
- [[K-nearest Neighbors]] -> class -> confidence fraction
- [[Classification Trees]] -> class
- [[Classification Forrest]] -> class -> confidence fraction
- [[Kernel Perceptron]] -> class
- [[Best Seperation (SVM)]] -> class -> confidence within margin

#### Regression Algorithms
- [[Linear Regression]] -> model -> confidence interval of the line



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
      - created
    sort:
      - property: created
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

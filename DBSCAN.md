---
created: 2026-11-19
tags:
  - machine-learning
---

# DBSCAN

Two parameters to train for
- `EPS` - Radius of the neighborhood for each point
- `min_samples` - Number of samples needed for a point to be a core point.

Three types of point

- **Core Points** - Point within which neighbourhood we have at least `min_samples` datapoints
- **Border points** - Not enough points to be a dense neighbourhood, but within another neighbourhood
- **Noise Points** - Not withing a neighbourhood

#### Deterministic!
DBSCAN is not dependent on its initialization like [[K-means Algorithm|K-means]] and [[Gaussian Mixture Models]].

## Procedure
1. Identify core points
2. Select **one** core point randomly
3. "Grow" the cluster to encalulate all adjacent core point
4. Goto step 2
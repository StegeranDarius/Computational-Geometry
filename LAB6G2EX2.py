# This algorithm has a time complexity of O(n^2), where n is the number of points in the set.

# This algorithm works by starting at a point on the convex hull,
#  and then "wrapping" the points of the convex hull around the 
#  starting point in a clockwise direction until it returns to the starting point


def convex_hull(points):
  start = min(points, key=lambda p: p[0])
  hull = []
  current = start
  next = None
  while True:
    hull.append(current)
    next = points[0]
    for p in points[1:]:
      if (next[1] - current[1]) * (p[0] - current[0]) > (p[1] - current[1]) * (next[0] - current[0]):
        next = p
    current = next
    if current == start:
      break
  return hull

λ = float(input("Enter the value of λ: "))
points = [(3, -3), (3, 3), (-3, -3), (-3, 3), (2 - λ, 3 + λ)]
hull = convex_hull(points)
print(f"Number of points on the convex hull: {len(hull)}")

import math

def orientation(p, q, r):
  # compute the cross product of the vectors pq and pr
  val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
  # if the cross product is positive, the points form a counterclockwise turn
  if val > 0:
    return 1
  # if the cross product is negative, the points form a clockwise turn
  elif val < 0:
    return -1
  # if the cross product is zero, the points are collinear
  else:
    return 0

def dist(p, q):
  # compute the Euclidean distance between the points p and q
  return math.sqrt((q[1] - p[1])**2 + (q[0] - p[0])**2)

def graham_scan(points):
  # find the point with the minimum y-coordinate (or, if there are multiple points with the same minimum y-coordinate, the one with the minimum x-coordinate)
  start = min(points, key=lambda p: (p[1], p[0]))
  # sort the points by the angle they make with the starting point
  points.sort(key=lambda p: (math.atan2(p[1] - start[1], p[0] - start[0]), dist(start, p)))
  # initialize an empty list to store the points on the convex hull
  hull = []
  # add the starting point to the list of points on the convex hull
  hull.append(points[0])
  # add the next point to the list of points on the convex hull
  hull.append(points[1])
  # for each remaining point in the list of points
  for i in range(2, len(points)):
    # while the last three points in the list of points on the convex hull form a clockwise turn
    while len(hull) >= 2 and orientation(hull[-2], hull[-1], points[i]) != 1:
      # remove the last point from the list of points on the convex hull
      hull.pop()
    # add the current point to the list of points on the convex hull
    hull.append(points[i])
  # return the list of points on the convex hull
  return hull

# test the function with the points P1, P2, P3, P4, P5, P6, and P7
points = [(4, 2), (7, 1), (-3, 5), (3, 6), (-4, -4), (-1, 1), (2, -6)]
hull = graham_scan(points)
# print the points on the convex hull
print("Points on the convex hull:")
for p in hull:
  print(p)

for x in range(minx, maxx+1):
#     for y in range(miny, maxy+1):
#         closest = -1
#         d = 10**10
#         tie = 0
#         for k in range(len(points)):
#             if dist([x, y], points[k]) < d:
#                 tie = 0
#                 d = dist([x, y], points[k])
#                 closest = k
#             elif dist([x, y], points[k]) == d:
#                 tie = 1
#         if not tie and not onHull[closest]:
#             grid[x][y] = closest+1

import time, itertools as itt


def load(file):
  with open(file) as f:
    grid = set()
    for y, row in enumerate(f.read().split('\n')):
      for x, c in enumerate(row):
        if c != '#': grid.add((x, y))
        if c == 'S': start = (x, y)
    return grid, start


def neighbors(x, y):
  return (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)


def gen_all_distances(grid, start):
  queue, distances = [start], {start: 0}
  while queue:
    pos = queue.pop(0)
    for new_pos in neighbors(*pos):
      if new_pos not in grid or new_pos in distances: continue
      queue += [new_pos]
      distances[new_pos] = distances[pos] + 1
  return distances


def solve(grid, start):
  part1 = part2 = 0
  dist = gen_all_distances(grid, start)
  
  for (ax, ay), (bx, by) in itt.combinations(dist, 2):
    manh_dist = abs(ax - bx) + abs(ay - by)
    if manh_dist > 20: continue
    if dist[bx,by] - dist[ax,ay] - manh_dist < 100: continue
    part1 += manh_dist == 2 
    part2 += manh_dist < 21 
  
  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(*load("day20.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

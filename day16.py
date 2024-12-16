import time, heapq


def load(file):
  walls = set()
  with open(file) as f:
    for y, row in enumerate(f.read().split('\n')):
      for x, c in enumerate(row):
        match c:
          case '#': walls.add((x, y))
          case 'S': start = x, y
          case 'E': end = x, y
    return start, end, walls


def dirs(x, y, dx, dy):
  dx1, dy1 = -dy, dx
  
  return ((x + dx, y + dy), (dx, dy), 1), \
         ((x, y), (dx1, dy1), 1000), \
         ((x, y), (-dx1, -dy1), 1000)


def bfs_priority(start, end, walls):
  queue, seen, tiles = [(0, start, (1, 0), {start})], dict(), set()
  min_cost = 999999

  while queue:
    cost, pos, dir, path = heapq.heappop(queue)
    if cost > min_cost: return min_cost, len(tiles)
    if cost > seen.get((*pos, *dir), 999999): continue

    seen[*pos, *dir] = cost

    if pos == end:
      min_cost = cost
      tiles |= path

    for new_pos, new_dir, add_cost in dirs(*pos, *dir):
      if new_pos in walls: continue
      heapq.heappush(queue, (cost + add_cost, new_pos, new_dir, path | {new_pos}))


def solve(p):
  return bfs_priority(*p)


time_start = time.perf_counter()
print(f'Solution: {solve(load("day16.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

import time


def load(file):
  with open(file) as f:
    return [tuple(map(int,row.split(','))) for row in f.read().split('\n')]


def out_bound(x, y):
  return not (0 <= x < W and 0 <= y < H)


def bfs(seen):
  queue = [((0, 0), 0)]
  while queue:
    (x, y), step = queue.pop(0)
    if (x, y) == (W - 1, H - 1): return step
    for new_pos in ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)):
      if new_pos in seen or out_bound(*new_pos): continue
      seen.add(new_pos)
      queue.append((new_pos, step + 1))


def binary_search(p, low):
  high = len(p)
  while  high - low > 1:
    mid = (low + high) // 2
    low, high = (mid, high) if bfs(set(p[:mid])) else (low, mid)
  return p[low]


def solve(p, bytes):
  part1 = bfs(set(p[:bytes]))
  part2 = binary_search(p, bytes)
  return part1, part2


time_start = time.perf_counter()
W = H = 71

print(f'Solution: {solve(load("day18.txt"), 1024)}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

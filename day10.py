import time


def load(file):
  with open(file) as f:
    return {(x, y): int(c) for y, row in enumerate(f.read().split('\n'))
            for x, c in enumerate(row)}


def count_trails(p, x, y, n):
  dist_nines, trails = set(), 0
  queue = [(x, y, n)]
  while queue:
    x, y, n = queue.pop()
    if n == 9:
      dist_nines.add((x, y))
      trails += 1
      continue
    for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
      nx, ny = x + dx, y + dy
      n1 = p.get((nx, ny), -1)
      if n1 - n != 1: continue
      queue.append((nx, ny, n1))
  return len(dist_nines), trails


def solve(p):
  part1 = part2 = 0
  for (x, y), n in p.items():
    if n != 0: continue
    dist_nines, trails = count_trails(p, x, y, n)
    part1 += dist_nines
    part2 += trails
  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day10.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

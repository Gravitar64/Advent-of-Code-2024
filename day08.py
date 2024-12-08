import time, collections as coll, itertools as itt


def load(file):
  with open(file) as f:
    return {(x, y): c for y, row in enumerate(f.read().split('\n'))
            for x, c in enumerate(row)}


def get_antinodes(p, antennas, min_mul, max_mul) -> set:
  antinodes = set()
  for poss in antennas.values():
    for (x1, y1), (x2, y2) in itt.combinations(poss, 2):
      for mul in range(min_mul, max_mul):
        dx, dy = x2 - x1, y2 - y1
        nx, ny = x1 - dx * mul, y1 - dy * mul
        mx, my = x2 + dx * mul, y2 + dy * mul

        a, b = (nx, ny) in p, (mx, my) in p
        if not a and not b: break

        if a: antinodes.add((nx, ny))
        if b: antinodes.add((mx, my))
  return antinodes


def solve(p):
  part1 = part2 = 0
  antennas = coll.defaultdict(list)
  for pos, c in p.items():
    if c == '.': continue
    antennas[c].append(pos)

  part1 = len(get_antinodes(p, antennas, 1, 2))
  part2 = len(get_antinodes(p, antennas, 0, 50))

  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day08.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

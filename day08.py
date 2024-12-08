import time, collections as coll, itertools as itt


def load(file):
  with open(file) as f:
    return {(x, y): c for y, row in en(f.read().split('\n')) for x, c in en(row)}


def gen_resonances(p, antennas, part1):
  antinodes = set() if part1 else set(n for poss in antennas.values() for n in poss)
  max_mul = 2 if part1 else max(p)[0]

  for _, poss in antennas.items():
    for mul in range(1, max_mul):
      for (x1, y1), (x2, y2) in itt.combinations(poss, 2):
        dx, dy = x2 - x1, y2 - y1
        nx, ny = x1 - dx * mul, y1 - dy * mul
        if (nx, ny) in p:
          antinodes.add((nx, ny))
        nx, ny = x2 + dx * mul, y2 + dy * mul
        if (nx, ny) in p:
          antinodes.add((nx, ny))
  return antinodes


def solve(p):
  antennas = coll.defaultdict(list)
  for pos, c in p.items():
    if c == '.': continue
    antennas[c].append(pos)

  part1 = len(gen_resonances(p, antennas, part1=True))
  part2 = len(gen_resonances(p, antennas, part1=False))

  return part1, part2


time_start = time.perf_counter()
en = enumerate
print(f'Solution: {solve(load("day08.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

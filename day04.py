import time


def load(file):
  with open(file) as f:
    return {(r, c): char for r, row in enumerate(f) for c, char in enumerate(row)}


def check_target(p, r, c, dr, dc, target) -> bool:
  word = ''.join(p.get((r + dr * i, c + dc * i), ' ') for i in range(len(target)))
  return word == target or word[::-1] == target


def solve(p):
  part1 = part2 = 0
  for r, c in p:
    for delta in ((1, 0), (0, 1), (1, 1), (1, -1)):
      part1 += check_target(p, r, c, *delta, 'XMAS')
    part2 += check_target(p, r, c, 1, 1, 'MAS') and check_target(p, r, c + 2, 1, -1, 'MAS')

  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day04.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

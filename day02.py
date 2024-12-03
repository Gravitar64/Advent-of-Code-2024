import time, itertools as itt


def load(file):
  with open(file) as f:
    return [list(map(int, row.split())) for row in f]


def check_safe(report) -> bool:
  diffs = {a - b for a, b in itt.pairwise(report)}
  return diffs.issubset({1, 2, 3}) or diffs.issubset({-1, -2, -3})


def solve(p):
  part1 = part2 = 0
  for report in p:
    part1 += check_safe(report)
    part2 += any(check_safe(report[:i] + report[i + 1:]) for i in range(len(report)))

  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day02.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

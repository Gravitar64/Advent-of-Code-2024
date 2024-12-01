import time, re


def load(file):
  with open(file) as f:
    return re.findall('\d+', f.read())


def solve(p):
  left = sorted([int(p[i]) for i in range(0, len(p), 2)])
  right = sorted([int(p[i]) for i in range(1, len(p), 2)])
  part1 = sum(abs(b - a) for a, b in zip(left, right))
  part2 = sum(a * right.count(a) for a in left)
  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day01.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

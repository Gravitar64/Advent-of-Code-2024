import time, re


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]
  

def solve(p):
  part1 = part2 = 0
  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day01.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
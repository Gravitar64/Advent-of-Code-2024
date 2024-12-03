import time, re


def load(file):
  with open(file) as f:
    return f.read()


def solve(p):
  part1 = part2 = 0
  
  enabled = True
  for dont, do, m1, m2 in re.findall(r'(don\'t\(\))|(do\(\))|mul\((\d+),(\d+)\)', p):
    if dont or do:
      enabled = do
      continue
    e = int(m1) * int(m2)
    part1 += e
    if not enabled: continue
    part2 += e

  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day03.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

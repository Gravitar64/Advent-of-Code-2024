import time, re


def load(file):
  with open(file) as f:
    return f.read()


def solve(p):
  part1 = part2 = 0
  enabled = True
  
  for dont, do, x, y in re.findall(r'(don\'t\(\))|(do\(\))|mul\((\d+),(\d+)\)', p):
    if dont or do: 
      enabled = bool(do)
    else:
      part1 += (e := int(x) * int(y))
      part2 += e * enabled
  
  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day03.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

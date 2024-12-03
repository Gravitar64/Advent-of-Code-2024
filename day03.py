import time, re


def load(file):
  with open(file) as f:
    return f.read()
  

def solve(p):
  part1 = part2 = 0
  
  enabled = True
  for match in re.findall(r'(don\'t\(\))|(do\(\))|mul\((\d+),(\d+)\)',p):
    if match[0]:
      enabled = False
    elif match[1]:
      enabled = True
    else:
      e = int(match[2]) * int(match[3])
      part1 += e
      if not enabled: continue
      part2 += e  

  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day03.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
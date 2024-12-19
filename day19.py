import time, re, functools


def load(file):
  with open(file) as f:
    return (re.findall('\w+',b) for b in f.read().split('\n\n'))
  

@functools.cache
def count_variants(design, patterns):
  if not design: return 1
  
  variants = 0
  for patt in patterns:
    if not design.startswith(patt): continue
    variants += count_variants(design.removeprefix(patt), patterns)
  
  return variants    


def solve(patterns, designs):
  part1 = part2 = 0
  for design in designs:
    poss_patt = tuple(p for p in patterns if p in design)
    if not (v := count_variants(design, poss_patt)): continue
    part1 += 1
    part2 += v
  
  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(*load("day19.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

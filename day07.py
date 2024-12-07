import time, re


def load(file):
  with open(file) as f:
    return [list(map(int, re.findall('\d+', row))) for row in f]


def is_valid(target, numbers, part2):
  subtotals = {target}
  for number in reversed(numbers):
    new_sub = set()
    for sub in subtotals:
      if not sub % number:
        new_sub.add(sub // number)
      if sub >= number:
        new_sub.add(sub - number)
      if not part2: continue
      str_sub, str_num = map(str, [sub, number])
      if sub > number and str_sub.endswith(str_num):
        new_sub.add(int(str_sub[:-len(str_num)]))
    subtotals = new_sub
  return target if 0 in subtotals else False


def solve(p):
  part1 = part2 = 0
  for target, *numbers in p:
    part1 += is_valid(target, numbers,part2=False)
    part2 += is_valid(target, numbers,part2=True)
  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day07.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

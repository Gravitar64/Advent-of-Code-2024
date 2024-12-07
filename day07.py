import time, re, itertools as itt


def load(file):
  with open(file) as f:
    return [list(map(int, re.findall('\d+', line))) for line in f.readlines()]


def is_valid(target, start, numbers, part1):
  operators = '*+' if part1 else '*+|'
  for variant in itt.product(operators, repeat=len(numbers)):
    tmp = start
    for operator, number in zip(variant, numbers):
      match operator:
        case '*': tmp *= number
        case '+': tmp += number
        case '|': tmp = int(f'{tmp}{number}')
    if tmp == target: return target
  return False


def solve(p):
  part1 = part2 = 0
  for target, start, *numbers in p:
    part1 += is_valid(target, start, numbers, part1=True)
    part2 += is_valid(target, start, numbers, part1=False)
  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day07.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

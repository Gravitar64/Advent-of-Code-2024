import time, re


def load(file):
  with open(file) as f:
    return [list(map(int, re.findall('\d+', block)))
            for block in f.read().split('\n\n')]


def cheapest_way(machine, offset):
  # Cramer's rule https://en.wikipedia.org/wiki/Cramer%27s_rule
  ax, ay, bx, by, prize_x, prize_y = machine

  prize_x += offset
  prize_y += offset

  d = ax * by - bx * ay
  if d == 0: return 0

  bt_a = (by * prize_x - bx * prize_y) / d
  bt_b = (ax * prize_y - ay * prize_x) / d

  if not bt_a.is_integer() or not bt_b.is_integer(): return 0

  return int(bt_a * 3 + bt_b)


def solve(p):
  part1 = part2 = 0
  for machine in p:
    part1 += cheapest_way(machine, 0)
    part2 += cheapest_way(machine, 10e12)
  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day13.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

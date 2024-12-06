import time


def load(file):
  with open(file) as f:
    return {(x, y): char for y, line in enumerate(f.read().split('\n'))
            for x, char in enumerate(line)}


def run_guard_run(p, guard_pos, guard_dir):
  distinct_pos, counter = set(), 0
  while True:
    (x, y), (dx, dy) = guard_pos, guard_dir
    new_pos = x + dx, y + dy

    if new_pos not in p: return distinct_pos
    if counter > 500: return 'loop'

    if p[new_pos] == '#':
      guard_dir = -dy, dx
    else:
      guard_pos = new_pos
      if new_pos in distinct_pos:
        counter += 1
      else:
        distinct_pos.add(new_pos)
        counter = 0


def solve(p):
  part1 = part2 = 0
  guard_pos = [pos for pos, char in p.items() if char == '^'][0]
  guard_dir = (0, -1)
  distinct_pos = run_guard_run(p, guard_pos, guard_dir)
  part1 = len(distinct_pos | {guard_pos})

  for pos in distinct_pos:
    p[pos] = '#'
    if run_guard_run(p, guard_pos, guard_dir) == 'loop': part2 += 1
    p[pos] = '.'

  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day06.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

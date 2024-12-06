import time


def load(file):
  with open(file) as f:
    return {(x, y): char for y, line in enumerate(f.read().split('\n')) for x, char in enumerate(line)}


def run_guard_run(p, guard_pos, guard_dir, dirs):
  distinct_pos = set()
  counter = 0
  while True:
    dx, dy = dirs[guard_dir][0]
    x, y = guard_pos
    nx, ny = x + dx, y + dy
    if (nx, ny) not in p:
      return distinct_pos
    if p[nx, ny] == '#':
      guard_dir = dirs[guard_dir][1]
    else:
      guard_pos = nx, ny
      if (nx, ny) in distinct_pos:
        counter += 1
      else:
        counter = 0
      distinct_pos.add((nx, ny))
    if counter > 1000: return 'loop'


def solve(p):
  part1 = part2 = 0
  dirs = {'^': ((0, -1), '>'), '>': ((1, 0), 'v'), '<': ((-1, 0), '^'), 'v': ((0, 1), '<')}
  guard_pos = [pos for pos, char in p.items() if char == '^'][0]
  guard_dir = p[guard_pos]
  
  distinct_pos = run_guard_run(p, guard_pos, guard_dir, dirs) | {guard_pos}
  part1 = len(distinct_pos)
  
  for x,y in distinct_pos:
    p[x, y] = '#'
    e = run_guard_run(p, guard_pos, guard_dir, dirs)
    if e == 'loop': part2 += 1
    p[x, y] = '.'

  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day06.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

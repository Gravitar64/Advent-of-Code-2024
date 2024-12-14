import time, re, math


def load(file):
  with open(file) as f:
    return [list(map(int, re.findall('-?\d+', row))) for row in f.readlines()]


def move_robots(p, times, w, h):
  for i, (x, y, dx, dy) in enumerate(p):
    x, y = (x + dx * times) % w, (y + dy * times) % h
    p[i] = x, y, dx, dy
  return [(x,y) for x,y,_,_ in p]  


def count_quadrants(robots, w, h):
  mid_w, mid_h = w // 2, h // 2
  quadrants = [0] * 4
  for x, y in robots:
    if x == mid_w or y == mid_h: continue
    quadrant = y // (mid_h+1) * 2 + x // (mid_w+1)
    quadrants[quadrant] += 1
  return math.prod(quadrants)


def show_robots(robots, w, h):
  for y in range(h):
    for x in range(w):
      if (x, y) in robots:
        print('*', end='')
      else:
        print(' ', end='')
    print()
  print()


def solve(p):
  part1 = part2 = 0
  w, h = 101, 103
  p2 = p.copy()
  robots = move_robots(p, 100, w, h)
  part1 = count_quadrants(robots, w, h)
  while True:
    part2 += 1
    robots = move_robots(p2, 1, w, h)
    if len(set(robots)) != len(robots): continue
    show_robots(robots,w,h)
    break
  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day14.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

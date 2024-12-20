import time


def load(file):
  with open(file) as f:
    spaces = set()
    for y, row in enumerate(f.read().split('\n')):
      for x, c in enumerate(row):
        if c != '#': spaces.add((x, y))
        if c == 'S': start = (x, y)
        if c == 'E': end = (x, y)
    return spaces, start, end


def neighbors(x, y):
  return (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)


def get_shortest_path(spaces, start, end):
  queue, seen = [(start, [start])], set()
  while queue:
    pos, path = queue.pop(0)
    if pos == end: return path

    for new_pos in neighbors(*pos):
      if new_pos not in spaces or new_pos in seen: continue
      seen.add(new_pos)
      queue.append((new_pos, path + [new_pos]))


def solve(spaces, start, end):
  part1 = part2 = 0
  path = get_shortest_path(spaces, start, end)

  for a in range(len(path)):
    for b in range(a + 102, len(path)):
      (ax, ay), (bx, by) = path[a], path[b]
      manh_dist = abs(ax - bx) + abs(ay - by)
      if manh_dist > 20 or b - a - manh_dist < 100: continue
      part1 += manh_dist == 2
      part2 += manh_dist < 21

  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(*load("day20.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

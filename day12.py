import time


def load(file):
  with open(file) as f:
    return {(x, y): c for y, row in enumerate(f.read().split('\n'))
            for x, c in enumerate(row)}


def dirs(x, y):
  return (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)


def corner_points(x, y):
  return (x - 0.5, y - 0.5), (x + 0.5, y - 0.5), (x + 0.5, y + 0.5), (x - 0.5, y + 0.5)


def get_area(x, y, plant, p):
  queue, seen = [(x, y)], set()
  while queue:
    x, y = queue.pop()
    seen.add((x, y))
    for nx, ny in dirs(x, y):
      if (nx, ny) in seen: continue
      if p.get((nx, ny), '@') != plant: continue
      queue.append((nx, ny))
  return seen


def get_perimeter(area):
  return len([(x, y) for x, y in area for nx, ny in dirs(x, y)
              if (nx, ny) not in area])


def get_sides(area):
  corn_count = 0
  corn_candidates = {(nx, ny) for x, y in area for nx, ny in corner_points(x, y)}

  for x, y in corn_candidates:
    corners = [(nx, ny) in area for nx, ny in corner_points(x, y)]
    if sum(corners) in (1, 3):
      corn_count += 1
    elif corners == [True, False, True, False] or corners == [False, True, False, True]:
      corn_count += 2
  return corn_count


def solve(p):
  part1 = part2 = 0
  found_areas = set()

  for (x, y), plant in p.items():
    if (x, y) in found_areas: continue

    found_areas.update(area := get_area(x, y, plant, p))

    perimeter = get_perimeter(area)
    sides = get_sides(area)
    part1 += len(area) * perimeter
    part2 += len(area) * sides

  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day12.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

import time, re, functools


def load(file):
  with open(file) as f:
    return list(map(int, re.findall('\d+', f.read())))


@functools.cache
def count_stones(stone, blinks):
  if blinks == 0: return 1
  
  if stone == 0:
    return count_stones(1, blinks - 1)
  elif (lenght := len(str(stone))) % 2 == 0:
    left, right = int(str(stone)[:lenght // 2]), int(str(stone)[lenght // 2:])
    return count_stones(left, blinks - 1) + count_stones(right, blinks - 1)
  else:
    return count_stones(stone * 2024, blinks - 1)


def solve(p):
  part1 = part2 = 0
  for stone in p:
    part1 += count_stones(stone, 25)
    part2 += count_stones(stone, 75)
  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day11.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

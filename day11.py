import time, re


def load(file):
  with open(file) as f:
    return list(map(int, re.findall('\d+', f.read())))


memory = {}
def count_stones(stone, blinks):
  if blinks == 0: return 1
  elif (stone, blinks) in memory:
    return memory[(stone, blinks)]
  elif stone == 0:
    val = count_stones(1, blinks - 1)
  elif not len(str(stone)) % 2:
    mid = len(str(stone))//2
    val = count_stones(int(str(stone)[:mid]), blinks - 1) + count_stones(int(str(stone)[mid:]), blinks - 1)
  else:
    val = count_stones(stone * 2024, blinks - 1)
  memory[(stone, blinks)] = val
  return val


def solve(p):
  part1 = part2 = 0
  for stone in p:
    part1 += count_stones(stone,25)
    part2 += count_stones(stone,75)
  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day11.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

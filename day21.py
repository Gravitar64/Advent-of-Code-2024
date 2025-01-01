# https://github.com/LiquidFun/adventofcode/blob/main/2024/21/21.py

import time, itertools as itt, functools


def load(file):
  with open(file) as f:
    return [e for e in f.read().split('\n')]


time_start = time.perf_counter()

num_kp = {'7': 0, '8': 1,      '9': 2,
          '4': 1j, '5': 1 + 1j, '6': 2 + 1j,
          '1': 2j, '2': 1 + 2j, '3': 2 + 2j,
          ' ': 3j, '0': 1 + 3j, 'A': 2 + 3j}
dir_kp = {' ': 0,  '^': 1,      'A': 2,
          '<': 1j, 'v': 1 + 1j, '>': 2 + 1j}


# Optimal Path between a,b is:
# - No Zig-Zag-Motion, better multiple Moves with same direction
# - Move like Manhatten Distance (dy*'v' + dx*'>')
# - First all vertical moves, then the horizontal moves
# - If move over the "Bad"-Square, switch to first horizontal than vertical moves

@functools.cache
def path(start, end):
  pad = num_kp if start in num_kp and end in num_kp else dir_kp
  diff = pad[end] - pad[start]
  dx, dy = int(diff.real), int(diff.imag)
  vert = ('^' * -dy) + ('v' * dy)
  hori = ('<' * -dx) + ('>' * dx)

  bad = pad[' '] - pad[start]
  vert_first = (dx > 0 or bad == dx) and bad != dy * 1j
  return (vert + hori if vert_first else hori + vert) + 'A'


@functools.cache
def gen_len(sub_path, depth, s=0):
  if depth == 0: return len(sub_path)
  for a, b in itt.pairwise('A' + sub_path):
    s += gen_len(path(a, b), depth - 1)
  return s


def solve(p):
  part1 = part2 = 0
  
  for code in p:
    num_part = int(code[:3])
    part1 += num_part * gen_len(code, 3)
    part2 += num_part * gen_len(code, 26)
  
  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day21.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.4f} sec')

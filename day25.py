import time, itertools as itt


def load(file):
  locks, keys = [], []
  with open(file) as f:
    blocks = [block for block in f.read().split('\n\n')]
    for block in blocks:
      shematic = [[c for c in row] for row in block.split('\n')]
      sizes = [col.count('#') for col in zip(*shematic)]
      first = shematic[0]
      if len(first) == first.count('#'):
        locks.append(sizes)
      else:
        keys.append(sizes)
  return locks, keys


def solve(locks, keys):
  part1 = part2 = 0
  for lock, key in itt.product(locks, keys):
    part1 += all(a + b < 8 for a, b in zip(lock, key))
  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(*load("day25.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.4f} sec.')

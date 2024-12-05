import time, collections as coll


def load(file):
  with open(file) as f:
    a, b = f.read().split('\n\n')
    updates = [list(map(int, line.split(','))) for line in b.splitlines()]

    rules = coll.defaultdict(set)
    for rule in a.splitlines():
      lower, higher = map(int, rule.split('|'))
      rules[lower].add(higher)

    return rules, updates


def solve(rules, updates):
  part1 = part2 = 0
  for update in updates:
    sorted_update = sorted(update, key=lambda x: -len(rules[x] & set(update)))
    if update == sorted_update:
      part1 += update[len(update) // 2]
    else:
      part2 += sorted_update[len(update) // 2]

  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(*load("day05.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

import time, itertools as itt, collections as coll


def load(file):
  friends = coll.defaultdict(set)
  with open(file) as f:
    for row in f.read().split('\n'):
      a, b = row.split('-')
      friends[a].update((a, b))
      friends[b].update((a, b))
  return friends


def solve(p):
  part1 = len({frozenset(comb) for conn in p.values()
               for comb in itt.combinations(conn, 3)
               if all(set(comb).issubset(p[c]) for c in comb) and
               any(t[0] == 't' for t in comb)})

  networks = [{comp} for comp in p]
  for network, comp in itt.product(networks, p):
    if network.issubset(p[comp]): network.add(comp)
  part2 = ','.join(sorted(max(networks, key=len)))

  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day23.txt"))}')
print(f'solved in {time.perf_counter() - time_start:.4f} sec.')

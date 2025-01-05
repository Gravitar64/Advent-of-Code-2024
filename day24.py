#Part 2 based on https://www.reddit.com/r/adventofcode/comments/1hl698z/comment/m3kt1je/ from lscddit

import time


def load(file):
  with open(file) as f:
    top, down = f.read().split('\n\n')
    wires = dict()
    for row in top.split('\n'):
      wire, value = row.split(': ')
      wires[wire] = int(value)
    gates = [row.split() for row in down.split('\n')]
  return wires, gates


def get_errors(gates):
  highest_z = max(g[4] for g in gates)

  errors = set()
  for w1, gate, w2, _, target in gates:
    if target[0] == 'z' and gate != 'XOR' and target != highest_z:
      errors.add(target)

    if gate == 'XOR' and all(w[0] not in ['x', 'y', 'z'] for w in (target, w1, w2)):
      errors.add(target)

    if gate == 'AND' and 'x00' not in [w1, w2]:
      for supw1, supgate, subw2, *_ in gates:
        if (target == supw1 or target == subw2) and supgate != 'OR':
          errors.add(target)
          break

    if gate == 'XOR':
      for supw1, supgate, subw2, *_ in gates:
        if (target == supw1 or target == subw2) and supgate == 'OR':
          errors.add(target)
          break

  return ','.join(sorted(errors))


def get_number(gates, wires):
  ops = {'AND': lambda a, b: a and b, 'OR': lambda a, b: a or b, 'XOR': lambda a, b: a ^ b}

  while gates:
    w1, gate, w2, _, target = gates.pop(0)
    if w1 in wires and w2 in wires:
      wires[target] = ops[gate](wires[w1], wires[w2])
    else:
      gates.append((w1, gate, w2, _, target))

  return ''.join([str(wires[w]) for w in sorted(wires,reverse=True) if w[0] == 'z'])


def solve(wires, gates):
  part2 = get_errors(gates)
  part1 = int(get_number(gates, wires), 2)
  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(*load("day24.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.4f} sec.')

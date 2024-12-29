import time, re, itertools as itt, collections as coll


def load(file):
  with open(file) as f:
    return list(map(int, re.findall('\d+', f.read())))


def mix_prune(s):
  s = (s ^ (s * 64)) % 16777216
  s = (s ^ (s // 32)) % 16777216
  return (s ^ (s * 2048)) % 16777216


def solve(p):
  part1 = part2 = 0
  bananas = coll.defaultdict(int)

  for s in p:
    nums = [s := mix_prune(s) for _ in range(2000)]
    part1 += nums[-1]

    diffs = [b % 10 - a % 10 for a, b in itt.pairwise(nums)]
    first_seen_pat = set()
    for i in range(len(nums) - 4):
      pat = tuple(diffs[i:i + 4])
      if pat in first_seen_pat: continue
      bananas[pat] += nums[i + 4] % 10
      first_seen_pat.add(pat)

  part2 = max(bananas.values())

  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day22.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.4f} sec')

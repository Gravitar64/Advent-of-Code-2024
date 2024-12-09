import time, re


def load(file):
  with open(file) as f:
    return list(map(int, re.findall('\d', f.read())))


def rearrange(p):
  disk = []
  for i, n in enumerate(p):
    disk += [-1] * n if i % 2 else [i // 2] * n
  spaces = [i for i, n in enumerate(disk) if n == -1]
  for i in spaces:
    while disk[-1] == -1: disk.pop()
    if len(disk) <= i: break
    disk[i] = disk.pop()
  return sum(id * i for i, id in enumerate(disk))


def move_files(p):
  files, spaces = dict(), []
  pos = 0
  for i, n in enumerate(p):
    if i % 2:
      spaces.append((pos, n))
    else:
      files[i // 2] = (pos, n)
    pos += n

  for id, (file_pos, file_size) in reversed(files.items()):
    for i, (space_pos, space_size) in enumerate(spaces):
      if space_pos >= file_pos: break
      if file_size > space_size: continue

      files[id] = (space_pos, file_size)
      new_space_size = space_size - file_size

      if new_space_size == 0:
        spaces.pop(i)
      else:
        spaces[i] = (space_pos + file_size, new_space_size)
      break
  return sum(sum(id * n for n in range(p, p + l)) for id, (p, l) in files.items())


def solve(p):
  part1 = rearrange(p)
  part2 = move_files(p)
  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day09.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

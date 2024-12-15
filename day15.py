#move-routine by https://www.reddit.com/user/Effective_Load_6725/

import time


def load(file):
  with open(file) as f:
    map1, movements = f.read().split('\n\n')
    
    movements = movements.replace('\n', '')
    map2 = map1.replace('#', '##').replace('.', '..').replace('O', '[]').replace('@', '@.')
    
    return (map1, map2), movements
  

def move_robot(grid, pos, dir):
  pos += dir
  c = grid[pos]
  if all([c != '#',
          c != 'O' or move_robot(grid, pos, dir), 
          c != '[' or move_robot(grid, pos + 1, dir) and move_robot(grid, pos, dir),
          c != ']' or move_robot(grid, pos - 1, dir) and move_robot(grid, pos, dir)]):
    grid[pos], grid[pos - dir] = grid[pos - dir], grid[pos]
    return True


def solve(maps, movements):
  parts = []
  for act_map in maps:
    grid = {x + y * 1j: c for y, row in enumerate(act_map.split('\n')) for x, c in enumerate(row)}
    pos = [p for p, c in grid.items() if c == '@'][0]
    dirs = {'<': -1, '>': +1, '^': -1j, 'v': +1j}
    
    for move in movements:
      old_grid = grid.copy()
      dir = dirs[move]
      if move_robot(grid, pos, dir): 
        pos += dir
      else: 
        grid = old_grid
    parts.append(int(sum(pos.real + pos.imag * 100 for pos, c in grid.items() if c in 'O[')))
  
  return parts


time_start = time.perf_counter()
print(f'Solution: {solve(*load("day15.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
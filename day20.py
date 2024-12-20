import time


def load(file):
  with open(file) as f:
    walls = set()
    for y,row in enumerate(f.read().split('\n')):
      for x,c in enumerate(row):
        match c:
          case '#': walls.add((x,y))
          case 'S': start = (x,y)
          case 'E': end = (x,y)
    return walls, start, end, x+1, y+1    
  
def out_bound(x,y,w,h):
  return not (0 <= x < w and 0 <= y < h)


def bfs(walls,start,end,w,h):
  queue, seen = [(start,[])], set()
  while queue:
    (x,y),path = queue.pop(0)
    if (x,y) == end: return path
    for new_pos in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
      if new_pos in walls: continue
      if new_pos in seen or out_bound(x,y,w,h): continue
      seen.add(new_pos)
      queue.append((new_pos, path + [new_pos]))

def show_map(walls,path,w,h):
  for y in range(h):
    for x in range(w):
      if (x,y) in walls:
        print('#', end = '')
      elif (x,y) in path:
        print('O', end = '')
      else:
        print('.', end ='')
    print()        

def solve(walls, start, end, w, h):
  part1 = part2 = 0
  path = bfs(walls,start,end,w,h)  
  walls_list = list(walls)
  
  len_path = len(path)
  for i in range(len(walls_list)):
    cheat = set(walls_list[:i] + walls_list[i+1:])
    if len(bfs(cheat,start,end,w,h))-len_path <= -100:
      print(i, walls_list[i], len(walls_list))
      part1 += 1
  
  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(*load("day20.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

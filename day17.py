import time, re


def load(file):
  with open(file) as f:
    return list(map(int, re.findall('\d+', f.read())))


def run_program(a, b, c, program):
  ip, out, l = 0, [], len(program)
  while ip < l:
    opcode, literal = program[ip:ip + 2]
    combo = literal if literal < 4 else [a, b, c][literal - 4]
    ip += 2

    match opcode:
      case 0: a = a // 2 ** combo
      case 1: b ^= literal
      case 2: b = combo % 8
      case 3 if a != 0: ip = literal
      case 4: b ^= c
      case 5: out.append(combo % 8)
      case 6: b = a // 2 ** combo
      case 7: c = a // 2 ** combo
  return out


def find_a(program, a, b, c, prg_pos):
  if abs(prg_pos) > len(program): return a
  for i in range(8):
    first_digit_out = run_program(a * 8 + i, b, c, program)[0]
    if first_digit_out != program[prg_pos]: continue
    if (e := find_a(program, a*8+i, b, c, prg_pos - 1)): return e


def solve(p):
  a, b, c, *program = p
  part1 = run_program(a, b, c, program)
  part2 = find_a(program, 0, b, c, -1)
  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day17.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')

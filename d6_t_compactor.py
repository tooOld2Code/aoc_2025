# Day 6: Trash Compactor
# /learn/aoc_2025/d6_t_compactor.py
import re, math
import numpy as np

fl_pzl_input = '../aoc_2025/d6_math.txt'
fl_tst_input = '../aoc_2025/d6_tst.txt'

# Change to False when finished dev and testing to run on puzzle 
use_test = False
if use_test:
  curr_fl = fl_tst_input
else:
  curr_fl = fl_pzl_input

# part 1
def part_1():
  # modify as needed for current input
  with open(curr_fl, "r") as f:
    d6_vals = []
    for line in f:
      if "+" not in line:
        nbrs = r"(\d+)"
        tmp = re.findall(nbrs, line)
        tmp = list(map(int, tmp))
        d6_vals.append(tmp)
      else:
        ops = r"([+*]+)"
        d6_ops = re.findall(ops, line)
        d6_ops = d6_ops[::-1]

  hwork = np.array(d6_vals)
  hwork = np.rot90(hwork)

  rslt = 0
  for i, nbrs in enumerate(hwork):
    if d6_ops[i] == "+":
      if use_test:
        print(f"{d6_ops[i]} {nbrs} = {sum(nbrs)}")
      rslt += sum(nbrs)
    else:
      if use_test:
        print(f"{d6_ops[i]} {nbrs} = {math.prod(nbrs)}")
      rslt += math.prod(nbrs)
  return rslt


# part 2
def part_2():
  d6_vals, d6_ops = [], []
  with open(curr_fl, "r", encoding="utf-8") as f:
    for line in f:
      if "+" not in line:
        d6_vals.append(line[:-1])
      else:
        ops = r"([\+\*]+)"
        d6_ops = re.findall(ops, line)

  rws, cls = len(d6_vals), len(d6_vals[0])
  rslt = 0
  people_nbrs = []
  nbrs = []
  for j in range(cls-1, -1 , -1):
    if all(d6_vals[r][j].isspace() for r in range(rws)):
      people_nbrs.append(nbrs)
      nbrs = []
      continue
    num = ''
    for i in range(rws):
      if d6_vals[i][j].isnumeric():
        num += d6_vals[i][j]
    nbrs.append(num)
    if j == 0:
      people_nbrs.append(nbrs)


  d6_ops = d6_ops[::-1]
  for i, nbrs in enumerate(people_nbrs):
    if d6_ops[i] == '+':
      rslt += sum(map(int, nbrs))
    else:
      rslt += math.prod(map(int, nbrs))
  return rslt


print(f"Day 6, Part 1: {part_1()}")
print(f"Day 6, Part 2: {part_2()}")

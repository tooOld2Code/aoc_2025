# Day 6: Trash Compactor
# /learn/aoc_2025/d6_t_compactor.py
import re, math
import numpy as np
# import pandas as pd

fl_pzl_input = '../aoc_2025/d6_math.txt'
fl_tst_input = '../aoc_2025/d6_tst.txt'

# with open(fl_pzl_input, "r") as f:
#     d6_vals = [line.strip() for line in f]


# d6_tst = """
# """
# tst_vals = d6_tst.splitlines()


def inp_to_numpy(dD_in):
  rdgs = [[int(bd) for bd in rdg.strip()] for rdg in dD_in]
  r_np = np.array(rdgs)
  return r_np


# Change to False when finished dev and testing to run on puzzle 
use_test = True
if use_test:
  curr_fl = fl_tst_input
else:
  curr_fl = fl_pzl_input

# cnt_rdgs = len(curr_inp)
# nbr_dgts = len(curr_rdgs[0])

# convert data to numpy array if necessary, using function above
# np_d6 = inp_to_numpy(curr_inp)
# or convert data to numeric if necessary, note this is done by pwr_to_numpy() if you are using it
# d6_rdgs = [[int(bd) for bd in rdg] for rdg in d6_vals]

# part 1
def part_1():
  # modify as needed for current input
  with open(curr_fl, "r") as f:
    d6_vals = []
    for line in f:
      # ln = line.strip()
      if "+" not in line:
        nbrs = r"(\d+)"
        tmp = re.findall(nbrs, line)
        # print(tmp)
        tmp = list(map(int, tmp))
        d6_vals.append(tmp)
      else:
        ops = r"([+*]+)"
        d6_ops = re.findall(ops, line)
        d6_ops = d6_ops[::-1]

  # if use_test:
  #   print(d6_vals, "\n", d6_ops)

  hwork = np.array(d6_vals)
  hwork = np.rot90(hwork)

  # if use_test:
  #   print(hwork)

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
  # modify as needed for current input
  with open(curr_fl, "r") as f:
    d6_vals = []
    for line in f:
      # ln = line.strip()
      if "+" not in line:
        nbrs = r"(\d+)"
        tmp = re.findall(nbrs, line)
        # print(tmp)
        # tmp = list(map(int, tmp))
        d6_vals.append(tmp)
      else:
        ops = r"([+*]+)"
        d6_ops = re.findall(ops, line)
        d6_ops = d6_ops[::-1]

  if use_test:
    print(d6_vals, "\n", d6_ops)

  # hwork = np.array(d6_vals)
  # hwork = np.rot90(hwork)

  # if use_test:
  #   print(hwork)

  # for j in range(len(d6_vals)):
  #   print(f"{j}: ", end='')
  #   for i in range(len(d6_vals[0])):
  #     print(f"'{d6_vals[j][i]}'", end="")
  #   print()

  o_nbrs = []
  for i in range(len(d6_vals[0])):
    c_nbrs = []
    for j in range(len(d6_vals)):
      c_nbrs.append(d6_vals[j][i])
    print(c_nbrs)
    # o_nbrs.append(c_nbrs)
  for i in range(len(c_nbrs)):
    n_len = len(c_nbrs[0])
    o_nbr = []
    for j in range(n_len):
      o_nbr.append(c_nbrs[i][j])
    o_nbrs.append(o_nbr)


  print(o_nbrs)
  rslt = 0
  return rslt


print(f"Day X, Part 1: {part_1()}")
print(f"Day X, Part 2: {part_2()}")

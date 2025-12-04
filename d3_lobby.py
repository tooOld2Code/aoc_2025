# Day 3: Lobby
# /learn/aoc_2025/d3_lobby.py

from itertools import combinations as icmb
from time import perf_counter

fl_pzl_input = '../aoc_2025/d3_batteries.txt'
fl_tst_input = '../aoc_2025/d3_tst.txt'


# Change to False when finished dev and testing to run on puzzle 
use_test = False
if use_test:
  curr_fl = fl_tst_input
else:
  curr_fl = fl_pzl_input

# modify as needed for current input
with open(curr_fl, "r") as f:
  d3_vals = [line.strip() for line in f]

# part 1
def part_1():
  rslt = 0
  st_t = perf_counter()
  for t_bat in d3_vals:
    combs = icmb(t_bat, 2)
    mx_j = max(combs)
    mx_jolts = int("".join(mx_j))
    rslt += mx_jolts
    if use_test:
      print(mx_jolts)
  nd_t = perf_counter()
  print(f"combinations loop exec time: {nd_t - st_t}")
  
  rslt2 = 0
  st_t = perf_counter()
  mx_ib = len(d3_vals[0]) - 1
  for t_bat in d3_vals:
    b_mx = max(t_bat)
    i_mx = t_bat.index(b_mx)
    if i_mx == 0:
      t_bat2 = t_bat[1:]
    elif i_mx == mx_ib:
      # b_mx is actually the second digit
      t_bat2 = t_bat[:-1]
    else:
      t_bat2 = t_bat[(i_mx + 1):]
    b_mx2 = max(t_bat2)
    if i_mx != mx_ib:
      mx_jolts = (int(b_mx) * 10) + int(b_mx2)
    else:
      mx_jolts = (int(b_mx2) * 10) + int(b_mx)
    rslt2 += mx_jolts
  nd_t = perf_counter()
  print(f"list parsing loop exec time: {nd_t - st_t}")
  
  return rslt, rslt2


# part 2
def part_2():
  # can't use combinations, will just kill cpu and memory
  rslt = 0
  n_bat = 12
  l_bat = len(d3_vals[0])
  st_t = perf_counter()
  for t_bat in d3_vals:
    b_jolts = []
    s_rng = 0
    e_rng = l_bat - n_bat + 1
    while s_rng + 1 < e_rng <= l_bat:
      srch_rng = t_bat[s_rng:e_rng]
      b_mx = max(srch_rng)
      b_jolts.append(b_mx)
      s_rng += srch_rng.index(b_mx) + 1
      e_rng += 1
    j_mx = int("".join(b_jolts) +  t_bat[e_rng - 1 :])
    rslt += j_mx
  nd_t = perf_counter()
  print(f"parse loop took {nd_t - st_t}")
  return rslt


print(f"Day 3, Part 1: {part_1()}")
print(f"Day 3, Part 2: {part_2()}")

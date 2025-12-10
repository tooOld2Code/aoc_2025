# Day 7: Laboratories
# /learn/aoc_2025/d7_labs.py
from collections import defaultdict
import numpy as np

fl_pzl_input = '../aoc_2025/d7_manifold.txt'
fl_tst_input = '../aoc_2025/d7_tst.txt'

# Change to False when finished dev and testing to run on puzzle 
use_test = False
if use_test:
  curr_fl = fl_tst_input
else:
  curr_fl = fl_pzl_input

# modify as needed for current input
with open(curr_fl, "r") as f:
  d7_vals = f.read().splitlines()

# get dict of all roll locations as complex numbers (x = col, y = row)
spltrs = {complex(col, row) for row, r_spltrs in enumerate(d7_vals) for col, sym in enumerate(r_spltrs) if sym == '^'}


# part 1
def solve():
  rslt = 0
  ln, wd = len(d7_vals), len(d7_vals[0])
  strt = complex(d7_vals[0].index('S'), 0)
  rays = {strt, }
  mani = defaultdict(int)
  mani[int(strt.real)] = 1
  for i in range(ln-1):
    rays = {ray + 1j for ray in rays}
    fnd_spltrs = rays & spltrs
    rslt += len(fnd_spltrs)
    n_rays = []
    for spltr in fnd_spltrs:
      n_rays.append(spltr - 1)
      n_rays.append(spltr + 1)
      rays.discard(spltr)
      b_src= int(spltr.real)
      if b_src in mani:
        mani[b_src - 1] += mani[b_src]
        mani[b_src + 1] += mani[b_src]
        del mani[b_src]

    rays.update(n_rays)
  return rslt, sum(mani.values())


print(f"Day 7, Part 1 & 2: {solve()}")

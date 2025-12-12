# Day 10: Factory
# /learn/aoc_2025/d10_factory.py
import itertools
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


def le_solve(jlts, btns):
  jolts = np.array(jlts)
  n_b, n_j = len(btns), len(jolts)
  l_eqs = np.zeros((n_j, n_b))
  for i in range(n_j):
    for j in range(n_b):
      if i in btns[j]:
        l_eqs[i, j] = 1
  cost = np.ones(n_b)
  cnst = LinearConstraint(l_eqs, jolts, jolts)
  intg = np.ones(n_b)
  bnds = Bounds(lb=0, ub=np.inf)
  soln = milp(c=cost, constraints=cnst, integrality=intg, bounds=bnds)

  return np.sum(np.round(soln.x).astype(int))


fl_pzl_input = '../aoc_2025/d10_manual.txt'
fl_tst_input = '../aoc_2025/d10_tst.txt'

# Change to False when finished dev and testing to run on puzzle 
use_test = False
if use_test:
  curr_fl = fl_tst_input
else:
  curr_fl = fl_pzl_input

# modify as needed for current input
with open(curr_fl, "r") as f:
  d10_vals = [line.strip() for line in f]

# convert light and button info to binary so can
# use XOR to toggle button combinations for part 1
num_lts, trgts, btns, b_masks, jolts = [], [], [], [], []
for ln in d10_vals:
  lgt_nd = ln.find("]")
  btn_nd = ln.find("{")
  t_t = ln[1:lgt_nd]
  num_lts.append(len(t_t))
  b_trgt = 0
  # note this in fact reverses the order of lights
  for i, char in enumerate(t_t):
    if char == '#': 
      b_trgt |= (1 << i)
  trgts.append(b_trgt)
  t_btns = ln[lgt_nd+2:btn_nd-1]
  b_list = t_btns.split(" ")
  b_locs = []
  for btn in b_list:
    locs = [int(x) for x in btn[1:-1].split(",")]
    mask = 0
    for ndx in locs:
      mask |= (1 << ndx)
    b_locs.append(locs)
  btns.append(b_locs)

  btn_masks = [sum(1 << i for i in locs) for locs in b_locs]
  b_masks.append(btn_masks)
  # for part 2 need the power/jolt rqts
  s_j = ln[btn_nd+1:-1]
  t_j = [int(j) for j in s_j.split(",")]
  jolts.append(t_j)


# part 1
def part_1():
  rslt = 0
  for i, c_masks in enumerate(b_masks):
    flg = False
    n_bt = len(c_masks)
    for n_k in range(n_bt + 1):
      for cmb_prs in itertools.combinations(b_masks[i], n_k):
        lt_state = 0
        for mask in cmb_prs:
          # XOR effectively toggles the appropriate switches
          lt_state ^= mask
          if lt_state == trgts[i]:
            rslt += n_k
            flg = True
            break
        if flg:
          break          
      if flg:
        break          
  return rslt


# part 2
def part_2():
  rslt = 0
  for i, m_jlt in enumerate(jolts):
    n_prss = le_solve(m_jlt, btns[i], dbg_p=False)
    rslt += n_prss
  return rslt


print(f"Day 10, Part 1: {part_1()}")
print(f"Day 10, Part 2: {part_2()}")

# Day 11: Reactor
# /learn/aoc_2025/d11_reactor.py
from functools import cache

fl_pzl_input = '../aoc_2025/d11_paths.txt'
fl_tst_inputs = ['../aoc_2025/d11_tst.txt', '../aoc_2025/d11_tst2.txt']

# Change to False when finished dev and testing to run on puzzle 
use_test = False
n_prt = 2
if use_test:
  if n_prt == 1:
    curr_fl = fl_tst_inputs[0]
  else:
    curr_fl = fl_tst_inputs[1]
else:
  curr_fl = fl_pzl_input

# modify as needed for current input
with open(curr_fl, "r") as f:
  d11_vals = [line.strip() for line in f]

dvc_conns = {}
for ln in d11_vals:
  dvc, _, dstns = ln.partition(": ")
  dvc_conns[dvc] = set(dstns.split(" "))

if use_test:
  for k, v in dvc_conns.items():
    print(f"{k}: {v}")

# part 1
def part_1():
  def cnt_pths(d_from, d_to):
    if d_from == d_to:
      return 1
  
    return(sum(cnt_pths(d_nxt, d_to) for d_nxt in dvc_conns[d_from]))


  return(cnt_pths("you", "out"))    


# part 2
def part_2():

  @cache
  def cnt_pths(d_from, d_to, thru_dac, thru_fft):
    if d_from == d_to:
      return thru_dac and thru_fft
  
    return(sum(
      cnt_pths(
        d_nxt,
        d_to,
        thru_dac or d_nxt=="dac",
        thru_fft or d_nxt=="fft",
      ) for d_nxt in dvc_conns[d_from]))


  return(cnt_pths("svr", "out", False, False))


if n_prt == 1:
  print(f"Day 11, Part 1: {part_1()}")
else:
  print(f"Day 11, Part 2: {part_2()}")

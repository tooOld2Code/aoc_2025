# Day 1: Secret Entrance
# /learn/aoc_2025/d1_secret_in.py

fl_pzl_input = '../aoc_2025/d1_turns.txt'
fl_tst_input = '../aoc_2025/d1_tst.txt'

# Change to False when finished dev and testing to run on puzzle 
use_test = False
if use_test:
  curr_fl = fl_tst_input
else:
  curr_fl = fl_pzl_input

# modify as needed for current input
with open(curr_fl, "r") as f:
  dX_vals = [line.strip() for line in f]

d_sz = 100  # number of values on dial, 0-99
d_dir = {'L': -1, 'R': +1}


# part 1
def part_1():
  d_pos = 50  # starting location
  rslt = 0
  for rot in dX_vals:
    r_dir, r_sz = rot[0], rot[1:]
    d_rot = int(r_sz) * d_dir[r_dir]
    d_pos = (d_pos + d_rot) % d_sz
    if d_pos == 0:
      rslt += 1
  return rslt


# part 2
def part_2():
  def did_cross_0(p_pos, d_rot):
    """ Determine how often the 0 position is clicked while executing the specified dial rotation

      params:
        p_pos: previous/starting dial position
        d_rot: dial rotation, int, negative if moving left, positive otherwise
    
      returns: number of times 0 clicked
    """
    d_mv = abs(d_rot)
    # account for rotation amount greater than the dial size
    n_cs = d_mv // d_sz # number of hundreds in rotation amount
    b_rot = d_rot       # base rotation amount, the value without the extra hundreds of steps
    if n_cs > 0:
      if b_rot >= 0:
        b_rot = d_rot % d_sz
      else:
        b_rot = d_rot + (d_sz * n_cs)
    tst = p_pos + b_rot
    z_clk = False
    # don't double count if final position is zero
    if tst < 0 and p_pos != 0:
      z_clk = True
    else:
      if d_rot > 0 and p_pos <= 99 and tst > d_sz:
        z_clk = True
    if z_clk:
      return n_cs + 1
    else:
      return n_cs


  d_pos = 50  # starting location

  rslt = 0
  d_dir = {'L': -1, 'R': +1}
  for rot in dX_vals:
    r_dir, r_sz = rot[0], rot[1:]
    d_rot = int(r_sz) * d_dir[r_dir]
    tst = did_cross_0(d_pos, d_rot)
    if tst:
      rslt += tst
    d_pos = (d_pos + d_rot) % d_sz
    if d_pos == 0:
      rslt += 1
  return rslt


print(f"Day 1, Part 1: {part_1()}")
print(f"Day 1, Part 2: {part_2()}")

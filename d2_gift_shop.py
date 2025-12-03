# Day 2: Gift Shop
# /learn/aoc_2025/d2_gift_shop.py

fl_pzl_input = '../aoc_2025/d2_ids.txt'
fl_tst_input = '../aoc_2025/d2_tst.txt'

# Change to False when finished dev and testing to run on puzzle 
use_test = False
if use_test:
  curr_fl = fl_tst_input
else:
  curr_fl = fl_pzl_input

# modify as needed for current input
with open(curr_fl, "r") as f:
  f_id_rngs = f.readline().strip()
  d2_id_rngs = f_id_rngs.split(",")


# part 1
def part_1():
  rslt = 0
  r_ids = []
  for id_rng in d2_id_rngs:
    s_st, s_nd = id_rng.split("-")
    for t_id in range(int(s_st), int(s_nd) + 1):
      s_id = str(t_id)
      if len(s_id) % 2 == 0:
        ndx_mid = len(s_id) // 2
        lh, rh = s_id[:ndx_mid], s_id[ndx_mid:]
        if lh == rh:
          rslt += t_id

  return rslt


# part 2
def part_2():
  def chk_4_2heq(s_id):
    rtn = False
    ndx_mid = len(s_id) // 2
    lh, rh = s_id[:ndx_mid], s_id[ndx_mid:]
    if lh == rh:
      rtn = True
    return(rtn)  


  def chk_4_rpts(s_id):
    rtn = False
    l_id = len(s_id)
    for i in range(1, (l_id // 2) + 1):
      t1 = s_id[:i] * (l_id // i)
      if s_id == t1:
        rtn = True
        break

    return(rtn)  

  
  rslt = 0
  for id_rng in d2_id_rngs:
    s_st, s_nd = id_rng.split("-")
    for t_id in range(int(s_st), int(s_nd) + 1):
      s_id = str(t_id)
      if len(s_id) % 2 == 0:
        is_2heq = chk_4_2heq(s_id)
        if is_2heq:
          rslt += t_id
          continue
      is_reps = chk_4_rpts(s_id)
      if is_reps:
        rslt += t_id
        continue

  return rslt


print(f"Day X, Part 1: {part_1()}")
print(f"Day X, Part 2: {part_2()}")

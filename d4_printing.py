# Day 4: Printing Department
# /learn/aoc_2025/d4_printing.py
# Used algorithm I saw in solution for problem in AOC 2024.
# Had added it to the file with my less than brilliant solution.
# Really liked the use of complex numbers for map locations. So simple.
# And you've got to love the added simplicity of using set theory to get
# the rolls accessible to the forklifts.

fl_pzl_input = '../aoc_2025/d4_rolls.txt'
fl_tst_input = '../aoc_2025/d4_tst.txt'

# Change to False when finished dev and testing to run on puzzle 
use_test = False
if use_test:
  curr_fl = fl_tst_input
else:
  curr_fl = fl_pzl_input

# modify as needed for current input
with open(curr_fl, "r") as f:
  d4_vals = f.read().splitlines()

# get dict of all roll locations as complex numbers (x = col, y = row)
rolls = {complex(col, row) for row, r_syms in enumerate(d4_vals) for col, sym in enumerate(r_syms) if sym == '@'}
# get position as complex nbr for all possible neighbours of each roll in rolls dictionary
neighbours = {r: {r+complex(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if x or y} for r in rolls}


# part 1
def part_1():
  # for each roll in rolls dict, get intersection of possible neigbours and all rolls
  # if length of intersection < 4, roll is accessible by forklift
  can_rmv = {r for r in rolls if len(neighbours[r] & rolls)<4}
  return(len(can_rmv))


# part 2
def part_2():
  global rolls
  fl_rolls = []
  # repeat until no more rolls are forklift accessible
  # been wanting to use this 'new' operator for awhile
  while can_rmv := {r for r in rolls if len(neighbours[r] & rolls)<4}:
    fl_rolls.append(len(can_rmv))
    rolls -= can_rmv
  return(sum(fl_rolls))


print(f"Day X, Part 1: {part_1()}")
print(f"Day X, Part 2: {part_2()}")

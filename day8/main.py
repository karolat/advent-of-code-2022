# count the number of trees that are visible from outside the grid when looking directly along a row or column

# input data into 2 dimensional array
def read_input() -> list:
  with open('day8/input.txt') as f:
    grid = f.read().splitlines()
    grid = [list(line) for line in grid]
  return grid

def check_if_tree_visible(y: int, x: int, grid: list) -> bool:
  tree_length = int(grid[y][x])
  # check up
  visible_top = True
  for i in range(y-1, -1, -1):
    if grid[i][x] >= tree_length:
      visible_top = False
      break
  # check down
  visible_bottom = True
  for i in range(y+1, len(grid)):
    if grid[i][x] >= tree_length:
      visible_bottom = False
      break
  # check left
  visible_left = True
  for i in range(x-1, -1, -1):
    if grid[y][i] >= tree_length:
      visible_left = False
      break
  # check right
  visible_right = True
  for i in range(x+1, len(grid[y])):
    if grid[y][i] >= tree_length:
      visible_right = False
      break
  return visible_top or visible_bottom or visible_left or visible_right

def get_visibility_score(y: int, x: int, grid: list) -> int:
  tree_length = int(grid[y][x])
  # check up
  top_score = 0
  for i in range(y-1, -1, -1):
    top_score += 1
    if grid[i][x] >= tree_length:
      break
  # check down
  bottom_score = 0
  for i in range(y+1, len(grid)):
    bottom_score += 1
    if grid[i][x] >= tree_length:
      break
  # check left
  left_score = 0
  for i in range(x-1, -1, -1):
    left_score += 1
    if grid[y][i] >= tree_length:
      break
  # check right
  right_score = 0
  for i in range(x+1, len(grid[y])):
    right_score += 1
    if grid[y][i] >= tree_length:
      break
  return top_score * bottom_score * left_score * right_score


def main():
  grid = read_input()
  # turn all chars into ints
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      grid[y][x] = int(grid[y][x])

  # for each cell, check if there is a clear path to the edge of the grid
  # if there is, add 1 to the count
  count = 0
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      if check_if_tree_visible(y, x, grid):
        count += 1
  print(f'Number of trees visible from outside the grid: {count}')

  # for each cell, calculate the score
  # print the highest score
  top_score = 0
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      score = get_visibility_score(y, x, grid)
      if score > top_score:
        top_score = score
  print(f'Highest possible score: {top_score}')

if __name__ == '__main__':
  main()
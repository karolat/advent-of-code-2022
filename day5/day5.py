import re

def find_stack_labels(lines: list) -> int:
  for i, line in enumerate(lines):
    if line[1] == '1':
      return i

def get_input() -> list:
  with open('input.txt') as f:
    lines = f.readlines()
  return lines

def create_stacks(label_line: list) -> list:
  stacks_dict = {}
  labels = [x for x in label_line[1::4]]
  for label in labels:
    stacks_dict[int(label)] = []
  return stacks_dict

def populate_stacks(stacks: list, label_line: list) -> dict:
  stacks_dict = create_stacks(label_line)
  for line in stacks[::-1]:
    for i, crate in enumerate(line[1::4]):
      if crate != ' ':
        stacks_dict[i+1].append(crate)
  return stacks_dict

def perform_moves(stacks_dict: dict, moves: list) -> dict:
  pattern = r'\d+'
  for move in moves:
    amount, from_stack, to_stack = [int(x) for x in re.findall(pattern, move)]
    for _ in range(int(amount)):
      stacks_dict[to_stack].append(stacks_dict[from_stack].pop())
  return stacks_dict

def get_tops(stacks_dict: dict) -> str:
  tops = ''
  for stack in stacks_dict.keys():
    if len(stacks_dict[stack]) > 0:
      tops += stacks_dict[stack][-1]
  return tops

def perform_moves_9001(stacks_dict: dict, moves: list) -> dict:
  pattern = r'\d+'
  for move in moves:
    amount, from_stack, to_stack = [int(x) for x in re.findall(pattern, move)]
    stacks_dict[to_stack].extend(stacks_dict[from_stack][-amount:])
    stacks_dict[from_stack] = stacks_dict[from_stack][:-amount]
  return stacks_dict

def main():
  # read in the input
  lines = get_input()

  # find line with stack labels, and split into stacks, labels, and directions
  label_line = find_stack_labels(lines)
  stacks = lines[:label_line]
  moves = lines[label_line+2:]
  label_line = lines[label_line]

  stacks_dict = populate_stacks(stacks, label_line)
  stacks_dict = perform_moves(stacks_dict, moves)

  tops = get_tops(stacks_dict)
  print(f'Part 1 tops: {tops}')

  # part 2
  stacks_dict = populate_stacks(stacks, label_line)
  stacks_dict = perform_moves_9001(stacks_dict, moves)
  tops = get_tops(stacks_dict)
  print(f'Part 2 tops: {tops}')

if __name__ == '__main__':
  main()

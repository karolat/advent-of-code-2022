from functools import reduce

def get_input(filename: str) -> list:
  with open(filename, 'r') as f:
    lines = f.readlines()
  return lines

def ls_to_dict(lines: list, file_stucture: dict, line_number: int) -> tuple[dict, int]:
  for i, line in enumerate(lines[line_number:]):
    line = line.strip()
    if line.startswith('$'):
      next_line = line_number + i
      return file_stucture, next_line

    if line.startswith('dir'):
      file_stucture[line.split(' ')[1]] = {}

    elif line.split(' ')[0].isnumeric():
      file_stucture[line.split(' ')[1]] = int(line.split(' ')[0])

  return file_stucture, len(lines)

def recursive_parse_lines(lines: list, i: int, file_structure: dict = {'/': {}}) -> dict | tuple[dict, int]:
  if i >= len(lines):
    return file_structure, i+1
  line = lines[i].strip().split(' ')
  if line[0] == '$':
    if line[1] == 'ls':
      file_structure, next_line = ls_to_dict(lines, file_structure, i+1)
      return recursive_parse_lines(lines = lines, i = next_line, file_structure = file_structure)

    if line[1] == 'cd':
      if line[2] != '..':
        file_structure[line[2]], next_line = recursive_parse_lines(lines, i+1, file_structure[line[2]])
        if next_line >= len(lines):
          return file_structure, next_line
        return recursive_parse_lines(lines = lines, i = next_line, file_structure = file_structure)

      else:
        return file_structure, i+1

  return file_structure

def determine_dir_size(file_structure: dict) -> int:
  current_dir_size = 0
  for key, value in file_structure.items():
    if isinstance(value, int):
      current_dir_size += value
    else:
      current_dir_size += determine_dir_size(value)
  return current_dir_size

def get_dir_sizes(file_structure: dict, dir_sizes: list[int] = []) -> list[int]:
  for key, value in file_structure.items():
    if isinstance(value, dict):
      dir_sizes.append(determine_dir_size(value))
      dir_sizes = get_dir_sizes(value, dir_sizes)
  return dir_sizes

def sum_dirs(size1: int, size2: int) -> int:
  if size2 > 100000:
    return size1 + size2
  else:
    return size2

def get_best_dir_to_delete(dir_sizes: list[int], need_to_free: int) -> int:
  dir_sizes.sort()
  for size in dir_sizes:
    if size >= need_to_free:
      return size
  return -1


# Three cases:
# 1. $ ls = done correctly
# 2. $ cd = done correctly
# 3. $ cd .. = need to go up one level and return execution at the correct place

def main():
  # Part 1
  lines = get_input('day7/input.txt')
  file_structure, _ = recursive_parse_lines(lines, 0)
  dir_sizes = get_dir_sizes(file_structure)
  sum_of_dir_sizes = reduce(sum_dirs, dir_sizes)
  print(f'Sum of dir sizes: {sum_of_dir_sizes}')

  # Part 2
  required_space = 30000000
  total_capacity = 70000000
  free_space = total_capacity - dir_sizes[0]
  need_to_free = required_space - free_space
  print(f'Best dir to delete: {get_best_dir_to_delete(dir_sizes, need_to_free)}')

if __name__ == '__main__':
  main()
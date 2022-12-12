import json

def get_input(filename: str) -> list:
  with open(filename, 'r') as f:
    lines = f.readlines()
  return lines

def ls_to_dict(lines: list, file_stucture: dict, line_number: int) -> dict:
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

def recursive_parse_lines(lines: list, i: int, file_structure: dict) -> dict:
  print(f'line number: {i}')
  print(f'file structure: {file_structure}')
  if i >= len(lines):
    return file_structure
  line = lines[i].strip().split(' ')
  if line[0] == '$':
    if line[1] == 'ls':
      file_structure, next_line = ls_to_dict(lines, file_structure, i+1)
      return recursive_parse_lines(lines, next_line, file_structure)
    if line[1] == 'cd':
      if line[2] != '..':
        print('going nested')
        file_structure[line[2]] = recursive_parse_lines(lines, i+1, file_structure[line[2]])
      else:
        print(file_structure)
        print('going up')
        return

  return file_structure

# Three real cases:
# 1. $ ls
# 2. $ cd
# 3. $ cd ..

def main():
  lines = get_input('day7/input.txt')
  file_structure = {}
  file_structure = recursive_parse_lines(lines, 1, file_structure)
  #print(file_structure)
  #print(json.dumps(file_structure, indent=2))

if __name__ == '__main__':
  main()
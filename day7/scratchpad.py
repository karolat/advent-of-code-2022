
def get_input(filename: str) -> list:
  with open(filename, 'r') as f:
    lines = f.readlines()
  return lines

def get_total_size(lines: list) -> int:
  total_size = 0
  for line in lines:
    # check if string is numeric
    if line.split(' ')[0].isnumeric() and int(line.split(' ')[0]) <= 100000:
      total_size += int(line.split(' ')[0])
  return total_size

def main():
  lines = get_input('input.txt')
  total_size = get_total_size(lines)
  print(f'sum of total sizes: {total_size}')


if __name__ == '__main__':
  main()

# directory structure
directory = {
  '/': {

  }
}

def create_directory_structure(lines: list) -> dict:
  directory = {}
  for i, line in enumerate(lines):
    if line.split(' ')[1] == 'cd':
      directory[line.split(' ')[2]] = create_directory_structure(lines[i+1:])
      # now we'd like to continue loop after cd ..

  return directory

def parse_lines(lines: list) -> dict:
  file_system = {}
  for i, line in enumerate(lines):
    line = line.strip()



'''
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
'''

def ls_to_dict(lines: list) -> dict:
  directory = {}
  for line in lines:
    line = line.strip()
    if line.startswith('dir'):
      directory[line.split(' ')[1]] = {}
    elif line.split(' ')[0].isnumeric():
      directory[line.split(' ')[1]] = int(line.split(' ')[0])


directory = {
  'a': {},
  'b.txt': 14848514,
  'c.dat': 8504156,
  'd': {}
}
def load_file():
  with open('input.txt') as f:
    return f.read()


def part_1():
  lines = load_file()

  for i in range(4, len(lines)):
    char_set = set()

    # use a set to check if there are 4 unique characters
    for j in range(i-4, i):
      char_set.add(lines[j])

    if len(char_set) == 4:
      print(f'part 1\nfirst marker after character {i}')
      return


def part_2():
  lines = load_file()

  for i in range(14, len(lines)):
    char_set = set()

    for j in range(i-14, i):
      char_set.add(lines[j])

    if len(char_set) == 14:
      print(f'part 2\nfirst marker after character {i}')
      return

def main():
  part_1()
  part_2()

if __name__ == '__main__':
  main()
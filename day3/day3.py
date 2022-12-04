print(3//2)

def get_char_priority(char) -> int:
  if char.isupper():
    return ord(char) - 38
  elif char.islower():
    return ord(char) - 96
  else:
    return 0

# determine which characters are in two strings
def get_common_chars(str1, str2) -> set:
  common_chars = set()
  for char in str1:
    if char in str2:
      common_chars.add(char)
  return common_chars

def get_common_chars_from_3_strings(str1, str2, str3) -> set:
  common_chars = get_common_chars(str1, str2)
  common_chars = common_chars.intersection(get_common_chars(str2, str3))
  common_chars = common_chars.intersection(get_common_chars(str1, str3))
  return common_chars

# split string in two halves
def split_string(str) -> list:
  return str[:len(str)//2], str[len(str)//2:]

# read lines from files into list
def read_lines_from_file(filename) -> list:
  with open(filename) as file:
    return file.readlines()

def main():
  # part 1
  sum_of_priorities = 0
  lines = read_lines_from_file('input.txt')
  for line in lines:
    first_half, second_half = split_string(line)
    common_chars = get_common_chars(first_half, second_half)
    for char in common_chars:
      sum_of_priorities += get_char_priority(char)
  print(f'Sum of priorities: {sum_of_priorities}')

  # part 2
  # for every 3 lines,
  # determine which characters are in all 3 lines
  # and add their priorities
  sum_of_priorities = 0
  for i in range(0, len(lines), 3):
    common_chars = get_common_chars_from_3_strings(lines[i], lines[i+1], lines[i+2])
    for char in common_chars:
      sum_of_priorities += get_char_priority(char)
  print(f'Sum of badge priorities: {sum_of_priorities}')


if __name__ == "__main__":
  main()
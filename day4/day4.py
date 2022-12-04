def return_section_assignments(line):
  first_half, second_half = line.split(',')
  section_a_min, section_a_max = first_half.split('-')
  section_b_min, section_b_max = second_half.split('-')
  section_a = list(range(int(section_a_min), int(section_a_max) + 1))
  section_b = list(range(int(section_b_min), int(section_b_max) + 1))
  return section_a, section_b

def read_lines_from_file(filename) -> list:
  with open(filename) as file:
    return file.readlines()

def main():
  # part 1
  overlap_sum, subset_sum = 0, 0
  lines = read_lines_from_file('input.txt')
  for line in lines:
    section_a, section_b = return_section_assignments(line)
    # part 1
    if set(section_a).issubset(set(section_b)) or set(section_b).issubset(set(section_a)):
      subset_sum += 1
    # part 2
    if section_a.__contains__(section_b[0]) or section_b.__contains__(section_a[0]):
      overlap_sum += 1
  print(f'Number of pairs including a subset: {subset_sum}')
  print(f'Number of pairs including an overlap: {overlap_sum}')

if __name__ == "__main__":
  main()
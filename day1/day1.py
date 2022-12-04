# input text from file
with open('input.txt') as f:
  input = f.read()

# split input into list of strings
input = input.split('\n')

calories_array = []
placeholder = 0
for num in input:
  if num == '':
    calories_array.append(placeholder)
    placeholder = 0
  else:
    placeholder += int(num)

# Part 1
print(f'The elf with the most calories has {max(calories_array)} calories')

# Part 2
print(f'The top 3 elves with the most calories have {sum(sorted(calories_array, reverse=True)[:3])} calories')
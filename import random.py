import random

num = int(input("How many random numbers would you like to generate? "))

with open('random_numbers.txt', 'w') as f:
  for i in range(num):
    f.write(str(random.randint(1, 500)) + '\n')

print("Random numbers written to random_numbers.txt")

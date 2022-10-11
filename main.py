# task 5
color_list = ["Red", "Green", "White", "Black"]
print(color_list[0], color_list[len(color_list) - 1])
# task 6
i = 1
while i <= 10:
    print("*" * i)
    i += 1
# task 7
j = 10
while j >= 1:
    print("*" * j)
    j -= 1
# task 8
import random

print("Guess the number")
number = random.randint(1, 20)

while True:
    line = input('> ')
    line = int(line)
    if line == number:
        break
    else:
        if line < number:
            print("Your guess is low.")
        else:
            print("Your guess is high.")

    print(line)
print('Done!')
# task 9
n = 10
for i in range(n):
    if i <= int(n / 2):
        for j in range(i):
            print('* ', end="")
    else:
        for j in range(-1, 0, i):
            print("* ", end="")
    print('')

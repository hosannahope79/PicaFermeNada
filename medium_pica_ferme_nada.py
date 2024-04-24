from random import randint

print("Welcome to Pica Ferme Nada!")
print()
def print_instructions():
  print("This game is a test of your logic and guessing skills. I will generate a five-digit number and you will attempt to guess it. After each guess, I will give you a code:")
  print("A 'P' stands for the right number in the wrong place.")
  print("An 'F' stands for the right number in its correct spot.")
  print("An 'N' stands for a wrong number.")
  print("The order of these letters is not in the particular order of the digits of the number that you guess. Your goal is to guess the number in the least amount of attempts possible. Good luck!")

answer = str(input("Would you like the instructions? (Yes/No) ")).lower()
if answer == "yes":
  print_instructions()
elif answer == "who asked":
  print("Come on, that was disrespectful. I'm going to try and purposely make it harder for you to win.")
digit_1 = randint(0, 9)
digit_2 = randint(0, 9)
digit_3 = randint(0, 9)
digit_4 = randint(0, 9)
digit_5 = randint(0, 9)
number = [digit_1, digit_2, digit_3, digit_4, digit_5]
turn_number = 0
for turn in range(1000):
  guess = str(input("Type your guess: "))
  indice = 0
  code = ""
  p_count = 0
  f_count = 0
  n_count = 0
  for char in guess:
    if int(char) == number[indice]:
      f_count += 1
    elif int(char) in number:
      p_count += 1
    else:
      n_count += 1
    indice += 1
  code = ("p" * p_count) + ("f" * f_count) + ("n" * n_count)
  turn_number += 1
  print(code)
  if code == "fffff":
    if turn_number == 1:
      print("Dude HOW did you guess my number on the FIRST try?!")
    else:
      print("Congratulations! You guessed my number in " + str(turn_number) + " tries!")
    break
  elif p_count > 3 or f_count > 3 or n_count < 2:
    print("Come on, you're getting closer!")
  else:
    print("Sorry, that's not my number.")
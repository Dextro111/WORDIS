import random

# Defining Important Variables
game_name = "WORDIS"
world_bank = []

with open("Testwords.txt") as wordfile:
  for line in wordfile:
    world_bank.append(line.rstrip().lower())
    
selected_word = random.choice(world_bank)

misplaced_letters=[]
incorrect_letters= []

max_turns = 6
used_turns = 0

print("Welcome To WORDIS!")
print("The Goal is to Guess What the Correct WORD IS! ")
print(f"You have {max_turns} turns to guess! \n")

# Game Loop

while used_turns < max_turns:
  guess = input("Guess the Word!:  \n")
  
  if guess == "stop":
    break
  
  if len(guess) != len(selected_word) or not guess.isalpha():
    print(f"Please enter a {len(selected_word)} letter word!")
    continue
  
  index = 0
  for letter in guess:
    if letter == selected_word[index]:
      print(letter, end='')
      
      if letter in misplaced_letters:
        misplaced_letters.remove(letter)
      
    elif letter in selected_word:
      if letter not in misplaced_letters:  
        misplaced_letters.append(letter)
      print('_', end='')
      
    else:
      if letter not in incorrect_letters:
        incorrect_letters.append(letter)
      print('_', end='')

    index += 1
    
    
# Win Condition
  if guess == selected_word:
    print("\nCongratulations You guessed correctly!")
    break
  
  used_turns += 1
  if used_turns == max_turns:
    print("\nGAME OVER")
    print("You Lost")
    print(f"The Word is {selected_word}")
    break
  
  print('\n')
  print(misplaced_letters)
  print(incorrect_letters)
  print(f"{max_turns-used_turns} Turns Left \n")
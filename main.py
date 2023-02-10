#Step 2

import random
from arts import stages
from arts import logo
from word_list import word_list

chosen_word = random.choice(word_list)

#Testing code


#TODO-1: - Create an empty List called display.
display=[]
#For each letter in the chosen_word, add a "_" to 'display'.

for _ in range(len(chosen_word)):
  display+='_'

#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.


#TODO-2: - Loop through each position in the chosen_word;

#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
end_reach=False
alive=7
letters=[]
print(logo)


while not end_reach:
  guess = input("Guess a letter: ").lower()

  for postition in range(len(chosen_word)):
    if display[postition]==guess:
      print('Already guessed')
      alive-=1
      print(stages[alive])
      break
      
    if chosen_word[postition] == guess:
      display[postition]=guess
      letters+=guess

  if guess not in chosen_word:
    alive-=1
    print(stages[alive])

  print('\n')
  print((' ').join(display))
  print('\n')

  if alive==0:
    print('You failed!')
    print('The word is acutally '+chosen_word)
    end_reach=True
  
  if('_' not in display):
    print('\nYou Sucess!!')
    
    end_reach=True


#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".


#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

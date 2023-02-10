#Step 2

import random   #import random from library which is already pre-built

from arts import stages,logo   #import from arts.py
from word_list import word_list  #import form word_list.py

#generate a random to choose any word from word_list
chosen_word = random.choice(word_list)

#display the word which you guess
#make sure empty array in display
display=[]


#For each letter in the chosen_word, add a "_" to 'display'.
for _ in range(len(chosen_word)):
  display+='_'

#check if the end of game is finsihed or not yet.
#make sure to assign false as it starts game.
end_game=False

#only 7 times left you can play which you have error.
alive=7

#save letter which you type and guess
letters=[]

#show logo from arts.py
print(logo)

#Check if it has reached the game or not yet
#if it has not finised, then go on running like looping
#if it has the end of game, then stop it.

while not end_game:
  
  #input from user
  guess = input("Guess a letter: ").lower()
  
  #check if it is matche or not
  for postition in range(len(chosen_word)):

    #make sure you have not written the same letter or character twice or more time
    #it is used to check if you have written the same letter, it show 'Already guessed' and also 1       point deduced alive.
    if display[postition]==guess:
      print('Already guessed')
      alive-=1
      print(stages[alive])
      break

    #check if it is match or not
    #if it is true match, then save and assingn value to display with postition
    if chosen_word[postition] == guess:
      display[postition]=guess
      letters+=guess

  #check if the letter you type is not contain in chosen_word.
  # if it is true that your letter is not contain in chosen_word. it applies 1 point to deduce alive
  if guess not in chosen_word:
    alive-=1
    print(stages[alive])

  #show the the group of letters you guess
  print('\n')
  print((' ').join(display))
  print('\n')

  #if alive is equal to 0, it means you fail. no more game as hang man is already gone.
  if alive==0:
    print('You failed!')
    print('The word is acutally '+chosen_word)
    end_game=True

  #if the word is perfect from your guess, it means you win the game and the end of game.
  if('_' not in display):
    print('\nYou Won!!')
    end_game=True

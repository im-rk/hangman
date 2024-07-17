#we are going to take a list of words
import random
from words import lis
from hangamn_art import stages,logo

print(logo)
lives=6
#choosen word
choosen_word=random.choice(lis)
print(choosen_word)
#user guess


#to add a underscore to a empty list for each letter in choosen word.
display=[]
for i in choosen_word:
    display.append('_')

while True:
    guess=input('Guess a letter:').lower()
    if guess in display:
        print('you have already guessed it.')
    for i in range(len(choosen_word)):
         if choosen_word[i]==guess:
            display[i]=guess
            for i in display:
                print(i,end=' ')
         else:
            pass


    #if the guessed letter is not in choosen word then we have to reduce the lives by 1

    if guess not in choosen_word:
        print(f"you guessed {guess},that's not in the word.You lose a life.")
        lives-=1
        if lives==0:
            print(stages[lives])
            print('you lose')
            break
    print(stages[lives])
    if '_' not in display:
        print('you won')
        break





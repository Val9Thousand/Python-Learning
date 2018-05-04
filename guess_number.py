import random
#Removed following block of code in order to create a central game hub script
#print('Greetings User. Would you like to play a game?')
#play_game = input('Enter Y or N: ')
#if play_game == 'Y' or play_game == 'y':
#    print("Great! Let\'s play!")
#else:
#    print("Perhaps another time.")

print('---------------------')
print('  Guess the number!')
print('---------------------')
print()

is_correct = False
answer = random.randint(0, 100)

#debugging
#print(answer)

while is_correct is not True:
    guess_text = input('Guess a number between 0 and 100: ')
    guess_int = int(guess_text)
    if guess_int >= 0 and guess_int <= 100:
        if guess_int > answer:
            print('Too high, try again!')
        elif guess_int < answer:
            print('Too low, try again!')
        elif guess_int == answer:
            print('Congrats! You win!')
            is_correct = True
    else:
        print('Please enter a valid number between 0 and 100!')

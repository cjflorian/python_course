import random
computer_choice =  random.choice(['rock','papper','scissors'])
user_choice = input('Do you want rock, papper or scissors?')
if(computer_choice == user_choice):
    print ('TIE')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('WIN')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN')
elif user_choice == 'scissors' and computer_choice == 'papper':
    print('WIN')
else:
    print('you LOSE')
import random
import time
wins=0
loose=0
draw=0
for i in range(3):
    
    computer_choice=random.choice(['rock', 'paper','scissors'])
    time.sleep(1)
    print('\nlets play rock ,paper and scissors.')
    print('lets start')

    user_choice=input('enter your choice: ').lower()
    print(f'Computer chose: {computer_choice}')

    if user_choice== computer_choice:
        print('draw')
        draw+=1
    elif user_choice=='rock' and computer_choice=='paper':
        print('computer wins \nyou loose\nbetter luck next time')
        loose+=1
    elif user_choice=='rock' and computer_choice=='scissors':
        print('you win')
        wins+=1
    elif user_choice=='paper' and computer_choice=='scissors':
        print('computer wins \nyou loose\nbetter luck next time.')
        loose+=1
    elif user_choice=='scissors' and computer_choice=='paper':
        print('you win')
        wins+=1
    elif user_choice=='paper' and computer_choice=='rock':
        print('you win')
        wins+=1
    elif user_choice=='scissors' and computer_choice=='rock':
        print('computer wins \nyou loose\nbetter luck next time.')
        loose+=1
    else:
        print('invalid input.')
        i-=1
print('......final result......')
print(f'draws={draw}')
print(f'wins={wins}')
print(f'loose={loose}')



from random import randint

player = input('rock (r), paper (p), scissors (s)?')

print(player,'vs')

chosen = randint(1,3)
print(chosen) 

if(chosen == 1):
    computer == 'r'

elif(chosen == 2):
    computer =='p'

else:
    computer =='s'

print(computer)

if(player == computer):
    print('DRAW!')
elif(player == 'r' and computer == 's'):
    print('Player WINS!')
elif(player == 'r' and computer == 'p'):
    print('Computer WINS!')
elif(player == 'p' and computer == 'r'):
    print("Player WINS!")
elif(player == 'p' and computer == 's'):
    print('Computer WINS!')
elif(player == 's' and computer == 'p'):
    print('Player WINS!')
elif(player == 's' and computer == 'r'):
    print('Computer WINS!')

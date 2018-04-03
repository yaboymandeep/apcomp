import random 
import sys

def play():
    global win
    global loss
    global counter
    global cont
    cont=True
    win=0
    loss=0
    counter=0
    play=raw_input('Welcome to Rock, Paper, Scissors, Lizard, Spock. Enter "s" to start: ')
    if play=='s':
        play1()
    
    
def play1(): 
    global win  
    global loss  
    global cont   
    decnum=0
    enemy=0
    '''RPSLS will be represented with numbers where 1=rock, 2=paper, 3=scissors
    4=lizard, 5=spock'''
    while win<2 and loss<2 and cont!=False:   
        decision=raw_input('Rock, Paper, Scissors, Lizard, or Spock? (q to quit): ')
        if decision=='Rock' or decision=='rock':
            decnum=1
        elif decision=='Paper' or decision=='paper':
            decnum=2
        elif decision=='Scissors' or decision=='scissors':
            decnum=3
        elif decision=='Lizard' or decision =='lizard':
            decnum=4
        elif decision=='Spock' or decision=='spock':
            decnum=5
        elif decision=='q':
            decnum=6
        else:
            print('Please enter a valid choice')
            play1()
    
        enemy=random.randint(1,5)
        if decnum==1:
            if enemy==1:
                print ('Rock clashes with rock. Tie')
                play1()
            if enemy==2:
                print('Paper covers your rock. Loss')
                loss+=1
                play1()
            if enemy==3:
                print('Your rock crushes scissors. Win')
                win+=1
                play1()
            if enemy==4:
                print('Your rock flattens lizard. Win')
                win+=1
                play1()
            if enemy==5:
                print ('Spock vaporizes rock. Loss')
                loss+=1
                play1()
                
        if decnum==2:
            if enemy==1:
                print ('Paper covers rock. Win')
                win+=1
                play1()
            if enemy==2:
                print('Paper and paper. Tie')
                play1()
            if enemy==3:
                print('Scissors cuts paper. Loss')
                loss+=1
                play1()
            if enemy==4:
                print('Lizard eats paper. Loss')
                loss+=1
                play1()
            if enemy==5:
                print ('Paper disproves spock. Win')
                win+=1
                play1()
                
        if decnum==3:
            if enemy==1:
                print ('Rock crushes scissors. Loss')
                loss+=1
                play1()
            if enemy==2:
                print('Scissors cuts paper. Win')
                win+=1
                play1()
            if enemy==3:
                print('Scissors and scissors. Tie')
                play1()
            if enemy==4:
                print('Scissors decapitates lizard')
                win+=1
                play1()
            if enemy==5:
                print ('Spock smashes scissors. Loss.')
                loss+=1
                play1()
            
        if decnum==4:
            if enemy==1:
                print ('Rock crushes lizard. Loss')
                loss+=1
                play1()
            if enemy==2:
                print('Lizard eats paper. Win')
                win+=1
                play1()
            if enemy==3:
                print('Scissors decapitates lizard. Loss')
                loss+=1
                play1()
            if enemy==4:
                print('Lizard and lizard brawl. Tie')
                play1()
            if enemy==5:
                print ('Lizard poisons spock. Win')
                win+=1
                play1()
                
        if decnum==5:
            if enemy==1:
                print ('Spock vaporizes rock. Win')
                win+=1
                play1()
            if enemy==2:
                print('Paper disproves Spock. Loss')
                loss+=1
                play1()
            if enemy==3:
                print('Spock smashes scissors. Win')
                win+=1
                play1()
            if enemy==4:
                print('Lizard poisons spock. Loss')
                loss+=1
                play1()
            if enemy==5:
                print ('Spock and Spock. Tie')
                play1()
        if decnum==6:
            print('Thanks for playing')
            cont=False
    
    if win==2:
        print ('Congrats! You win')
        again=raw_input('Press s to play again: ')
        if again == 's':
            win=0
            loss=0
            play1()
        else:
            print ('Play again another time')
            sys.exit()
    if loss==2:
        again=raw_input('You lost. Try again? Press s: ')
        if again=='s':
            win=0
            loss=0
            play1()
        else:
            print('Thanks for playing')
            sys.exit()
    
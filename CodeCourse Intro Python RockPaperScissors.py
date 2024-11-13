#import random library
import random
def RockPaperScissors():
    choice = ''
    result = ''
    compscore = 0
    yourscore = 0
    playagain = 'y'
    while playagain == 'y':
        # user to input choice
        userchoice = input("Enter a choice (Rock(r), Paper(p), Scissors(s))")
        if userchoice == 'r':
            choice = 'rock'
        elif userchoice == 'p':
            choice = 'paper'
        else:
            choice = 'scissors'

        # get computer to chose a random number between 1 and 3
        n = (random.randint(1, 3))
        if n == 1:
            compchoice = 'rock'
        elif n == 2:
            compchoice = 'paper'
        else:
            compchoice = 'scissors'
        #print your choice and computers choice
        print('Your Choice is ' + choice + ', Computers choice is ' + compchoice)

        if choice == compchoice:
            result = 'Its a tie!'
        elif choice == 'rock' and compchoice == 'paper':
            result = 'You lose, Paper wraps rock'
            compscore += 1
        elif choice == 'rock' and compchoice == 'scissors':
            result = 'You Win, Rock smashes scissors'
            yourscore += 1
        elif choice == 'paper' and compchoice == 'scissors':
            result = 'You lose, Scissors cut paper'
            compscore += 1
        elif choice == 'paper' and compchoice == 'rock':
            result = 'You Win, Paper wraps rock'
            yourscore += 1
        elif choice == 'scissors' and compchoice == 'rock':
            result = 'You lose, rock smashes scissors'
            compscore += 1
        elif choice == 'scissors' and compchoice == 'paper':
            result = 'You Win, Scissors cut paper'
            yourscore += 1

        print(result)
        print('Computers Score is: ' + str(compscore))
        print('Your Score is: ' + str(yourscore))

        playagain = input("Do you want to play again? y/n?")

    else:
        print('Final Scores')
        print('Computers Score is: ' + str(compscore))
        print('Your Score is: ' + str(yourscore))




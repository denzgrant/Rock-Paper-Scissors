import random
import math

def play():
    user = input("Choose your fighter carefully! 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r','p','s'])

    if user == computer:
        return (0, user, computer)

    if is_win(user, computer): 
        return (1, user, computer)
    # if its not a tie or a win, it's sadly a lost. 
    return (-1, user, computer)

def  is_win(player, opponent):
    # returns true is the player beats the opponent
    # winning conditions: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    return False

def play_best_of(n):
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary or computer_wins < wins_necessary: 
        result, user, computer = play() 
        if result == 0:
            print('It is a tie. You and the comnputer have both chose {}. \n'.format(user))
        elif result == 1:
            player_wins += 1
            print('You chose {} and the comnputer chose {}. You won!\n'.format(user, computer))   
        else: 
            computer_wins += 1
            print('You chose {} and the computer chose {}. The computer won\n'.format(user, computer))
        print('\n')

    if player_wins > computer_wins:
        print ("Congrats,  you won the best of {} games!".format(n))
    else: 
        print ("Sorry, the computer has won the best of {} games!".format(n))
        
if __name__ == '__main__':
    print(play())
    play_best_of(3)
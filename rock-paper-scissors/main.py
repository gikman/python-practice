import random


def play():
    user = input("'r' for rock, 's' for scissor, 'p' for paper: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print('tie')

    if is_win(computer, user):
        print(f'You lost! {computer} > {user}')

    if is_win(user, computer):
        print(f'You win! {user} > {computer}')


def is_win(player, opponent):
    # return true if player win
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


play()
while input('play again? Y/N: ').upper() == 'Y':
    play()

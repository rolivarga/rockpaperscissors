import random



def player_guess():
    guess = ''

    while (guess not in ['r', 'p', 's']):
        guess = input("R(ock) P(aper) or S(cissors): ")

    return guess


def check_guess(ai_guess, player_guess):
    ai_won = 0

    if (player_guess == 'r'):
        if (ai_guess == 'r'):
            print(f'Draw.')
        elif (ai_guess == 'p'):
            print(f'AI won.')
            ai_won = 1
        elif (ai_guess == 's'):
            print(f'You won.')
            ai_won = 2

    elif (player_guess == 'p'):
        if (ai_guess == 'r'):
            print(f'You won.')
            ai_won = 2
        elif (ai_guess == 'p'):
            print(f'Draw.')
        elif (ai_guess == 's'):
            print(f'AI won.')
            ai_won = 1

    elif (player_guess == 's'):
        if (ai_guess == 'r'):
            print(f'AI won.')
            ai_won = 1
        elif (ai_guess == 'p'):
            print(f'You won.')
            ai_won = 2
        elif (ai_guess == 's'):
            print(f'Draw.')

    return ai_won


default_list = ['r', 'p', 's']
player = ''
ai = ''
i = 0

ai_score = 0
player_score = 0

while (i < 5):
    player = player_guess()
    ai = random.choice(default_list)
    result = check_guess(ai, player)
    if (result==1):
        ai_score += 1
    elif (result==2):
        player_score += 1
    print(f'{player_score}:{ai_score}')

    if(ai_score == 3 or player_score == 3):
        break

    i += 1


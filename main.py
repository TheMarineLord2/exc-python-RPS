from random import randint


def player_interface(options) -> int:
    for each, option in enumerate(options):
        print(each, option)

    print('What number would you like to You choose?')
    result = int(input('__:'))
    return result


def computer_interface(options) -> int:
    return randint(0, len(options) - 1)


def determine_result(player_option, computer_option, options):
    print('Player plays:', options[player_option], 'and computer plays:', options[computer_option])

    if computer_option - player_option != 0:
        if player_option == 0:
            if computer_option == 1:
                print('Player looses')
            elif computer_option == 2:
                print('Player wins')
        elif player_option == 1:
            if computer_option == 2:
                print('Player looses')
            elif computer_option == 0:
                print('Player wins')
        elif player_option == 2:
            if computer_option == 0:
                print('Player looses')
            elif computer_option == 1:
                print('Player wins')
    else:
        print('It is draw')


def play():
    options_table = ['rock', 'paper', 'scissors']
    determine_result(player_interface(options_table), computer_interface(options_table), options_table)


def main():
    continue_game = ''
    while continue_game != 'n':
        play()
        continue_game = input('Continue game?')


main()
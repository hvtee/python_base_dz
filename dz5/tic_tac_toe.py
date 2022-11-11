from random import randint


def is_condition_win(field_):
    return ((field_[0] == 'x' and field_[2] == 'x' and field_[4] == 'x') or
            (field_[6] == 'x' and field_[8] == 'x' and field_[10] == 'x') or
            (field_[12] == 'x' and field_[14] == 'x' and field_[16] == 'x') or
            (field_[0] == 'x' and field_[6] == 'x' and field_[12] == 'x') or
            (field_[2] == 'x' and field_[8] == 'x' and field_[14] == 'x') or
            (field_[4] == 'x' and field_[10] == 'x' and field_[16] == 'x') or
            (field_[0] == 'x' and field_[8] == 'x' and field_[16] == 'x') or
            (field_[4] == 'x' and field_[8] == 'x' and field_[12] == 'x')) or \
           ((field_[0] == 'o' and field_[2] == 'o' and field_[4] == 'o') or
            (field_[6] == 'o' and field_[8] == 'o' and field_[10] == 'o') or
            (field_[12] == 'o' and field_[14] == 'o' and field_[16] == 'o') or
            (field_[0] == 'o' and field_[6] == 'o' and field_[12] == 'o') or
            (field_[2] == 'o' and field_[8] == 'o' and field_[14] == 'o') or
            (field_[4] == 'o' and field_[10] == 'o' and field_[16] == 'o') or
            (field_[0] == 'o' and field_[8] == 'o' and field_[16] == 'o') or
            (field_[4] == 'o' and field_[8] == 'o' and field_[12] == 'o'))


def create_field():
    field_ = '1 2 3\n' \
             '4 5 6\n' \
             '7 8 9'
    return field_


def print_field(field_):
    print()
    print(field_)
    print()


def choose_game_type():
    print("Choose game type: ")
    print("player vs player - 1")
    print("player vs bot - 2")
    while True:
        game_type_ = int(input("Game type: "))
        if game_type_ == 1 or game_type_ == 2:
            break
        print("Wrong!")
        print()
    return game_type_


def input_players_name(players_num: int):
    players_ = [input(f"Input player {i + 1} name: ") for i in range(players_num)]
    return players_


def find_first_player(players_num):
    first_player = randint(0, len(players_num) - 1)
    return first_player


def game_pvp(field_):
    def game_pvp_turn(players_, current_player_index_, field_f, signs_, current_sign_index_):
        print_field(field_f)
        place_for_sign = input(f'Where do you want to place sign, {players_[current_player_index_]}? ')
        field_f = field_f.replace(place_for_sign, signs_[current_sign_index_])
        return field_f

    signs = ['x', 'o']
    current_sign_index = 0
    players = input_players_name(2)
    current_player_index = find_first_player(players)

    while True:
        field_ = game_pvp_turn(players, current_player_index, field_, signs, current_sign_index)
        if is_condition_win(field_):
            print()
            print(f'{players[current_player_index]}, you won!')
            print()
            print(field_)
            break
        if ('1' and '2' and '3' and '4' and '5' and '6' and '7' and '8' and '9') not in field_:
            print()
            print('No one won!')
            print()
            print(field_)
            break
        if current_player_index == len(players) - 1:
            current_player_index = 0
        else:
            current_player_index += 1
        if current_sign_index == len(signs) - 1:
            current_sign_index = 0
        else:
            current_sign_index += 1


def game_pve(field_):
    print("New field created!")
    print_field(field_)


def main():
    field = create_field()

    while True:
        game_type = choose_game_type()

        if game_type == 1:  # PLAYER VS PLAYER
            while True:
                game_pvp(field)

                while True:
                    print()
                    choose = int(input("Back? 1. No 2. Yes | "))
                    if choose == 1 or choose == 2:
                        break
                    print("Wrong!")
                if choose == 2:
                    break
        elif game_type == 2:  # PLAYER VS BOT
            while True:
                game_pve(field)

                while True:
                    print()
                    choose = int(input("Back? 1. No 2. Yes | "))
                    if choose == 1 or choose == 2:
                        break
                    print("Wrong!")
                if choose == 2:
                    break

        while True:
            print()
            choose = int(input("Do you want to play again? 1. Yes 2. No | "))
            if choose == 1 or choose == 2:
                print('Thanks for playing!')
                break
            print("Wrong!")
        if choose == 2:
            print()
            print('Thanks playing!')
            break


main()

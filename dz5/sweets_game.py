from random import randint


def choose_game_type():
    print("Choose game type: ")
    print("player vs player - 1")
    print("player vs bot - 2")
    while True:
        game_type_ = int(input("Game type: "))
        if game_type_ == 1 or game_type_ == 2:
            break
    return game_type_


def input_players_name(players_num: int):
    players_ = [input(f"Input player {i + 1} name: ") for i in range(players_num)]
    return players_


def find_first_player(players_num):
    first_player = randint(0, len(players_num))
    return first_player


def game_turn(players_, current_player_index_, sweets_):
    print(f"Current sweets: {sweets_}")
    while True:
        sweets_to_take = int(input(f"{players_[current_player_index_]}"
                                   f", how many sweets do you want to take(1-28): "))
        if 1 <= sweets_to_take <= 28 and sweets_ - sweets_to_take >= 0:
            sweets_ -= sweets_to_take
            break
        print("Wrong sweets value")
    return sweets_


def main():
    game_type = choose_game_type()
    # players = []

    if game_type == 1:  # PLAYER VS PLAYER
        players = input_players_name(int(input("Input players quantity: ")))
        current_player_index = find_first_player(players)
        sweets = 221
        while sweets > 0:
            sweets = game_turn(players, current_player_index, sweets)

            if sweets == 0:
                print()
                print(f"Current sweets: {sweets}")
                print(f'Player {players[current_player_index]} has won!')
                break

            if current_player_index == len(players) - 1:
                current_player_index = 0
            else:
                current_player_index += 1

        # print(f'Players: {players}, game_type: {game_type}, players_indexes: {players_indexes},'
        #       f' current_player_index: {current_player_index}')

    elif game_type == 2:  # PLAYER VS BOT
        quit()
        players = input("Input player name: ")


main()

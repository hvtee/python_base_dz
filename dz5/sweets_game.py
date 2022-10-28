import time
from random import randint


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


def game_pvp():
    def game_turn(players_, current_player_index_, sweets_):
        print()
        while True:
            print(f"Current sweets: {sweets_}")
            sweets_to_take = int(input(f"{players_[current_player_index_]}"
                                       f", how many sweets do you want to take(1-28): "))
            if 1 <= sweets_to_take <= 28 and sweets_ - sweets_to_take >= 0:
                sweets_ -= sweets_to_take
                break
            print()
            print("Wrong sweets value")
            print()
        return sweets_

    print()
    print("Your game type: pve")

    while True:  # PLAYERS QUANTITY
        players_quantity = int(input("Input players quantity(2-4): "))
        if 1 < players_quantity < 5:
            break
        print("Wrong!")
        print()

    players = input_players_name(players_quantity)
    current_player_index = find_first_player(players)

    while True:  # SWEETS QUANTITY
        sweets = int(input("How many sweets do you want(112-2022)? "))
        if 112 <= sweets <= 2022:
            break
        print("Wrong!")
        print()

    while sweets > 0:  # MAIN GAME
        sweets = game_turn(players, current_player_index, sweets)

        if sweets == 0:
            print()
            print()
            print()

            print(f"Current sweets: {sweets}")
            print(f'Player {players[current_player_index]} has won!')
            break

        if current_player_index == len(players) - 1:
            current_player_index = 0
        else:
            current_player_index += 1


def game_pve():
    def game_turn(players_, current_player_index_, sweets_):
        print()
        time.sleep(1)
        if current_player_index_ == len(players_) - 1:
            while True:
                print(f"Current sweets: {sweets_}")
                sweets_to_take = int(input(f"{players_[current_player_index_]}"
                                           f", how many sweets do you want to take(1-28): "))
                if 1 <= sweets_to_take <= 28 and sweets_ - sweets_to_take >= 0:
                    sweets_ -= sweets_to_take
                    break
                print()
                print("Wrong sweets value")
                print()
        else:
            print(f"Current sweets: {sweets_}")
            if sweets_ > 28:
                sweets_to_take = randint(1, 28)
                sweets_ -= sweets_to_take

                print(f"{players_[current_player_index_]}"
                      f", how many sweets do you want to take(1-28): {sweets_to_take}")
            else:
                sweets_to_take = sweets_

                print(f"{players_[current_player_index_]}"
                      f", how many sweets do you want to take(1-28): {sweets_to_take}")

                sweets_ -= sweets_to_take
        return sweets_

    bot_names = ['Bob', 'Karl', 'Dan', 'Mike', 'Lad', 'John', 'Jason', 'Peter', 'Patrik']
    while True:  # BOTS QUANTITY
        bots_quantity = int(input("Input bots quantity(1-3): "))
        if 0 < bots_quantity < 4:
            break
        print("Wrong!")
        print()

    players = []  # BOT NAMES
    while len(players) != 3:
        bot_name_index = randint(0, len(bot_names) - 1)
        if bot_names[bot_name_index] not in players:
            players.append(bot_names[bot_name_index])
    print(f'Bot names: {players}')
    players.append(input("Input your name: "))

    current_player_index = find_first_player(players)
    while True:  # SWEETS QUANTITY
        sweets = int(input("How many sweets do you want(112-2022)? "))
        if 112 <= sweets <= 2022:
            break
        print("Wrong!")
        print()

    while sweets > 0:  # MAIN GAME
        sweets = game_turn(players, current_player_index, sweets)

        if sweets == 0:
            print()
            print()
            print()

            print(f"Current sweets: {sweets}")
            print(f'Player {players[current_player_index]} has won!')
            break

        if current_player_index == len(players) - 1:
            current_player_index = 0
        else:
            current_player_index += 1


def main():
    print()
    print("Hello, lets play sweet game!")
    print()

    while True:
        game_type = choose_game_type()

        if game_type == 1:  # PLAYER VS PLAYER
            while True:
                game_pvp()

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
                game_pve()

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
            print()
            print()

            print('Thanks playing!')
            break


main()

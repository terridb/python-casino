from games import fruitmachine, roulette, blackjack
from games.helpers import print_title
from profiles import create_account, show_all_players, show_account, switch_account, remove_account, initialize_player, \
    get_current_balance, register_played_game, update_current_balance

CASINO_NAME = "Casino de Gouden Driehoek"
TICKET_PRICE = 9.99
DRINK_PRICE = 4.99
TAX = 1.00
STANDARD_COSTS = TICKET_PRICE + DRINK_PRICE + TAX


def calculate_starting_budget(start_budget: float):
    """
    This function calculates the starting budget.
    :param start_budget: starting budget in euros (float)
    :return: new starting budget in euros (float)
    """
    return start_budget - STANDARD_COSTS


def show_account_menu():
    choice = int(
        input(f"Kies een optie:\n1 Toon alle accounts\n2 Nieuw Account\n3 Wissel account\n4 Verwijder account\n"))
    match choice:
        case 1:
            show_all_players()
        case 2:
            create_account(STANDARD_COSTS)
        case 3:
            switch_account()
        case 4:
            remove_account(STANDARD_COSTS, CASINO_NAME)


def main():
    initialize_player(STANDARD_COSTS, CASINO_NAME)

    while True:
        print("Kies één van de volgende opties: 1 Spellen, 2 Saldo, 3 Account, 0 Stop.")
        choice = int(input("Kies een optie: "))

        match choice:
            case 1:
                print()
                print_title(CASINO_NAME, "spellen")
                print("Kies één van de volgende spellen: 1 Fruitmachine, 2 Roulette, 3 Blackjack, 0 Terug.")
                game_choice = int(input("Kies een spel: "))
                if game_choice == 1:
                    register_played_game("fruitmachine")
                    balance = fruitmachine.play_fruitmachine(get_current_balance(), CASINO_NAME)
                elif game_choice == 2:
                    register_played_game("roulette")
                    balance = roulette.play_roulette(get_current_balance(), CASINO_NAME)
                elif game_choice == 3:
                    register_played_game("blackjack")
                    balance = blackjack.play_blackjack(get_current_balance(), CASINO_NAME)
                else:
                    continue

                update_current_balance(balance)
            case 2:
                print()
                print_title(CASINO_NAME, "saldo")
                print(f"Saldo: €{get_current_balance():.2f}")
                print()
            case 3:
                print()
                print_title(CASINO_NAME, "account")
                print()
                show_account()
                print()
                show_account_menu()
                print()
            case 0:
                print()
                print(f"Eindsaldo: €{get_current_balance():.2f}")
                break


if __name__ == '__main__':
    main()

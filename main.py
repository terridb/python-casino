from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from games import fruitmachine, roulette, blackjack
from profiles import create_account, show_all_players, show_account, switch_account, remove_account, initialize_player, \
    get_current_balance, register_played_game, update_current_balance

CASINO_NAME = "Casino de Gouden Driehoek"
TICKET_PRICE = 9.99
DRINK_PRICE = 4.99
TAX = 1.00
STANDARD_COSTS = TICKET_PRICE + DRINK_PRICE + TAX

console = Console()


def calculate_starting_budget(start_budget: float):
    """
    This function calculates the starting budget.
    :param start_budget: starting budget in euros (float)
    :return: new starting budget in euros (float)
    """
    return start_budget - STANDARD_COSTS


def show_account_menu():
    table = Table(expand=True)
    table.add_column("Optie")
    table.add_column("Spel")
    table.add_row("1", "Toon alle accounts")
    table.add_row("2", "Nieuw account")
    table.add_row("3", "Wissel account")
    table.add_row("4", "Verwijder account")
    console.print(Panel.fit(table, title=f"{CASINO_NAME} - account-menu"))

    choice = int(input(f"Kies een optie: "))
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
    console.print(f"is_terminal: {console.is_terminal}")
    initialize_player(STANDARD_COSTS, CASINO_NAME)

    while True:
        table = Table(expand=True)
        table.add_column("Optie")
        table.add_column("Actie")
        table.add_row("1", "Spellen")
        table.add_row("2", "Saldo")
        table.add_row("3", "Account")
        table.add_row("0", "Stop")
        console.print(Panel.fit(table, title=f"{CASINO_NAME} - hoofdmenu"))
        choice = int(input("Kies een optie: "))

        match choice:
            case 1:
                game_table = Table(expand=True)
                game_table.add_column("Optie")
                game_table.add_column("Spel")
                game_table.add_row("1", "Fruitmachine")
                game_table.add_row("2", "Roulette")
                game_table.add_row("3", "Blackjack")
                game_table.add_row("0", "Terug")
                console.print(Panel.fit(game_table, title=f"{CASINO_NAME} - spellen"))
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
                console.print(Panel(f"[bold]Saldo:[/] €{get_current_balance():.2f}", title=f"{CASINO_NAME} - saldo"))
            case 3:
                show_account()
                show_account_menu()
            case 0:
                console.print(f"[bold]Eindsaldo:[/] €{get_current_balance():.2f}")
                break


if __name__ == '__main__':
    main()

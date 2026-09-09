from random import randint

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from games.helpers import ask_for_bet

console = Console()


def show_roulette_options():
    """
    Prints roulette options.
    :return: input from user (int)
    """
    while True:
        table = Table(expand=True)
        table.add_column("Optie")
        table.add_column("Actie")
        table.add_row("1", "Rood")
        table.add_row("2", "Zwart")
        table.add_row("3", "Even")
        table.add_row("4", "Oneven")
        table.add_row("0", "Stop")
        console.print(Panel.fit(table, title="Roulette"))
        choice = int(input("Kies je gok: "))
        if choice not in (0, 1, 2, 3, 4):
            console.print("[red3]Ongeldige input. Probeer opnieuw.")
        else:
            return choice


def determine_win(color, choice, odd_even):
    """
    Determines if the user has won the game or not.
    :param color: color of the spin (string)
    :param choice: choice of the user (int)
    :param odd_even: if the spun number is odd or even (string)
    :return: win (boolean)
    """
    win = False
    if color == "groen":
        win = True
    elif choice == 1 and color == "rood":
        win = True
    elif choice == 2 and color == "zwart":
        win = True
    elif choice == 3 and odd_even == "even":
        win = True
    elif choice == 4 and odd_even == "oneven":
        win = True
    return win


def play_roulette(balance: float, casino):
    """
    Starts the roulette game.
    :param casino: Casino name
    :param balance: current balance of the user (float)
    :return: balance (float)
    """
    while True:
        console.print(Panel(f"Huidig saldo: €{balance:.2f}", title=f"{casino} - roulette"))
        choice = show_roulette_options()

        if choice == 0:
            break
        elif choice > 4:
            console.print("[red3]Dat is geen geldige keuze. Probeer opnieuw.")
            continue

        stake = ask_for_bet(balance)
        balance -= stake

        spin = randint(0, 36)
        odd_even = ""

        if spin == 0:
            color = "groen"
        else:
            if spin <= 18:
                if spin % 2 == 0:
                    color = "zwart"
                    odd_even = "even"
                else:
                    color = "rood"
                    odd_even = "oneven"
            else:
                if spin % 2 == 0:
                    color = "rood"
                    odd_even = "even"
                else:
                    color = "zwart"
                    odd_even = "oneven"

        win = determine_win(color, choice, odd_even)

        if win == True and color == "groen":
            balance += (stake * 6)
            outcome = f"[sea_green3]Je wint €{(stake * 5):.2f}!"
        elif win == True and not color == "groen":
            balance += (stake * 2)
            outcome = f"[sea_green3]Je wint €{(stake * 2):.2f}!"
        else:
            outcome = f"[red3]Je verliest €{stake:.2f}."

        console.print(Panel(f"Geland op {spin}\n{outcome}", title="Output"))

    console.print(f"Je nieuwe saldo is €{balance:.2f}.")
    return balance

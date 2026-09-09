from rich.console import Console
from rich.panel import Panel
from rich import print

from games.helpers import ask_for_bet

from random import choice

console = Console()

ICONS = [":cherries:", ":lemon:", ":star:", ":banana:", ":dragon:"]

def determine_rolls():
    """
    Determines the rolls of the round.
    :return: tuple with strings
    """

    roll1 = choice(ICONS)
    roll2 = choice(ICONS)
    roll3 = choice(ICONS)

    return roll1, roll2, roll3


def determine_payout(roll1, roll2, roll3, stake: float):
    """
    Determines the payout of the round.
    :param roll1: first roll
    :param roll2: second roll
    :param roll3: third roll
    :param stake: stake that the user picked (float)
    :return: stake or 0
    """
    if roll1 == roll2 == roll3:
        return stake * 3
    elif roll1 == roll2 or roll1 == roll3 or roll2 == roll3:
        return stake
    else:
        return 0


def play_fruitmachine(balance: float, casino):
    """
       Starts the fruitmachine game.
       :param casino: Casino name
       :param balance: current balance of the user (float)
       :return: balance (float)
       """
    while True:
        console.print(Panel(f"Huidig saldo: €{balance:.2f}", title=f"{casino} - fruitmachine"))
        choice = input("Druk op enter om te spelen of typ stop om terug te gaan: ")

        if choice == "stop":
            print("Spel gestopt.")
            return balance

        stake = ask_for_bet(balance)
        balance -= stake

        roll1, roll2, roll3 = determine_rolls()
        console.print(Panel(f"Rollen: {roll1} | {roll2} | {roll3}", title="Output"))
        payout = determine_payout(roll1, roll2, roll3, stake)

        if payout > 0:
            balance += payout
            console.print(f"[sea_green3]Je hebt €{payout:.2f} gewonnen!")
        else:
            console.print(f"[red3]Je hebt verloren. Je verliest €{stake:.2f}")

        console.print(f"Je nieuwe saldo is €{balance:.2f}.")
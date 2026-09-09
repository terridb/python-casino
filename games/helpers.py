from rich.console import Console

console = Console()

def ask_for_bet(balance):
    """
    Asks the user for their bet/stake and checks if valid.
    :param balance: current balance of the user (float)
    :return: stake
    """
    while True:
        stake = float(input("Hoeveel wil je inzetten? "))
        if stake <= 0:
            console.print("[red3]Je hebt geen geld ingezet. Probeer opnieuw.")
        elif stake > balance:
            console.print("[red3]Onvoldoende budget. Probeer opnieuw.")
        else:
            return stake
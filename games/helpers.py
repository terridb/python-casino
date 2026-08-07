def ask_for_bet(balance):
    """
    Asks the user for their bet/stake and checks if valid.
    :param balance: current balance of the user (float)
    :return: stake
    """
    while True:
        stake = float(input("Hoeveel wil je inzetten? "))
        if stake <= 0:
            print("Je hebt geen geld ingezet. Probeer opnieuw.")
        elif stake > balance:
            print("Onvoldoende budget. Probeer opnieuw.")
        else:
            return stake


def print_game_intro(casino, balance: float, game):
    """
    Prints game introduction.
    :param casino: Casino name
    :param balance: current balance of the user (float)
    :param game: name of current game
    """
    title = f"{casino} - {game}"
    print(title)
    print("-" * len(title))
    print(f"Huidig saldo: €{balance:.2f}")


def print_title(casino, subtitle):
    """
    Prints standard introduction/title.
    :param casino: Casino name
    :param subtitle: optional subtitle
    """
    if subtitle:
        title = f"{casino} - {subtitle}"
    else:
        title = casino

    print(title)
    print("-" * len(title))

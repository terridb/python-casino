from games.helpers import ask_for_bet, print_game_intro


def determine_rolls(round_number):
    """
    Determines the rolls of the round.
    :param round_number: number of the round
    :return: tuple with strings
    """
    match round_number % 9:
        case 0:
            return "kers", "citroen", "ster"
        case 1:
            return "kers", "kers", "kers"
        case 2:
            return "ster", "ster", "citroen"
        case 3:
            return "citroen", "kers", "ster"
        case 4:
            return "ster", "ster", "ster"
        case 5:
            return "citroen", "citroen", "citroen"
        case 6:
            return "kers", "ster", "kers"
        case 7:
            return "citroen", "ster", "citroen"
        case 8:
            return "ster", "kers", "citroen"


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
    round_number = 1
    while True:
        print()
        print_game_intro(casino, balance, "fruitmachine")
        choice = input("Druk op enter om te spelen of typ stop om terug te gaan: ")

        if choice == "stop":
            print("Spel gestopt.")
            return balance

        stake = ask_for_bet(balance)
        balance -= stake

        roll1, roll2, roll3 = determine_rolls(round_number)
        print(f"Je hebt {roll1}, {roll2} en {roll3} gedraaid.")
        payout = determine_payout(roll1, roll2, roll3, stake)

        if payout > 0:
            balance += payout
            print(f"Je hebt €{payout:.2f} gewonnen!")
        else:
            print(f"Je hebt verloren. Je verliest €{stake:.2f}")

        print(f"Je nieuwe saldo is €{balance:.2f}.")
        round_number += 1

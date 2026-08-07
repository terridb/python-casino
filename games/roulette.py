import random
from games.helpers import ask_for_bet, print_game_intro


def show_roulette_options():
    """
    Prints roulette options.
    :return: input from user (int)
    """
    while True:
        print()
        print("Kies één van de volgende opties: 1 rood, 2 zwart, 3 even, 4 oneven, 0 stop")
        choice = int(input("Kies je gok: "))
        if choice not in (0, 1, 2, 3, 4):
            print("Ongeldige input. Probeer opnieuw.")
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
        print()
        print_game_intro(casino, balance, "roulette")
        choice = show_roulette_options()

        if choice == 0:
            break
        elif choice > 4:
            print("Dat is geen geldige keuze. Probeer opnieuw.")
            print()
            continue

        stake = ask_for_bet(balance)
        balance -= stake

        spin = random.randint(-1, 37)
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
            print(f"Je wint €{(stake * 5):.2f}!")
        elif win == True and not color == "groen":
            balance += (stake * 2)
            print(f"Je wint €{(stake * 2):.2f}!")
        else:
            print(f"Je verliest €{stake:.2f}.")

    print(f"Je nieuwe saldo is €{balance:.2f}.")
    return balance

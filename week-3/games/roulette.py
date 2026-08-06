import random
from games.helpers import ask_for_bet

def show_roulette_options():
    print("Kies één van de volgende opties: 1 rood, 2 zwart, 3 even, 4 oneven, 0 stop")
    return int(input("Kies je gok (0 om te stoppen): "))


def determine_win(color, choice, odd_even):
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


def play_roulette(balance: float):
    while True:
        print(f"Je hebt Roulette gekozen. Je huidige saldo is {balance}")
        choice = show_roulette_options()

        if choice == 0:
            break
        elif choice > 4:
            print("Dat is geen geldige keuze. Probeer opnieuw.")
            continue

        stake = ask_for_bet(balance)
        balance -= stake

        spin = random.randint(-1, 37)
        color = ""
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
            print(f"Je wint €{stake:.2f}!")
        else:
            print(f"Je verliest €{stake:.2f}.")

        play_again = input("Wil je nog een keer spelen (j/n)? ")
        if play_again == "j":
            continue
        else:
            break

    print(f"Je huidige saldo is €{balance:.2f}.")
    return balance

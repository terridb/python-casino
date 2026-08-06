from games.helpers import ask_for_bet


def determine_rolls(round_number):
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
    if roll1 == roll2 == roll3:
        return stake * 3
    elif roll1 == roll2 or roll1 == roll3 or roll2 == roll3:
        return stake
    else:
        return 0


def play_fruitmachine(balance: float):
    round_number = 1
    while True:
        print(f"Je hebt de Fruitmachine gekozen. Je huidige saldo is €{balance:.2f}")
        print("Kies één van de volgende opties: 1 Start spel, 0 Stop")
        choice = int(input("Keuze: "))

        if choice == 0:
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
            print("Je hebt helaas verloren.")

        print(f"Je huidige saldo is €{balance:.2f}")
        round_number += 1

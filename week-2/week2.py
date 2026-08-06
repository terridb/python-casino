import datetime
import random

CASINO_NAME = "Casino de Gouden Driehoek"
TICKET_PRICE = 9.99
DRINK_PRICE = 4.99
TAX = 1.00
MIN_AGE = 18

STANDARD_COSTS = TICKET_PRICE + DRINK_PRICE + TAX

first_name = input("Voer je voornaam in: ").strip()
last_name = input("Voer je achternaam in: ").strip()
dob = input("Voer je geboortedatum in (dd-mm-yyyy): ").strip()

birth_day, birth_month, birth_year = dob.split("-")
current_date = datetime.datetime.now()
age = current_date.year - int(birth_year)

if age < MIN_AGE:
    print(
        f"Deze applicatie mag alleen gebruikt worden boven de {MIN_AGE} jaar. We zien je graag over {MIN_AGE - age} jaar weer terug!")
    exit(1)

gender = input("Voer je geslacht in (m/v): ").strip()
start_budget = float(input("Voer je startbudget in (in euro's): "))

form_of_address = "mevrouw" if gender == "v" else "meneer" if gender == "m" else first_name
saldo = start_budget - STANDARD_COSTS
enough_saldo = True if saldo >= 0 else False
conclusion = "Je hebt nog genoeg budget voor toegang tot het casino." if enough_saldo == True else "Je hebt niet voldoende budget voor toegang tot het casino."

print(CASINO_NAME)
print("-" * len(CASINO_NAME))
print(f"Welkom, {form_of_address} {last_name}")
print()
print("{0:20} {1}".format("Startbudget:", f"€{start_budget:.2f}"))
print("{0:20} {1}".format("Vaste kosten:", f"€{STANDARD_COSTS:.2f}"))
print("{0:20} {1}".format("Saldo:", f"€{saldo:.2f}"))
print()
print(conclusion)

while True:
    print("Kies één van de volgende opties: 1 rood, 2 zwart, 3 even, 4 oneven, 0 stop")
    choice = int(input("Kies je gok (0 om te stoppen): "))

    if choice == 0:
        break
    elif choice > 4:
        print("Dat is geen geldige keuze. Probeer opnieuw.")
        continue

    stake = float(input("Hoeveel geld (in euro's) wil je inzetten? "))

    if stake <= 0:
        print("Gokken zonder geld in te zetten is wel heel saai. Begin maar even opnieuw.")
        continue

    if stake > saldo:
        print("Zoveel geld heb je qua saldo helemaal niet. Begin maar even opnieuw.")
        continue

    saldo -= stake

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

    win = False
    if choice == 1 and color == "rood":
        win = True
    elif choice == 2 and color == "zwart":
        win = True
    elif choice == 3 and odd_even == "even":
        win = True
    elif choice == 4 and odd_even == "oneven":
        win = True
    elif color == "groen":
        win = True

    if win == True:
        saldo += (stake * 2)
        print(f"Je wint €{stake:.2f}!")
    elif win == True and color == "groen":
        saldo += (stake * 6)
        print(f"Je wint €{(stake * 5):.2f}!")
    else:
        print(f"Je verliest €{stake:.2f}.")

    play_again = input("Wil je nog een keer spelen (j/n)? ")
    if play_again == "j":
        continue
    else:
        break

print(f"Je huidige saldo is €{saldo:.2f}. Tot ziens!")

import datetime

from games import fruitmachine, roulette

CASINO_NAME = "Casino de Gouden Driehoek"
TICKET_PRICE = 9.99
DRINK_PRICE = 4.99
TAX = 1.00
MIN_AGE = 18
CURRENT_DATE = datetime.datetime.now()
STANDARD_COSTS = TICKET_PRICE + DRINK_PRICE + TAX


def calculate_age(birthdate):
    birth_day, birth_month, birth_year = birthdate.split("-")
    return CURRENT_DATE.year - int(birth_year)


def check_age(birthdate):
    age = calculate_age(birthdate)

    if age < MIN_AGE:
        print(
            f"Deze applicatie mag alleen gebruikt worden boven de {MIN_AGE} jaar. We zien je graag over {MIN_AGE - age} jaar weer terug!")
        exit(1)
    else:
        return birthdate


def determine_salutation(first_name, last_name, gender):
    if gender == "v":
        return f"mevrouw {last_name}"
    elif gender == "m":
        return f"meneer {last_name}"
    elif gender == "x":
        return first_name
    else:
        print("Ongeldig geslacht opgegeven. Kies man (m), vrouw (v) of overig (x).")
        return None


def calculate_starting_budget(start_budget: float):
    return start_budget - STANDARD_COSTS


def show_welcome_message(start_budget: float, salutation, balance):
    print()
    print(CASINO_NAME)
    print("-" * len(CASINO_NAME))
    print(f"Welkom, {salutation}")
    print()
    print("{0:20} {1}".format("Startbudget:", f"€{start_budget:.2f}"))
    print("{0:20} {1}".format("Vaste kosten:", f"€{STANDARD_COSTS:.2f}"))
    print("{0:20} {1}".format("Saldo:", f"€{calculate_starting_budget(start_budget):.2f}"))
    print()
    enough_saldo = True if balance >= 0 else False
    conclusion = "Je hebt nog genoeg budget voor toegang tot het casino." if enough_saldo == True else "Je hebt niet voldoende budget voor toegang tot het casino."
    print(conclusion)


def show_current_balance(balance):
    print(f"Huidig saldo: €{balance:.2f}")


def main():
    first_name = input("Voer je voornaam in: ").strip()
    last_name = input("Voer je achternaam in: ").strip()
    dob = check_age(input("Voer je geboortedatum in (dd-mm-yyyy): ").strip())

    salutation = None
    while salutation is None:
        gender = input("Voer je geslacht in (m/v/x): ").strip()
        salutation = determine_salutation(first_name, last_name, gender)

    start_budget = float(input("Voer je startbudget in (in euro's): "))
    balance = calculate_starting_budget(start_budget)
    show_welcome_message(start_budget, salutation, balance)

    while True:
        print("Kies één van de volgende opties: 1 Spellen, 2 Saldo, 3 Account, 0 Stop.")
        choice = int(input("Kies een optie: "))

        match choice:
            case 1:
                print("Kies één van de volgende spellen: 1 Fruitmachine, 2 Roulette, 0 Terug.")
                game_choice = int(input("Kies een spel: "))
                if game_choice == 1:
                    balance = fruitmachine.play_fruitmachine(balance)
                elif game_choice == 2:
                    balance = roulette.play_roulette(balance)
                else:
                    continue
            case 2:
                print("Je hebt gekozen voor 'Saldo'.")
                show_current_balance(balance)
            case 3:
                print("Je hebt gekozen voor 'Account'.")
                print(f"Naam: {first_name} {last_name}")
                print(f"Aanspreekvorm: {salutation}")
                print(f"Geboortedatum: {dob}")
                print(f"Leeftijd: {calculate_age(dob)}")
            case 0:
                print(f"Eindsaldo: €{balance:.f2}")
                break

if __name__ == '__main__':
    main()
import datetime

MIN_AGE = 18
CURRENT_DATE = datetime.datetime.now()

players = {}
current_player = None


def get_current_player():
    """
    Gets current player
    :return:
    """
    global current_player
    return players[current_player]


def get_current_balance():
    account = get_current_player()
    return account["saldo"]


def update_current_balance(balance):
    account = get_current_player()
    account["saldo"] = balance


def register_played_game(game_name):
    account = get_current_player()
    played_games = account["gespeelde_spellen"]
    if game_name in played_games:
        played_games[game_name] += 1
    else:
        played_games[game_name] = 1


def determine_salutation(name, gender):
    if gender == "v":
        return f"mevrouw {name}"
    elif gender == "m":
        return f"meneer {name}"
    elif gender == "x":
        return name
    else:
        print("Ongeldig geslacht opgegeven. Kies man (m), vrouw (v) of overig (x).")
        return None


def calculate_age(birthdate):
    """
    This function calculates the age using a birthdate.
    :param birthdate: birthdate (dd-mm-yyyy) of a user
    :return: age
    """
    birth_day, birth_month, birth_year = birthdate.split("-")
    return CURRENT_DATE.year - int(birth_year)


def check_age(birthdate):
    """
    This function checks if the age of the user is above the MIN_AGE or not.
    :param birthdate: birthdate (dd-mm-yyyy) of a user
    :return: birthdate or exit
    """
    age = calculate_age(birthdate)

    if age < MIN_AGE:
        print(
            f"Deze applicatie mag alleen gebruikt worden boven de {MIN_AGE} jaar. We zien je graag over {MIN_AGE - age} jaar weer terug!")
        exit(1)
    else:
        return birthdate


def show_account():
    global current_player

    current_account = players[current_player]

    print(f"Naam: {current_player}")
    print(f"Saldo: €{current_account["saldo"]:.2f}")
    print(f"Gespeelde spellen: {current_account["gespeelde_spellen"]}")
    print(f"Beschikbare spelers: {list(players.keys())}")


def show_all_players():
    for player in players:
        print(f"1 {player["naam"]}: €{player["saldo"]:.2f}")


def create_account(total_cost, name=None):
    global current_player

    if name is None:
        name = input("Naam voor het nieuwe account: ").capitalize()
        if name in players:
            print("Dit account bestaat al. Gebruik 'Wissel account' om het te openen.")
            return

    password = input("Voer een wachtwoord in: ").strip()
    dob = check_age(input("Voer je geboortedatum in (dd-mm-yyyy): ").strip())
    gender = input("Voer je geslacht in (m/v/x): ").strip().lower()
    while gender not in ("m", "v", "x"):
        gender = input("Ongeldig geslacht. Voer je geslacht in (m/v/x): ").strip().lower()
    start_budget = float(input("Voer je startbudget in (in euro's): "))
    balance = start_budget - total_cost
    players[name] = create_profile(name, dob, gender, balance, password)
    current_player = name
    return


def create_profile(name, birthdate, gender, balance, password):
    return {
        "naam": name,
        "wachtwoord": password,
        "geboortedatum": birthdate,
        "gender": gender,
        "saldo": balance,
        "gespeelde_spellen": {},
    }


def switch_account():
    global current_player

    account = input("Naar welke account-naam wil je wisselen? ").strip().capitalize()
    if account in players:
        check_user_password(account)
        current_player = account
    else:
        print("Dit account bestaat niet, probeer opnieuw.")
        return


def remove_account(total_cost, casino):
    global current_player
    if len(players) < 2:
        print("Dit account mag niet verwijderd worden.")
        return
    else:
        del players[current_player]
        print("Je account is succesvol verwijderd!")
        print()
        initialize_player(total_cost, casino)


def check_password_validity(name, password):
    account = players[name]
    account_password = account["wachtwoord"]

    if account_password == password:
        return True
    else:
        return False


def check_user_password(name):
    password = input("Wat is je wachtwoord? ").strip()

    while check_password_validity(name, password) == False:
        print("Verkeerd wachtwoord. Probeer opnieuw.")
        continue

    print("Succesvol ingelogd!")


def initialize_player(total_cost, casino_name):
    global players
    global current_player

    players = {
        "Anna": {
            "naam": "Anna",
            "wachtwoord": "demo",
            "geboortedatum": "24-03-2000",
            "gender": "v",
            "saldo": 50,
            "gespeelde_spellen": {},
        }
    }

    name = input("Wat is je naam? ").strip().capitalize()
    current_player = name

    if name in players:
        check_user_password(name)
        profile = players[current_player]
        salutation = determine_salutation(current_player, profile["gender"])
        balance = get_current_balance()

        print()
        print(casino_name)
        print("-" * len(casino_name))
        print(f"Welkom, {salutation}")
        print(f"Saldo: €{balance:.2f}")
        print()
    else:
        create_account(total_cost, name)

        profile = players[current_player]
        balance = profile["saldo"]
        start_balance = balance + total_cost
        salutation = determine_salutation(current_player, profile["gender"])
        has_budget = total_cost <= start_balance
        conclusion = "Je hebt nog genoeg budget voor toegang tot het casino." if has_budget == True else "Je hebt niet voldoende budget voor toegang tot het casino."

        print(f"Welkom, {salutation}")
        print()
        print("{0:20} {1}".format("Startbudget:", f"€{start_balance:.2f}"))
        print("{0:20} {1}".format("Vaste kosten:", f"€{total_cost:.2f}"))
        print("{0:20} {1}".format("Saldo:", f"€{balance:.2f}"))
        print()
        print(conclusion)
        print()

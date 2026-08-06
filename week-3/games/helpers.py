def ask_for_bet(balance):
    while True:
        stake = float(input("Hoeveel geld (in euro's) wil je inzetten? "))
        if stake <= 0:
            print("Gokken zonder geld in te zetten is wel heel saai. Begin maar even opnieuw.")
        elif stake > balance:
            print("Zoveel geld heb je qua saldo helemaal niet. Begin maar even opnieuw.")
        else:
            return stake
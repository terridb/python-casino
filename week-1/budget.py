CASINO_NAME = "Casino de Gouden Driehoek"
TICKET_PRICE = 9.99
DRINK_PRICE = 4.99
TAX = 1.00

standard_costs = TICKET_PRICE + DRINK_PRICE + TAX

first_name = input("Voer je voornaam in: ").strip()
last_name = input("Voer je achternaam in: ").strip()
dob = input("Voer je geboortedatum in (dd-mm-yyyy): ").strip()
gender = input("Voer je geslacht in (m/v): ").strip()
start_budget = float(input("Voer je startbudget in (in euro's): "))

form_of_address = "mevrouw" if gender == "v" else "meneer" if gender == "m" else first_name
saldo = start_budget - standard_costs
enough_saldo = True if saldo >= 0 else False
conclusion = "Je hebt nog genoeg budget voor toegang tot het casino." if enough_saldo == True else "Je hebt niet voldoende budget voor toegang tot het casino."

print(CASINO_NAME)
print("-" * len(CASINO_NAME))
print(f"Welkom, {form_of_address} {last_name}")
print()
print("{0:20} {1}".format("Startbudget:", f"€{start_budget:.2f}"))
print("{0:20} {1}".format("Vaste kosten:", f"€{standard_costs:.2f}"))
print("{0:20} {1}".format("Saldo:", f"€{saldo:.2f}"))
print()
print(conclusion)
import random

from games.helpers import print_game_intro, ask_for_bet

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def create_deck():
    deck = [f"{s}{r}" for s in SUITS for r in RANKS]
    random.shuffle(deck)
    return deck


def draw_card(deck, hand):
    hand.append(deck[0])
    pulled_card = deck.pop(0)
    return pulled_card


def show_hand(hand, label, hide_card=False):
    if label == "player":
        print(f"Jouw hand: {" | ".join(hand)}")
    else:
        if hide_card:
            print(f"Dealer hand: {hand[0]} | ??")
        else:
            print(f"Dealer hand: {" | ".join(hand)}")


def calculate_card_value(card):
    rank = card[1]
    if rank in ("J", "K", "Q"):
        return 10
    elif rank == "A":
        return 11
    else:
        return int(rank)


def calculate_hand_value(hand):
    total = 0
    for card in hand:
        total += calculate_card_value(card)

    aces = [card for card in hand if card[1] == "A"]
    number_of_aces = len(aces)

    while total > 21 and number_of_aces > 0:
        total -= 10
        number_of_aces -= 1

    return total


def determine_win(hand_dealer, hand_player, balance, stake):
    total_player = calculate_hand_value(hand_player)
    total_dealer = calculate_hand_value(hand_dealer)

    win: float = 0
    if total_dealer > 21:
        win = stake * 2
        balance += win
        print(f"Je wint van de dealer: €{win:.2f}!")
    elif total_player > total_dealer:
        win = stake * 1.5
        balance += win
        print(f"Je wint van de dealer: €{win:.2f}!")
    elif total_dealer == total_player:
        balance += stake
        print("Gelijkspel! Je krijgt je inzet terug.")
    else:
        print("Verloren van de dealer.")

    return balance


def play_blackjack(balance: float, casino):
    while True:
        print()
        print_game_intro(casino, balance, "blackjack")
        stake = ask_for_bet(balance)
        balance -= stake

        deck = create_deck()
        hand_dealer = []
        hand_player = []
        draw_card(deck, hand_dealer)
        draw_card(deck, hand_player)
        draw_card(deck, hand_dealer)
        draw_card(deck, hand_player)
        show_hand(hand_player, "player")
        show_hand(hand_dealer, "dealer", True)
        print(f"Jouw totaal: {calculate_hand_value(hand_player)}")

        while calculate_hand_value(hand_player) < 21:
            hit_or_stand = input("Kies hit of stand: ").strip().lower()
            if hit_or_stand == "stand":
                break
            elif hit_or_stand == "hit":
                card = draw_card(deck, hand_player)
                print(f"Je trekt: {card}")
                show_hand(hand_player, "player")
                print(f"Jouw totaal: {calculate_hand_value(hand_player)}")

                if calculate_hand_value(hand_player) > 21:
                    print("Bust!")
                    return balance
            else:
                print("Incorrecte input. Probeer opnieuw.")
                continue

        show_hand(hand_dealer, "dealer")
        while calculate_hand_value(hand_dealer) < 17:
            card = draw_card(deck, hand_dealer)
            print(f"Dealer trekt: {card}")
            show_hand(hand_dealer, "dealer")

        print(f"Jouw totaal: {calculate_hand_value(hand_player)}")
        print(f"Dealer totaal: {calculate_hand_value(hand_dealer)}")
        balance = determine_win(hand_dealer, hand_player, balance, stake)
        print(f"Nieuw saldo: €{balance:.2f}")
        return balance

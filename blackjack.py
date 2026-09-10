import random

deck = []

def start():
    suits = ["♥", "♦", "♠", "♣"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    for suit in suits:
        for rank in ranks:
            if rank.isdigit():
                value = int(rank)
            elif rank.strip().lower() == "a":
                value = 11
            else:
                value = 10
            deck.append(
                {
                    "rank": rank,
                    "suit": suit,
                    "value": value
                }
            )
    random.shuffle(deck)

while True:
    start()

    dealer_hand = []
    player_hand = []
    dealer_score = []
    player_score = []

    card = deck.pop()
    dealer_hand.append(card)
    card = deck.pop()
    player_hand.append(card)
    card = deck.pop()
    dealer_hand.append(card)
    card = deck.pop()
    player_hand.append(card)
    card = deck.pop()
    dealer_hand.append(card)
    card = deck.pop()
    player_hand.append(card)
    card = deck.pop()
    dealer_hand.append(card)
    card = deck.pop()
    player_hand.append(card)
    print("Dealer hand:")
    for card in dealer_hand:
        print(f"{card['rank']}{card['suit']}")
        dealer_score.append(
            card['value']
        )
    usable_aces = 0
    ace_count = 0
    dealer_total = sum(dealer_score)
    for card in dealer_hand:
        if card['rank'] == "A":
            usable_aces += 1
            ace_count += 1
            if dealer_total > 21:
                dealer_total -= 10
                usable_aces -= 1
                continue
    print(dealer_total)
    print(usable_aces)
    print(ace_count) #make ace logic a function and rework how scoring is handled
    print("\nYour hand:")
    for card in player_hand:
        print(f"{card['rank']}{card['suit']}")
        player_score.append(
            card['value']
        )
    found = False
    for card in player_hand:
        player_total = sum(player_score)
        if card['rank'] == "A":
            found = True
        if found:
            if sum(player_score) > 13:
                player_total = sum(player_score) - 10
                continue
        if not found:
            continue
    print(player_total)

    break
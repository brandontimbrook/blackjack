import random

deck = []

def start():
    suits = ["hearts", "diamonds", "spades", "clubs"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    for suit in suits:
        for rank in ranks:
            if rank.isdigit():
                value = int(rank)
            elif rank.strip().lower() == "ace":
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

    card = deck.pop()
    dealer_hand.append(card)
    card = deck.pop()
    player_hand.append(card)
    card = deck.pop()
    dealer_hand.append(card)
    card = deck.pop()
    player_hand.append(card)
    print("Dealer hand:")
    total1 = []
    total2 = []
    for card in dealer_hand:
        print(f"{card['rank']} of {card['suit']}")
        total1.append(
            card['value']
        )
    print(sum(total1))
    print("\nYour hand:")
    for card in player_hand:
        print(f"{card['rank']} of {card['suit']}")
        total2.append(
            card['value']
        )
    print(sum(total2))
    break
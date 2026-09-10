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

def deal_card(hand):
    card = deck.pop()
    hand.append(card)

def play(hand):
    hand_score = score_hand(hand)

    while True:
        

        if hand_score > 21:
            return hand_score

        elif hand_score == 21 and len(hand) == 2:
            print(f"\nBLACKJACK! Player has {hand_score}.\n")
            hand_score = score_hand(hand)
            return hand_score
        elif hand_score == 21:
            print(f"\nPlayer has {hand_score}!")
            return hand_score
        
        hit_stand = input("\nHit or Stand? ")
        
        if hit_stand.strip().lower() == "h":
            deal_card(hand)
            show_hand(hand)
            hand_score = score_hand(hand)
            
            if hand_score < 21:
                continue

        if hit_stand.strip().lower() == "s":
            show_hand(hand)
            hand_score = score_hand(hand)
            print(f"\nPlayer stands with {hand_score}.")
            return hand_score

def dealer(hand):
    hand_score = score_hand(hand)
    

    while True:

        if hand_score > 21:
            print(f"\nDealer busts with {hand_score}!")
            return hand_score
        elif hand_score == 21 and len(hand) == 2:
            print(f"\nBLACKJACK! Dealer has {hand_score}.")
            return hand_score
        elif hand_score == 21:
            print(f"\nDealer has {hand_score}!")
            return hand_score

        if hand_score <= 16:
            deal_card(hand)
            print("\nDealer draws:")
            show_hand(hand)
            hand_score = score_hand(hand)
            continue
        elif hand_score > 16:
            hand_score = score_hand(hand)
            print(f"\nDealer stands with {hand_score}.")
            return hand_score
        
def show_hand(hand):

    for card in hand:
        print(f"{card['rank']}{card['suit']}", end=" ")

    print()

def aces(hand):
    usable_aces = 0

    for card in hand:
        if card['rank'] == "A":
            usable_aces += 1

    return usable_aces

def score_hand(hand):
    score = []
    usable_aces = aces(hand)

    for card in hand:
        score.append(card['value'])

    hand_score = sum(score)

    while hand_score > 21 and usable_aces > 0:
        hand_score -= 10
        usable_aces -= 1
    return hand_score

while True:
    start()

    dealer_hand = []
    player_hand = []

    deal_card(dealer_hand)
    deal_card(player_hand)
    deal_card(dealer_hand)
    deal_card(player_hand)

    print("\n================ BLACKJACK ================\n")

    print("Dealer Hand:")
    show_hand(dealer_hand)
    score_hand(dealer_hand)

    print("\nPlayer Hand:")
    show_hand(player_hand)
    score_hand(player_hand)

    print("\n-------------------------------------------")

    play(player_hand)
    player_score = score_hand(player_hand)
    if player_score > 21:
        print(f"\nPlayer busts with {player_score}!")
        print("\n================ RESULT ===================")
        print("Dealer wins!")
        break
    else:
        print("\n------------- DEALER'S TURN ---------------\n")
        print("Dealer Hand:")
        show_hand(dealer_hand)
        dealer(dealer_hand)
        dealer_score = score_hand(dealer_hand)
        if dealer_score > 21:
            print("\n================ RESULT ===================")
            print(f"Player wins! {player_score}")
            break
        elif dealer_score <= 21:
            if player_score > dealer_score:
                print("\n================ RESULT ===================")
                print(f"Player wins! {player_score}")
                break
            elif player_score < dealer_score:
                print("\n================ RESULT ===================")
                print(f"Dealer wins! {dealer_score}")
                break
            elif player_score == dealer_score:
                print("\n================ RESULT ===================")
                print(f"Push! Both finish with {player_score}.")    
                continue

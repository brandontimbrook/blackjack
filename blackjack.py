import random

def base_deck(deck):
    suits = ["♥", "♦", "♠", "♣"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    for suit in suits:
        for rank in ranks:

            if rank.isdigit():
                value = int(rank)

            elif rank == "A":
                value = 11

            else:
                value = 10

            deck.append({
                "rank": rank,
                "suit": suit,
                "value": value
            })

    random.shuffle(deck)

def dealer_deal_card(hand):
    hand.append(dealer_deck.pop())

def player_deal_card(hand):
    hand.append(player_deck.pop())

def player_turn(hand):
    hand_score = score_hand(hand)
    player_blackjack = False

    while True:

        if hand_score > 21:
            return hand_score, player_blackjack

        if hand_score == 21 and len(hand) == 2:
            player_blackjack = True
            print(f"\nBLACKJACK! Player has {hand_score}.\n")
            return hand_score, player_blackjack

        if hand_score == 21:
            print(f"\nPlayer has {hand_score}!")
            return hand_score, player_blackjack

        hit_stand = input("\nHit or Stand? ").strip().lower()

        if hit_stand == "h":
            player_deal_card(hand)
            show_hand(hand)
            hand_score = score_hand(hand)
            continue

        if hit_stand == "s":
            show_hand(hand)
            print(f"\nPlayer stands with {hand_score}.")
            return hand_score, player_blackjack

def dealer_turn(hand):
    hand_score = score_hand(hand)
    dealer_blackjack = False

    while True:

        if hand_score > 21:
            print(f"\nDealer busts with {hand_score}!")
            return hand_score, dealer_blackjack

        if hand_score == 21 and len(hand) == 2:
            dealer_blackjack = True
            print(f"\nBLACKJACK! Dealer has {hand_score}.")
            return hand_score, dealer_blackjack

        if hand_score == 21:
            print(f"\nDealer has {hand_score}!")
            return hand_score, dealer_blackjack

        if hand_score <= 16:
            dealer_deal_card(hand)
            print("\nDealer draws:")
            show_hand(hand)
            hand_score = score_hand(hand)
            continue

        print(f"\nDealer stands with {hand_score}.")
        return hand_score, dealer_blackjack
        
def show_hand(hand):

    for card in hand:
        print(f"{card['rank']}{card['suit']}", end=" ")

    print()

def show_dealer(hand):

    for index, card in enumerate(hand):
        if index == 0:
            print("??", end= " ")
        else:
            print(f"{card['rank']}{card['suit']}", end= " ")

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

def win_conditions(player_score, player_blackjack, dealer_score, dealer_blackjack):
    player_wins = False
    dealer_wins = False
    player_bust = False
    dealer_bust = False

    print("\n================ RESULT ===================")

    if player_score > 21:
        print(f"\nDealer wins!. Player busts with {player_score}!")
        dealer_wins = True
        player_bust = True
        return player_wins, dealer_wins, player_bust, dealer_bust

    if dealer_score > 21:
        print(f"Player wins! Dealer busts with {dealer_score}.")
        player_wins = True
        dealer_bust = True
        return player_wins, dealer_wins, player_bust, dealer_bust

    if player_blackjack and dealer_blackjack:
        print("Push! Both players have BLACKJACK.")
        return player_wins, dealer_wins, player_bust, dealer_bust

    if player_blackjack:
        print("Player has BLACKJACK! Player wins.")
        player_wins = True
        return player_wins, dealer_wins, player_bust, dealer_bust

    if dealer_blackjack:
        print("Dealer has BLACKJACK! Dealer wins.")
        dealer_wins = True
        return player_wins, dealer_wins, player_bust, dealer_bust
    
    if player_score > dealer_score:
        print(f"Player wins! {player_score}")
        player_wins = True
        return player_wins, dealer_wins, player_bust, dealer_bust

    if player_score < dealer_score:
        print(f"Dealer wins! {dealer_score}")
        dealer_wins = True
        return player_wins, dealer_wins, player_bust, dealer_bust

    

    print(f"Push! Both players finish with {player_score}.")
    return player_wins, dealer_wins, player_bust, dealer_bust

while True:
    dealer_deck = []
    player_deck = []
    player_hp = 30
    dealer_hp = 30

    base_deck(dealer_deck)
    base_deck(player_deck)

    while True:
        dealer_hand = []
        player_hand = []

        dealer_deal_card(dealer_hand)
        player_deal_card(player_hand)
        dealer_deal_card(dealer_hand)
        player_deal_card(player_hand)

        print("\n================ BLACKJACK ================\n")
        print(f"Dealer HP - {dealer_hp}")
        print(f"Player HP - {player_hp}\n")

        print("Dealer Hand:")
        show_dealer(dealer_hand)

        print("\nPlayer Hand:")
        show_hand(player_hand)

        print("\n------------- PLAYER'S TURN ---------------\n")

        player_score, player_blackjack = player_turn(player_hand)

        dealer_score = score_hand(dealer_hand)
        dealer_blackjack = dealer_score == 21 and len(dealer_hand) == 2

        if player_score <= 21:
            print("\n------------- DEALER'S TURN ---------------\n")
            print("Dealer Hand:")
            show_hand(dealer_hand)

            if not player_blackjack:
                dealer_score, dealer_blackjack = dealer_turn(dealer_hand)

        player_wins, dealer_wins, player_bust, dealer_bust = win_conditions(
            player_score,
            player_blackjack,
            dealer_score,
            dealer_blackjack
        )

        if player_wins and dealer_bust:
            dealer_hp -= dealer_score - player_score
            print(f"Player does {dealer_score - player_score} damage!")
        elif player_wins:
                dealer_hp -= player_score - dealer_score
                print(f"Player does {player_score - dealer_score} damage!")
        if dealer_wins and player_bust:
            player_hp -= player_score - dealer_score
            print(f"Dealer does {player_score - dealer_score} damage!")
        elif dealer_wins:
            player_hp -= dealer_score - player_score
            print(f"Dealer does {dealer_score - player_score} damage!")

        
        if dealer_hp <= 0:
            print("Dealer has been DEFEATED!")
            break
            
        if player_hp <=0:
            print("Player has been RESHUFFLED!")
            break
    break
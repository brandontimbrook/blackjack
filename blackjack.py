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

def deal_card(hand, deck, discard):
    if len(deck) == 0:
        reshuffle(deck, discard)
    hand.append(deck.pop())

def discard_hand(discard, hand):
    while hand:
        discard.append(hand.pop())

def reshuffle(deck, discard):
    while discard:
        deck.append(discard.pop())
    random.shuffle(deck)

def p_turn(hand, deck, discard):
    p_score = score_hand(hand)
    p_blackjack = False

    while True:

        if p_score > 21:
            return p_score, p_blackjack

        if is_blackjack(p_score, hand):
            p_blackjack = True
            print(f"\nBLACKJACK! Player has {p_score}.\n")
            return p_score, p_blackjack

        if p_score == 21:
            print(f"\nPlayer has {p_score}!")
            return p_score, p_blackjack

        hit_stand = input("\nHit or Stand? ").strip().lower()

        if hit_stand == "h":
            deal_card(hand, deck, discard)
            show_hand(hand)
            p_score = score_hand(hand)
            continue

        if hit_stand == "s":
            show_hand(hand)
            print(f"\nPlayer stands with {p_score}.")
            return p_score, p_blackjack

def enemy_turn(hand, deck, discard):
    enemy_score = score_hand(hand)
    enemy_blackjack = False

    while True:

        if enemy_score > 21:
            return enemy_score, enemy_blackjack

        if is_blackjack(enemy_score, hand):
            enemy_blackjack = True
            return enemy_score, enemy_blackjack

        if enemy_score == 21:
            return enemy_score, enemy_blackjack

        if enemy_score <= 16:
            deal_card(hand, deck, discard)
            enemy_score = score_hand(hand)
            continue

        return enemy_score, enemy_blackjack
        
def show_hand(hand):

    for card in hand:
        print(f"{card['rank']}{card['suit']}", end=" ")

    print()

def show_hidden(hand):

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

def is_blackjack(score, hand):
    return score == 21 and len(hand) == 2

def win_conditions(p_score, p_blackjack, enemy_score, enemy_blackjack):
    p_wins = False
    enemy_wins = False
    p_bust = False
    enemy_bust = False

    if p_score > 21:
        enemy_wins = True
        p_bust = True
        return p_wins, enemy_wins, p_bust, enemy_bust

    if enemy_score > 21:
        p_wins = True
        enemy_bust = True
        return p_wins, enemy_wins, p_bust, enemy_bust

    if p_blackjack and enemy_blackjack:
        return p_wins, enemy_wins, p_bust, enemy_bust

    if p_blackjack:
        p_wins = True
        return p_wins, enemy_wins, p_bust, enemy_bust

    if enemy_blackjack:
        enemy_wins = True
        return p_wins, enemy_wins, p_bust, enemy_bust
    
    if p_score > enemy_score:
        p_wins = True
        return p_wins, enemy_wins, p_bust, enemy_bust

    if p_score < enemy_score:
        enemy_wins = True
        return p_wins, enemy_wins, p_bust, enemy_bust

    return p_wins, enemy_wins, p_bust, enemy_bust

while True:

    enemy_deck = []
    p_deck = []
    p_hand = []
    enemy_hand = []
    p_discard = []
    enemy_discard = []

    enemy_name = "Casino Dealer"

    p_hp = 30
    enemy_hp = 30

    base_deck(enemy_deck)
    base_deck(p_deck)

    while True:

        deal_card(enemy_hand, enemy_deck, enemy_discard)
        deal_card(p_hand, p_deck, p_discard)
        deal_card(enemy_hand, enemy_deck, enemy_discard)
        deal_card(p_hand, p_deck, p_discard)

        print("\n================ BLACKJACK ================\n")
        print(f"{enemy_name} HP - {enemy_hp}")
        print(f"Player HP - {p_hp}\n")

        print(f"{enemy_name} Hand:")
        show_hidden(enemy_hand)

        print("\nPlayer Hand:")
        show_hand(p_hand)

        print("\n------------- PLAYER'S TURN ---------------\n")

        p_score, p_blackjack = p_turn(p_hand, p_deck, p_discard)

        enemy_score = score_hand(enemy_hand)

        if p_score <= 21:
            print(f"\n------------- {enemy_name}'S TURN ---------------\n")
            print(f"{enemy_name} Hand:")
            show_hand(enemy_hand)

            if not p_blackjack:
                if enemy_score <= 16:
                    print(f"\n{enemy_name} draws:")
                enemy_score, enemy_blackjack = enemy_turn(enemy_hand, enemy_deck, enemy_discard)
                show_hand(enemy_hand)
                if enemy_score > 21:
                    print(f"\n{enemy_name} busts with {enemy_score}!")
                
                elif enemy_score == 21:
                    print(f"\n{enemy_name} has {enemy_score}!")
                else:
                    print(f"\n{enemy_name} stands with {enemy_score}.")
                

        p_wins, enemy_wins, p_bust, enemy_bust = win_conditions(
            p_score,
            p_blackjack,
            enemy_score,
            enemy_blackjack
        )
        print("\n================ RESULT ===================")

        if p_bust:
            print(f"\n{enemy_name} wins!. Player busts with {p_score}!")
        elif enemy_bust:
            print(f"Player wins! {enemy_name} busts with {enemy_score}.")
        elif p_blackjack and enemy_blackjack:
            print("Push! Both players have BLACKJACK.")
        elif p_blackjack:
            print("Player has BLACKJACK! Player wins.")
        elif enemy_blackjack:
            print(f"{enemy_name} has BLACKJACK! {enemy_name} wins.")
        elif p_score > enemy_score:
            print(f"Player wins! {p_score}")
        elif p_score < enemy_score:
            print(f"{enemy_name} wins! {enemy_score}")
        else:
            print(f"Push! Both players finish with {p_score}.")

        damage = abs(p_score - enemy_score)

        if p_wins:
            enemy_hp -= damage
            print(f"Player does {damage} damage!")
        elif enemy_wins:
            p_hp -= damage
            print(f"{enemy_name} does {damage} damage!")

        discard_hand(p_discard, p_hand)
        discard_hand(enemy_discard, enemy_hand)

        
        
        #if enemy_hp <= 0:
            #print(f"{enemy_name} has been DEFEATED!")
            #p_bank += 8
            #rewards(scaling special chips/common 1.2x base multiplier/common extra $1 interest on current bank at end of round/ uncommon/ rare/ epic??)
            #shop(buy special_card's/ wild for value/ choose one card from p_deck to draw to hand/ blank_card??/ remove_card from p_deck/ lock shop??)
            #enemy_hp = 50
            #enemy_name = "Ol' Smokey"
            
            
        if p_hp <=0:
            print("Player has been RESHUFFLED!")
            new_game = input("Start a new game? ")
            if new_game == "y":
                continue
            elif new_game == "n":
                break

    break
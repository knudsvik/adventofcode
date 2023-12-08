filename = '2023/input/day7.txt'
lines = open(filename, 'r').readlines()

highs = {}
pairs = {}
like5 = {}
like4 = {}
like3 = {}
houses = {}
pairs2 = {}


for line in lines:
    hand, bet = line.split()
    if len(set(hand)) == 5:
        highs[hand] = bet
        continue
    elif len(set(hand)) == 4:
        pairs[hand] = bet
        continue
    elif len(set(hand)) == 1:
        like5[hand] = bet
        continue

    cards = {}
    for card in hand:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    
    if any(count == 4 for count in cards.values()):
        like4[hand] = bet
        continue
    elif any(count == 3 for count in cards.values()) and not any(count == 2 for count in cards.values()):
        like3[hand] = bet
        continue
    elif any(count == 3 for count in cards.values()) and any(count == 2 for count in cards.values()):
        houses[hand] = bet
        continue
    elif any(count == 2 for count in cards.values()) and any(count == 1 for count in cards.values()):
        pairs2[hand] = bet
    

def card_value(card):
    if card.isdigit():
        return int(card)
    elif card == 'T':
        return 10
    elif card == 'J':
        return 11
    elif card == 'Q':
        return 12
    elif card == 'K':
        return 13
    elif card == 'A':
        return 14

all_hands = [highs, pairs, pairs2, like3, houses, like4, like5]

rank = 1
winnings = 0

for hand_dict in all_hands:
    sorted_items = sorted(hand_dict.items(), key=lambda item: [card_value(card) for card in item[0]])
    for i in sorted_items:
        winnings += int(i[1]) * rank
        rank += 1
    # hand_dict.clear()
    # hand_dict.update(sorted_items)

print(winnings)
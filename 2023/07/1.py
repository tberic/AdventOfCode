cardValues = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def isFiveOfKind(hand):
    return hand[0] == hand[1] and hand[1] == hand[2] and hand[2] == hand[3] and hand[3] == hand[4]

def isFourOfKind(hand):
    hand = sorted(hand)
    return hand[0] == hand[1] and hand[1] == hand[2] and hand[2] == hand[3] or \
           hand[1] == hand[2] and hand[2] == hand[3] and hand[3] == hand[4]

def isFullHouse(hand):
    hand = sorted(hand)
    return hand[0] == hand[1] and hand[1] == hand[2] and hand[3] == hand[4] or \
           hand[0] == hand[1] and hand[2] == hand[3] and hand[3] == hand[4]           

def isThreeOfKind(hand):
    hand = sorted(hand)
    return hand[0] == hand[1] and hand[1] == hand[2] or \
           hand[1] == hand[2] and hand[2] == hand[3] or \
           hand[2] == hand[3] and hand[3] == hand[4]           

def isTwoPair(hand):
    hand = sorted(hand)
    return hand[1] == hand[2] and hand[3] == hand[4] or \
           hand[0] == hand[1] and hand[3] == hand[4] or \
           hand[0] == hand[1] and hand[2] == hand[3]

def isOnePair(hand):
    hand = sorted(hand)
    return hand[0] == hand[1]  or hand[1] == hand[2] or hand[2] == hand[3] or hand[3] == hand[4]

def classify(hand):
    # print(hand, end=': ')
    if isFiveOfKind(hand):
        # print("Five of a kind")
        return 1
    if isFourOfKind(hand):
        # print("Four of a kind")
        return 2
    if isFullHouse(hand):
        # print("Full house")
        return 3
    if isThreeOfKind(hand):
        # print("Three of a kind")
        return 4
    if isTwoPair(hand):
        # print("Two pairs")
        return 5
    if isOnePair(hand):
        # print("One pair")
        return 6
    # print("High card")
    return 7

def compare(hand1, hand2):
    score1 = classify(hand1)
    score2 = classify(hand2)

    if score1 == score2:
        if hand1[0] != hand2[0]:
            return cardValues.index(hand1[0]) - cardValues.index(hand2[0])
        if hand1[1] != hand2[1]:
            return cardValues.index(hand1[1]) - cardValues.index(hand2[1])
        if hand1[2] != hand2[2]:
            return cardValues.index(hand1[2]) - cardValues.index(hand2[2])
        if hand1[3] != hand2[3]:
            return cardValues.index(hand1[3]) - cardValues.index(hand2[3])
        if hand1[4] != hand2[4]:
            return cardValues.index(hand1[4]) - cardValues.index(hand2[4])

    return score1 - score2


f = open('input.txt', 'r')

lines = [line.strip() for line in f if line.strip() != ""]

hands = []
bids = []
for line in lines:
    hand, bid = line.split(' ')
    hands.append(hand)
    bids.append(int(bid))

for i in range(len(hands)):
    for j in range(i+1, len(hands)):
        if compare(hands[i], hands[j]) < 0:
            tmpHand = hands[i]
            hands[i] = hands[j]
            hands[j] = tmpHand
            tmpBid = bids[i]
            bids[i] = bids[j]
            bids[j] = tmpBid

winnings = 0
for i in range(len(hands)):
    winnings += bids[i] * (i+1)

print(winnings)

# print(hands)
# print(bids)
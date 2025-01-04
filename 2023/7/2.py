cardValues = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

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
    if isFiveOfKind(hand):
        return 1
    if isFourOfKind(hand):        
        return 2
    if isFullHouse(hand):
        return 3
    if isThreeOfKind(hand):
        return 4
    if isTwoPair(hand):
        return 5
    if isOnePair(hand):
        return 6
    return 7

def classifyWithJokers(hand):    
    if 'J' not in hand:
        return classify(hand)
    
    best = 10
    for card in cardValues[:-1]:
        newHand = hand.replace('J', card, 1)
        res = classifyWithJokers(newHand)
        if res < best:
            best = res

    return best

def compare(hand1, hand2, type1, type2):
    if type1 == type2:
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

    return type1 - type2


f = open('input.txt', 'r')

lines = [line.strip() for line in f if line.strip() != ""]

hands = []
bids = []
handTypes = []
for line in lines:
    hand, bid = line.split(' ')
    hands.append(hand)
    bids.append(int(bid))
    handTypes.append(classifyWithJokers(hand))

print('Classification done')

for i in range(len(hands)):
    for j in range(i+1, len(hands)):
        if compare(hands[i], hands[j], handTypes[i], handTypes[j]) < 0:
            tmpHand = hands[i]
            hands[i] = hands[j]
            hands[j] = tmpHand
            tmpBid = bids[i]
            bids[i] = bids[j]
            bids[j] = tmpBid
            tmpType = handTypes[i]
            handTypes[i] = handTypes[j]
            handTypes[j] = tmpType

winnings = 0
for i in range(len(hands)):
    winnings += bids[i] * (i+1)

print(winnings)
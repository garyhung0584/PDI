def isValidCard(card: str) -> bool:
    valid_cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    return card in valid_cards

def validInput(cards: list) -> bool:
    validflag = True
    for card in cards:
        if not isValidCard(card):
            validflag = False
            break
    return validflag

def transferPoint(card: str) -> float:
    porker = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    point = [1,2,3,4,5,6,7,8,9,10,0.5,0.5,0.5]
    index = porker.index(card)
    return point[index]

def justPoint(point: float) -> float:
    if point > 10.5:
        return 0
    else:
        return point
    
def deal(myPoint: float, card: str) -> float:
    myPoint += transferPoint(card)
    myPoint = justPoint(myPoint)
    return myPoint

def winner(playerPoint: float, computerPoint: float) -> str:
    if playerPoint > computerPoint:
        return 'player win ' + str(playerPoint) + ' ' + str(computerPoint)
    elif playerPoint < computerPoint:
        return 'computer win ' + str(playerPoint) + ' ' + str(computerPoint)
    else:
        return 'tie ' + str(playerPoint)
    
def game(playerCards: list, computerCards: list) -> str:
    if validInput(playerCards) and validInput(computerCards):
        playerPoint = transferPoint(playerCards[0])
        computerPoint = transferPoint(computerCards[0])
        playerIndex, computerIndex = 1, 1
        playerBust, computerBust = False, False
        while playerIndex < len(playerCards) and playerBust == False:
            playerPoint = deal(playerPoint, playerCards[playerIndex])

            if playerPoint == 0:
                playerBust = True
            else:
                playerIndex += 1
        while computerIndex < len(computerCards) and computerBust == False:
            computerPoint = deal(computerPoint, computerCards[computerIndex])
            if computerPoint == 0:
                computerBust = True
            else:
                computerIndex += 1
        return winner(playerPoint, computerPoint)
    else:
        return 'Error input'
    
def inputData() -> list:
    playerCardsStr = input()
    computerCardsStr = input()
    playerCards = playerCardsStr.split()
    computerCards = computerCardsStr.split()
    return playerCards, computerCards

def testgame():
    playerCards, computerCards = inputData()
    result = game(playerCards, computerCards)
    print(result)

if __name__ == '__main__':
    testgame()
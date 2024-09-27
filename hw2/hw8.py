xCard1 = str(input())
xCard2 = str(input())
xCard3 = str(input())
yCard1 = str(input())
yCard2 = str(input())
yCard3 = str(input())

xCards = [xCard1, xCard2, xCard3]
yCards = [yCard1, yCard2, yCard3]

xValue = 0
yValue = 0
for card in xCards:
    if card in ("J", "Q", "K"):
        card = 0.5
    elif card == "A":
        card = 1
    else:
        card = int(card)
    xValue += card


for card in yCards:
    if card in ("J", "Q", "K"):
        card = 0.5
    elif card == "A":
        card = 1
    else:
        card = int(card)
    yValue += card

if xValue > 10.5:
    xValue = 0
if yValue > 10.5:
    yValue = 0
if not xValue % 1:
    xValue = int(xValue)
if not yValue % 1:
    yValue = int(yValue)
print(f"{xValue}\n{yValue}")
if xValue > yValue:
    print("X Win")
elif xValue < yValue:
    print("Y Win")
if xValue == yValue:
    print("Tie")

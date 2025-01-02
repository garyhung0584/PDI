def isvalid(invo):
    return len(invo) == 8 and invo.isdigit()


def isInPeriod(invo, s):
    periods = [s[:7], s[:5] + s[8:]]
    if invo[:7] in periods:
        return True
    return False


def getPrize(invoice_num, prize_numbers):
    for i, prize_set in enumerate(prize_numbers):
        for prize in prize_set:
            if invoice_num.endswith(prize):
                return i
    return -1


def main():
    invos = []
    storeNum = {}
    highest_profit = (0, 0)
    PossiblePrizes = {
        0: ("Special", 10000000),
        1: ("Grand", 2000000),
        2: ("1st", 200000),
        3: ("2nd", 40000),
        4: ("3rd", 10000),
        5: ("4th", 4000),
        6: ("5th", 1000),
        7: ("6th", 200),
    }

    # Input: first line - winning numbers and period range
    s = input().split()
    n = int(input())  # number of invoices

    # Process all the invoices
    for _ in range(n):
        invo = input().split()
        invos.append(invo)

    prize_numbers = [
        [s[0]],
        [s[1]],
        [i for i in s[2:-1]],
        [i[-7:] for i in s[2:-1]],
        [i[-6:] for i in s[2:-1]],
        [i[-5:] for i in s[2:-1]],
        [i[-4:] for i in s[2:-1]],
        [i[-3:] for i in s[2:-1]],
    ]

    for i in range(n):
        invo_number, store, date, amount = invos[i]

        # Check if the invoice number is valid
        if not isvalid(invo_number):
            print("{} has an invalid format.".format(invo_number))
            continue

        # Check if the invoice is within the prize period
        if not isInPeriod(date, s[5]):
            print("{} is outside the prize period.".format(invo_number))
            continue

        prize_index = getPrize(invo_number, prize_numbers)

        if prize_index == -1:
            print("{} did not win anything.".format(invo_number))
            continue

        prize_name, prize_value = PossiblePrizes[prize_index]
        profit = prize_value - int(amount)

        print(
            "{} won: {} Prize: {} TWD Profit: {} TWD".format(
                invo_number, prize_name, prize_value, profit
            )
        )

        # Track the store's number of winning invoices
        storeNum[store] = storeNum.get(store, 0) + 1

        # Track highest profit
        if profit > highest_profit[1]:
            highest_profit = (i, profit)

    # If no invoices have won any prize
    if highest_profit[1] == 0:
        print("No invoices won any prize.")
        return

    # Store with the most winning invoices
    max_store = max(storeNum.items(), key=lambda x: x[1])
    print(
        "Store {} opened the most winning invoices: {}".format(
            max_store[0], max_store[1]
        )
    )

    # Invoice with the highest profit
    highest_invoice = invos[highest_profit[0]]
    invoice_number, store, date, amount = highest_invoice
    prize_index = getPrize(invoice_number, prize_numbers)
    prize_name, prize_value = PossiblePrizes[prize_index]
    print(
        "Invoice with the highest profit: {}, from store {}, purchase date {}, total prize {} TWD, profit {} TWD".format(
            invoice_number, store, date, prize_value, highest_profit[1]
        )
    )


if __name__ == "__main__":
    main()

def isNumSep(password):
    for i in range(len(password) - 1):
        if password[i].isdigit() and password[i + 1].isdigit():
            return False
    return True


def check_id(id):
    area_code_map = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
        "G": 16,
        "H": 17,
        "I": 34,
        "J": 18,
        "K": 19,
        "L": 20,
        "M": 21,
        "N": 22,
        "O": 35,
        "P": 23,
        "Q": 24,
        "R": 25,
        "S": 26,
        "T": 27,
        "U": 28,
        "V": 29,
        "W": 32,
        "X": 30,
        "Y": 31,
        "Z": 33,
    }

    weight = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    if id[0] in area_code_map:
        id = str(area_code_map[id[0]]) + id[1:]
    else:
        print("Wrong area code")
        return

    if id[2] not in {"1", "2"}:
        print("Wrong gender code")
        return

    check = sum([weight[i] * int(id[i]) for i in range(len(weight))])
    check = 10 - check % 10 if check % 10 != 0 else 0

    if id[-1] == str(check):
        print("Pass")
    else:
        print("Illegal")


def check_password(password):
    score = 0

    score += sum([3 for i in password if i.isupper()])
    score += sum([1 for i in password if i.islower()])
    score += sum([5 for i in password if i in "{ ~!@#$%^&*<>_+=}"])

    digit_score = [2 for i in password if i.isdigit()]
    score += sum(digit_score)
    if len(digit_score) >= 5 and isNumSep(password):
        score += 15

    if score >= 30:
        print(score)
    else:
        print(score, "Not strong enough")


def main():

    id = input()
    password = input()

    check_id(id)
    check_password(password)


if __name__ == "__main__":
    main()

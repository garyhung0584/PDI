def main():
    s = input().strip()

    # Check length and format
    if len(s) != 8 or s[3] != "-":
        print(s + " is Invalid license plate number.")
        return

    word, num = s[:3], s[4:]

    # Validate word part
    if not word.isalpha() or "I" in word or "O" in word:
        print(s + " is Invalid license plate number.")
        return

    # Validate number part
    if not num.isdigit() or "4" in num:
        print(s + " is Invalid license plate number.")
        return

    # Check banned words
    BANNED = {
        "FUC",
        "FUG",
        "FUQ",
        "FUT",
        "GPU",
        "KGB",
        "KKK",
        "KMT",
        "DPP",
        "PUG",
        "PUP",
        "CAT",
        "ANT",
        "APE",
        "MAD",
        "NUN",
        "SEX",
        "SLY",
        "BAD",
        "GAY",
        "ASS",
        "BUM",
        "BRA",
        "CRY",
    }
    if word in BANNED:
        print(s + " is Invalid license plate number.")
        return

    print(s + " is Valid license plate number.")


if __name__ == "__main__":
    main()

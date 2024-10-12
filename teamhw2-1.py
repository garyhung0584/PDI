def forOps():
    i = 1
    myList = ["asm", "C", "python", "C++", "Java", "iOS", "Ruby", "perl", "delphi"]
    for index in myList:
        if index == "python":
            print(i, index)
        elif index == "Java":
            print(i, index)
        elif i % 3 != 0:
            print(i, index)
            i = i + 1
        else:
            i = i + 1


forOps()

def ex(n):
    student = {}
    for _ in range(n):
        name = input("Name:")
        score = int(input("Score:"))
        student[name] = score
    name = input("del Name")
    print("average = ", (sum(student.values())) / n)

    del student[name]
    for name, score in student.items():
        print(name, score)


ex(2)

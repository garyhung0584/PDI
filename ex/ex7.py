# def ex(n):
#     student = {}
#     for _ in range(n):
#         name = input("Name:")
#         score = int(input("Score:"))
#         student[name] = score
#     name = input("del Name")
#     print("average = ", (sum(student.values())) / n)

#     del student[name]
#     for name, score in student.items():
#         print(name, score)


# ex(2)

import re

PRIME = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
front = "AEHG"
backs = ["TAA", "TAG", "TGA"]
txt = "AEHGTTTTAAALSKFj;akAEHGFALKJTAAKFj;akAEHGFALKJTGA"

back = "|".join(backs)
exp = front + "[A-Z]+(?:" + back + ")"

x = re.findall(exp, txt)
x = [i[4:-3] for i in x if len(i[4:-3]) in PRIME]
print(x)

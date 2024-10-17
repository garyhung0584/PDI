ALLOWED_TIME = ['1','2','3',"4",'5','6','7','8','9','a','b','c']

n = int(input())
if n < 2 or n > 10:
    exit()
courseTable = []
for i in range(n):
    timeTable = []
    courseId = str(input())
    courseHour = int(input())
    for j in range(courseHour):
        time = input()
        timeTable.append(time)
    courseTable.append([courseId,timeTable])
conflict = []
for i in range(len(courseTable)):
    for j in range(len(courseTable[i][1])):
        if courseTable[i][1][j][1] not in ALLOWED_TIME or int(courseTable[i][1][j][0]) > 5 or int(courseTable[i][1][j][0]) < 1 :
            print("-1")
            exit()
        count = i + 1
        while count < n:
            if courseTable[i][1][j] in courseTable[count][1]:
                conflict.append(f"{courseTable[i][0]},{courseTable[count][0]},{courseTable[i][1][j]}")
            count += 1
if not conflict:
    print("correct")
    exit()

for i in conflict:
    print(i)
course1id = int(input())
course1time1 = int(input())
course1time2 = int(input())
course2id = int(input())
course2time1 = int(input())
course2time2 = int(input())
course3id = int(input())
course3time1 = int(input())
course3time2 = int(input())

table = {
    course1id: [course1time1, course1time2],
    course2id: [course2time1, course2time2],
    course3id: [course3time1, course3time2],
}

id = [course1id, course2id, course3id]
id.sort()

i = 0
compare1 = [x for x in table[id[i]] if x in table[id[i + 1]]]
compare2 = [x for x in table[id[i]] if x in table[id[i + 2]]]
compare3 = [x for x in table[id[i + 1]] if x in table[id[i + 2]]]
compare1.sort()
compare2.sort()
compare3.sort()
for i in compare1:
    print(f"{id[0]} and {id[1]} conflict on {i}")
for i in compare2:
    print(f"{id[0]} and {id[2]} conflict on {i}")
for i in compare3:
    print(f"{id[1]} and {id[2]} conflict on {i}")
if not compare1 and not compare2 and not compare3:
    print("correct")

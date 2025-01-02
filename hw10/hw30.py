def main():
    schools = []
    queries = []
    conditions = []
    sol = []

    n = int(input())
    for _ in range(n):
        sc = input().split()
        schools.append(sc)

    m = int(input())
    for _ in range(m):
        qu = input().split()
        queries.append(qu)

    b = int(input())

    datatable = {}
    for i in schools:
        datatable[i[0]] = set(i[1:])

    for query in queries:
        condition = [set()]
        now = 0
        for j in query:
            if j != "+":
                condition[now].add(j)
            else:
                now += 1
                condition.append(set())
        conditions.append(condition)

    for condition in conditions:
        if b == 0:
            sol.append([])
        else:
            sol.append({sName: set() for sName in datatable})

        for i in condition:
            for sName in datatable:
                if b == 0:
                    if i.issubset(datatable[sName]):
                        if sName not in sol[-1]:
                            sol[-1].append(sName)
                else:
                    sol[-1][sName] |= i & datatable[sName]

        if b == 1:
            max_matches = max((len(attrs) for attrs in sol[-1].values()), default=0)
            sol[-1] = " ".join(
                sName for sName, attrs in sol[-1].items() if len(attrs) == max_matches
            )

    for result in sol:
        if b == 0:
            result.sort(key=lambda x: [school[0] for school in schools].index(x))
            print(" ".join(result))
        else:
            print(result)


if __name__ == "__main__":
    main()

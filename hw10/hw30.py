def main():
    schools = []
    queries = []
    conditions = []
    results = []

    n = int(input())
    for _ in range(n):
        line = input().split()
        schools.append((line[0], set(line[1:])))

    m = int(input())
    for _ in range(m):
        query = input().split(" + ")
        conditions.append([set(q.split()) for q in query])

    b = int(input())

    for condition in conditions:
        if b == 0:  # Output all schools that fully meet the conditions
            valid_schools = []
            for school_name, attributes in schools:
                if any(
                    all(req.issubset(attributes) for req in option)
                    for option in condition
                ):
                    valid_schools.append(school_name)
            results.append(valid_schools)
        else:  # Output the school(s) that meet the most conditions
            match_counts = {}
            for school_name, attributes in schools:
                match_count = 0
                for option in condition:
                    match_count += sum(1 for req in option if req & attributes)
                match_counts[school_name] = match_count

            max_match = max(match_counts.values(), default=0)
            best_schools = [
                school for school, count in match_counts.items() if count == max_match
            ]
            results.append(best_schools)

    for result in results:
        print(" ".join(result))


if __name__ == "__main__":
    main()

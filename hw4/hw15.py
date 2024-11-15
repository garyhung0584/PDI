n = input()


def parse(n):
    try:
        return int(n)
    except:
        return None


output = [parse(i) for i in n if parse(i)]

if output == output[::-1]:
    output = sorted([i for i in set(output)])
else:
    temp = []
    for _ in range(len(output)):
        n = output.pop()
        if n in output:
            temp.append(n)
    output = sorted([i for i in set(temp)], reverse=True)
print(output)

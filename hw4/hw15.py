n = input()
def parse(n):
    try:
        return int(n)
    except:
        return None
output = [parse(i) for i in n if parse(i)]

if output == output[::-1]:
    output = [i for i in set(output)]
    output.sort()
else:
    temp = []
    for _ in range(len(output)):
        n = output.pop()
        if n in output:
            temp.append(n)
    output = [i for i in set(temp)]
    output.sort(reverse=True)
print(output)
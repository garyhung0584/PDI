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
    print(output)
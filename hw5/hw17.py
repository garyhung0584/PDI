n = int(input())
m = int(input())
c = int(input())

def tower(i):
    for j in range(i-1,-i,-1):
        print(abs(j)+1, end="")

if c == 1:
    for i in range(-n+1,n):
        if m % 2 == 0:
            print("*" * (n - abs(i))+"_" * ((2 * n)- 2*(n - abs(i))) + "*" * (2 * (n - (abs(i)+1)) + 1) + "_" * (abs(i)))
        else:
            print("_" * (abs(i)) + "*" * (2 * (n - (abs(i)+1)) + 1) + "_" * ((2 * n)- 2*(n - abs(i))) + "*" * (n - abs(i)))
elif c == 2:
    for i in range(n):
        if m % 2 != 0:
            i= n-i-1
        print("_"*i,end="")
        tower(n-i)
        print("_"*i)


#a, b = map(int, input().split())
a = input()
y = int(a[-1])
#print(y)
x = a[:-2]
#print(x)

if 0 <= y <= 2:
    x += '-'
    print(x)
elif 3 <= y <= 6:
    print(x)
elif 7 <= y <= 9:
    x += '+'
    print(x)
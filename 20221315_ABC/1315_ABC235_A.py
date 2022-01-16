#A, B = map(int, input().split())
s = input()
a = int(s[0])
b = int(s[1])
c = int(s[2])

abc = 100*a + 10*b + c
bca = 100*b + 10*c + a
cab = 100*c + 10*a + b
print(abc+bca+cab)
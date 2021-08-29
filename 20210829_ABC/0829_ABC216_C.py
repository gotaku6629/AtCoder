n = int(input())

path =  ''
now = 0
while(now != n):
    #print(now)
    a = now + 1
    b = now * 2
    if n - a >= 0 and n - b >= 0:
        if n - a < n - b:
            now = a
            path += 'A'
        else:
            now = b
            path += 'B'
    elif n - a >= 0 and n - b <= 0:
        now = a
        path += 'A'
    elif n - a <= 0 and n - b >= 0:
        now = b
        path += 'B'

print(path)
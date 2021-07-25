s1 = input()
s2 = input()
s3 = input()
s4 = input()


S = []
S.append(s1)
S.append(s2)
S.append(s3)
S.append(s4)

T = [0 for _ in range(4)]

for i in range(4):
    if S[i] == 'H':
        T[0] = 1
    elif S[i] == '2B':
        T[1] = 1
    elif S[i] == '3B':
        T[2] = 1
    elif S[i] == 'HR':
        T[3] = 1

if sum(T) == 4:
    print('Yes')
else:
    print('No')



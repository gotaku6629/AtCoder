N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

"""
count = 0
for i in range(N):
    for j in range(N):
        if A[i] == B[C[j]-1]:
            count += 1
print(count)
"""

A.sort()
B_ = []
for i in range(N):
    B_.append(B[C[i]-1])
B = sorted(B_)
print(A)
print(B)
count = 0
a = 0
b = 0
while(True):

    print(a, b)
    if a == N-1:
        if A[a] == B[b]:
            count += 1
        if b == N-1:
            break
        b += 1

    elif b == N-1:
        if A[a] == B[b]:
            count += 1
        if a == N-1:
            break
        a += 1
    else:
        if A[a] < B[b]:
            a += 1
        elif A[a] > B[b]:
            b += 1        
        else: # A[a] == B[b]:
            count += 1
            if A[a] != A[a+1] and B[b] != B[b+1]:
                a += 1
                b += 1
            elif A[a] == A[a+1] and B[b] == B[b+1]:
                b += 1
            elif A[a] == A[a+1] and B[b] != B[b+1]:
                a += 1
            else: # A[a] != A[a+1] & B[b] == B[b+1]:
                b += 1

    #if a == N-1 and b == N-1:
    #    break
print(count)
    
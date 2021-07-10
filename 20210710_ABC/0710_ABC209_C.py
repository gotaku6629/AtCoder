#統合部
def merge(A, left, mid, right):
    L = A[left:mid]
    R = A[mid:right]
    for i in range(left,right):
        if len(L) == 0:
            A[i] = R.pop(0)
        elif len(R) == 0:
            A[i] = L.pop(0)
        elif L[0] <= R[0]:
            A[i] = L.pop(0)
        else:
            A[i] = R.pop(0)

#分割部
def mergesort(A, left, right):
    if left + 1 < right:
        mid = (left + right)//2
        mergesort(A, left, mid)
        mergesort(A, mid, right)
        merge(A, left, mid, right)
    return A

n = int(input())
c = list(map(int, input().split()))

#c.sort()
c = mergesort(c,0,n)
#print(c)
q = 10**9 + 7

d = [0 for _ in range(n)]
for i in range(n):
    d[i] = (c[i] - i) % q 

sum = 1
for i in range(n):
    sum = sum * d[i]
print(sum%q)
a, n = map(int, input().split())

i = 0
flag = 0
s_tt = str(n)
while(n != 1):
    print(n)
    if n < 10:
        s = str(n)
        s_t = str(n)
    else:        
        s = str(n) # 611
        s_t = s[1:] + s[0] # 116
    print(s_tt, s_t, s)
    if n % a != 0: # 割り切れなかったら、
        if n < 10 and s_tt == s_t:
            i = -1
            break
        else:
            n = int(s_t)
    else: # 割り切れたら、
        if s_tt == s_t:
            n = int(n / a)
        else:
            x1 = int(s_t) 
            x2 = int(n / a)
            if x1 < x2:
                n = x1
            else:
                n = x2
    s_tt = s
    i += 1
        
print(i)
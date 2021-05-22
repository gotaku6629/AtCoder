S = input()

T = ''
for s in range(len(S)):
    if S[len(S)-1-s] == '6':
        T += '9'
    elif S[len(S)-1-s] == '9':
        T += '6'
    else:
        T += S[len(S)-1-s]
print(T)
N, r, c = map(int, input().split())

ans = 0
while N>=0:
    N-=1

    if c < 2**(N):
        if r < 2**(N): # 2사분면
            quad = 2
        else: # 3사분면
            quad = 3
            r -= 2**N
            ans += ((2**N)**2) * 2
    else:
        if r < 2**(N): #1사분면
            quad = 1
            c -= 2**N
            ans += ((2**N)**2) * 1
        else:
            quad = 4
            r -= 2**N
            c -= 2**N
            ans += ((2**N)**2) * 3
    
print(ans)
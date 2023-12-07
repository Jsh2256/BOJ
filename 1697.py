import sys
input = sys.stdin.readline
cnt=0
n, k = map(int, input().split())
if n > k:
    tmp = k
    k = n
    n = tmp
while True:
    if n == k:
        break
    elif n < k:
        if k - n > 1:
            if 2*n <= k:
                if k - 2*n > 1:
                    if (k+n)/2 <= 2*n:
                        n+=1
                        cnt+=1
                    else:
                        n*=2
                        cnt+=1
                else:
                    n*=2
                    cnt+=1
            elif 2*n > k:
                if 2*n - k > 1:
                    n-=1
                    cnt+=1
                else:
                    n*=2
                    cnt+=1
        else:
            n+=1
            cnt+=1
    else:
        if n-k == 1:
            n-=1
            cnt+=1
        

print(cnt)
    
        
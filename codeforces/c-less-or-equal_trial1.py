n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

if k == 0:
    ans = a[0] - 1
    if ans > 0:
        print(ans)
    else:
        print(-1)
elif k == n:
    print(a[k-1])
else:
    if a[k-1] != a[k]:
        print(a[k-1])
    else:
        print(-1)
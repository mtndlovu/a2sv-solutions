n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i = j = 0
ans = []

while i < n and j < m:
    ai = a[i]
    bj = b[j]
    if ai < bj:
        i += 1
        ans.append(ai)
    elif ai > bj:
        ans.append(bj)
        j += 1
    else:
        ans.extend([ai, bj])
        i += 1
        j += 1
        
if i < n:
    ans.extend(a[i:])
elif j < m:
    ans.extend(b[j:])

print(" ".join(map(str, ans)))

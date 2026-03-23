import sys

input = sys.stdin.readline

def solve():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    max_len = 0
    curr_sum = 0
    l = 0

    for r in range(n):
        curr_sum += a[r]
        
        if curr_sum > s:
            curr_sum -= a[l]
            l += 1
        
        max_len = max(max_len, r - l + 1)
    
    return max_len

if __name__  == "__main__":
    print(solve())

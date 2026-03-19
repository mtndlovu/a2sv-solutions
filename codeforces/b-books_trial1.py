import sys

input = sys.stdin.readline

def solve():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    left = 0
    max_books = 0
    curr_sum = 0

    for right in range(n):
        curr_sum += a[right]

        while curr_sum > t and left <= right:
            curr_sum -= a[left]
            left += 1
        max_books = max(max_books, right - left + 1)
    
    print(max_books)

if __name__ == "__main__":
    solve()
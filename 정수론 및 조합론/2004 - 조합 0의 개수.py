import sys

def count_two(n):
    answer = 0
    while n >= 2:
        n = n // 2
        answer += n
    return answer

def count_five(n):
    answer = 0
    while n >= 5:
        n = n // 5
        answer += n
    return answer

input = sys.stdin.readline
n, m = map(int, input().split())
result = min(count_two(n) - count_two(m) - count_two(n-m), count_five(n) - count_five(m) - count_five(n-m))
print(result)
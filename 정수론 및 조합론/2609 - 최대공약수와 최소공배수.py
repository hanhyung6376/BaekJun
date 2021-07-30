import sys


def multiple(n, m):
    num = 2
    m_num = 1
    while 1:
        if num > n or num > m:
            break

        if n % num == 0 and m % num == 0:
            while 1:
                if n % num != 0 or m % num != 0:
                    break
                else:
                    m_num *= num
                    n /= num
                    m /= num
        num += 1

    return m_num, int(m_num*m*n)

n, m = map(int, sys.stdin.readline().split())

a, b = multiple(n, m)

sys.stdout.write("%s\n" % a)
sys.stdout.write("%s\n" % b)

def f(k):
    res = 1
    for i in range(1, k + 1):
        res *= i
    return res


n, m = [int(i) for i in input().split()]

print(int(f(n+m-1)/(f(m)*f(n-1))))
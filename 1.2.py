def fact(k):
    res = 1
    for i in range(1, k + 1):
        res *= i
    return res


n, m = [int(i) for i in input().split()]
p = (n - m) if n - m != 0 else 1
print(int(fact(n) / (fact(m) * fact(p))))

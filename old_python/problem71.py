LIMIT = 10**6
n = LIMIT
while n % 7:
    n -= 1
print(n//7*3-1)
a = [1, 3, 5, 6, 10]
n = len(a)
for i in range(n):
    print(a[i-1]+a[(i+1) % n], end=' ')
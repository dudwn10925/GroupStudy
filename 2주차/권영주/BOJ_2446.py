n = int(input())
for k, i in enumerate(range(n, 0, -1)):
    print(" "*k + "*"*(2*i-1))
for k, i in enumerate(range(n-2, -1, -1)):
    print(" "*i + "*"*(2*k+3))
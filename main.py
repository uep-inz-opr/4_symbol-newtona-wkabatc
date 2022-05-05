import math


nk = list(map(int, input().split()))
n = nk[0]
k = nk[1]
output = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
print(int(output))
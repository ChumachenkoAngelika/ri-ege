m = int(input())
n = int(input())

first= ((m - 1) // 2) * 2 + 1

for i in range(first, n - 1, -2):
    print(i)
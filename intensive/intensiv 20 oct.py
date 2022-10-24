a = int(input())
if (a % 7 == 0 or a % 17 == 0) and (a > 999 and a < 10000):
    print('YES')
else:
    print('NO')
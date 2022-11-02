a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if abs(b1 - b2) == abs(a1 - a2) or a1 == a2 or b1 == b2:
    print('YES')
else:
    print('NO')
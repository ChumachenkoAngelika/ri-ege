a = 0
b = 0
for i in range(54,9184):
    if i % 5 == 0:
        i += a
        i += b
        print(i)
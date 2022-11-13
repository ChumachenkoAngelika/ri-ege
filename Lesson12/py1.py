n = int(input())
fibonachi0 = 0
fibonachy1 = 1
for i in range(n):
    fibonachy1 = fibonachi0 + fibonachy1
    fibonachi0 = fibonachy1 - fibonachi0
    print(fibonachi0,end=' ')
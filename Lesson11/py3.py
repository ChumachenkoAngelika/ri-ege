n = int(input())
s = 0
for i in range(1, n):
     if n%i == 0:
         print(i)
         s = s + i
print(s)

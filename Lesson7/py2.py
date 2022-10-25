a = float(input())
b = float(input())
c = float(input())
if a == b and a == c and b == c:
    print('Равносторонний')
elif a == b or b == a:
    print('Равнобедренный')
else:
    print('Разносторонний')

print("введите количество городов")
k = int(input())

print("введите города")
a = []
for i in range(0, k):
    a.append(input())

b = set(a)
print("введите НОВЫЙ город")
s2 = input()

if b.intersection(s2) == 0:
    print("OK")
else:
    print("REPEAT")


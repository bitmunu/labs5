print("введите два множества")
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

if (b.issubset(a) == 1 and b != a) or (a.issubset(b) == 1 and b != a):
    print("true")
else:
    print("false")
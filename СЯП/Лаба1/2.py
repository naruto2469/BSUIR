a = input("Введите строку: ")
a = a.lower().split()
i = 0
while i < len(a):
  if a[i].endswith('а'):
    del a[i]
    continue
  i += 1
print(*a)
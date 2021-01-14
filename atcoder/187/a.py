i = input().split(" ")
a, b = i[0], i[1]
# A, B = input().split()
sa = int(a[0])+int(a[1])+int(a[2])
sb = int(b[0])+int(b[1])+int(b[2])
print(max([sa, sb]))

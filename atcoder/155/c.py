N = int(input())
D = dict()
for i in range(N):
    INPUT = input()
    if INPUT in D:
        D[INPUT] += 1
    else:
        D[INPUT] = 1
MAX = max(D.values())
A = list()
for i in D:
    if D[i] == MAX:
        A.append(i)
for i in sorted(A):
    print(i)

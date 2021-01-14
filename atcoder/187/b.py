from itertools import combinations
times = input()
l = [input().split(" ") for i in range(int(times))]
l = list(combinations(l, 2))
result = 0
for i in l:
    x = [int(i[0][0]), int(i[1][0])]
    y = [int(i[0][1]), int(i[1][1])]
    dx = max(x) - min(x)
    dy = max(y) - min(y)
    slope = dy/dx
    if slope >= -1 and slope <= 1:
        result += 1
print(result)

# 解説
# N = int(input())
# A = [tuple(map(int, input().split())) for i in range(N)]
# ans = 0
# for i in range(N):
#     for j in range(i):
#         if abs(A[i][1] - A[j][1]) <= abs(A[i][0] - A[j][0]):
#             ans += 1
# print(ans)

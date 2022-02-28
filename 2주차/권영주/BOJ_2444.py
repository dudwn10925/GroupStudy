# 방법 1
# n = int(input())
# for i in range(2*n-1):
#     if i < n:
#         print(" "*(n-i-1) + "*"*(2*i+1))
#     else:
#         print(" "*(i-n+1) + "*"*(2*n-((i-n+1)*2+1)))

# 방법 2 - 출력 형식이 잘못되었습니다, vscode에선 정상 작동
# n = int(input())
# A = 2*n-1
# star = 1
# for i in range(A):
#     print(f"{'*'*star:^{A}}")
#     star = star+2 if i < n-1 else star-2

n = int(input())
A = 2*n-1
star, gap = 1, n-1
for i in range(A):
    print(" "*gap + "*"*star)
    star = star+2 if i < n-1 else star-2
    gap = gap-1 if i < n-1 else gap+1
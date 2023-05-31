import sys

n, k = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0] * 10001
dp[0] = 1

# 반복문을 통해 코인을 확인
for i in coin:
    # 반복문을 통해 코인으로 1원부터 k원까지 만들 수 있는 경우의 수를 확인
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]

print(dp[k])
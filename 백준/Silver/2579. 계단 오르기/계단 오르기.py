import sys

input = sys.stdin.readline

# 계단의 개수 입력
n = int(input())

# 계단의 숫자를 초기화합니다. 1층은 1번째(not 0번째) 인덱스에 저장합니다.
stairs = [0] * 301
for i in range(1, n + 1):
    stairs[i] = int(input())

# dp 배열을 초기화합니다.
dp = [0] * 301
dp[1] = stairs[1]  # 1층까지의 최댓값은 1층의 값과 같습니다.
dp[2] = stairs[1] + stairs[2]  # 2층까지의 최댓값은 1층과 2층을 모두 밟은 값입니다.
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])  # 3층까지의 최댓값은 1층-3층 중 최선의 선택입니다.

# 점화식을 계산합니다.
for i in range(4, n + 1):
    # i층까지의 최댓값은 (i-3층을 밟고 올라오는 경우 or i-2층을 밟고 올라오는 경우) 중 최선의 선택입니다.
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

# 결과 출력
print(dp[n])

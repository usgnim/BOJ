# 사용자로부터 정수 n을 입력받음
n = int(input())

# 사용자로부터 공백으로 구분된 정수들을 입력받아 리스트 data에 저장
data = list(map(int, input().split()))

# 소수의 개수를 저장하는 변수 count를 초기화
count = 0

# data 리스트에 있는 각 정수 x에 대해 반복
for x in data:
  # 2부터 x까지의 각 숫자 i로 나누어보며 확인
  for i in range(2, x+1):
    # x를 i로 나눴을 때 나머지가 0이면 (즉, i가 x의 약수이면)
    if x % i == 0:
      # 만약 x와 i가 같다면 (즉, x 자체가 소수인 경우)
      if x == i:
        # 소수이므로 count를 1 증가
        count += 1
      
      # 루프를 탈출하여 다음 숫자로 넘어감
      break

# 소수의 개수를 출력
print(count)
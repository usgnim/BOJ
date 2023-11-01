import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,r = map(int,input().split())  # n: 노드의 개수, m: 간선의 최대 길이, r: 길의 개수

items = [-1] + list(map(int,input().split()))  # 각 노드에 아이템의 가치를 나타내는 리스트

distance = [[INF for i in range(n + 1)] for j in range(n + 1)]  # distance[i][j]: 노드 i에서 노드 j까지의 최단 거리

# 각 노드에서 자기 자신으로 가는 거리는 0으로 초기화
for i in range(1,n+1):
    distance[i][i] = 0

# 간선 정보를 입력받아 distance 행렬 업데이트
for i in range(r):
    a,b,l = map(int,input().split())
    distance[a][b] = l
    distance[b][a] = l

# Floyd-Warshall 알고리즘을 이용하여 최단 거리 갱신
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if distance[j][k] > distance[j][i] + distance[i][k]:
                distance[j][k] = distance[j][i] + distance[i][k]

result = 0

# 각 노드에서 아이템을 수집하며 얻을 수 있는 가치 계산
for i in range(1,n + 1):
    temp = 0
    for j in range(1, n + 1):
        if distance[i][j] <= m:
            temp += items[j]
    if temp > result:
        result = temp

print(result)  # 결과 출력
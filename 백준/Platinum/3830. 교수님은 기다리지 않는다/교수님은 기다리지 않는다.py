import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 노드 x와 y를 합치고 가중치 w를 반영하여 부모 노드 및 값 갱신
def union(x, y, w):
  value[x] -= w
  parent[x] = y
  parentvalue[x] = value[y]

# x의 최상위 부모 노드를 찾아서 반환하고, 부모 노드의 값을 갱신
def findparent(x):
  if parent[x] != x:
    p, pv = parent[x], parentvalue[x]
    parent[x] = findparent(p)
    value[x] += value[p] - pv
    parentvalue[x] = value[parent[x]]
  return parent[x]

# 입력을 계속 받아서 처리하는 반복문
while 1:
  N, M = map(int, input().split())
  if not N:
    break
  
  # 각 노드의 부모, 현재 노드의 값, 부모 노드의 값 초기화
  parent = [i for i in range(N + 1)]
  value = [0] * (N + 1)
  parentvalue = [0] * (N + 1)
  
  # 간선 정보를 처리하는 반복문
  for _ in range(M):
    Q = input().split()
    if Q[0] == "?":
      # ? 쿼리일 경우 값을 출력하거나 "UNKNOWN" 출력
      a, b = map(int, Q[1:])
      print(value[b] - value[a] if findparent(a) == findparent(b) else "UNKNOWN")
    else:
      # 간선 추가일 경우 두 노드를 합치고 가중치를 반영하여 값을 갱신
      a, b, w = map(int, Q[1:])
      if findparent(a) != findparent(b):
        union(parent[a], parent[b], w - value[b] + value[a])
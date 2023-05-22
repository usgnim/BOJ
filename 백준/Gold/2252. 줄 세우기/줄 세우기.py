from collections import deque
import sys
input = sys.stdin.readline

#입력을 받으면서 인접 리스트를 만든다.
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

#앞에 몇명이 있는지 front 리스트에 기록한다.
front = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    front[b] += 1

#q에 앞에 있어야 할 사람이 0인 사람들을 append하고, q가 빌 때까지 반복한다.
def answer():
    result = []
    q = deque()
    for k in range(1, len(front)):
        if front[k] == 0:
            q.append(k)
    while q:
        now = q.popleft()
        result.append(now)
        for nnow in arr[now]:
            front[nnow] -= 1
            if front[nnow] == 0:
                q.append(nnow)
    print(*result)


answer()
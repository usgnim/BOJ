from collections import deque

# 입력 받기
n = int(input())  # n을 입력받음

graph = []  # 빈 리스트 graph 생성
for _ in range(n):
    graph.append(list(map(int, input().split())))  # n개의 줄에 대해, 각 줄을 공백 기준으로 나누어서 정수로 변환하여 리스트에 추가

m = 0  # m 초기값 설정
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:  # 만약 graph[i][j]가 9라면
            x, y = i, j  # x, y에 i, j 값을 할당
        elif graph[i][j]:  # 그렇지 않고, graph[i][j]가 0이 아니라면
            m += 1  # m을 1 증가시킴

size = 2  # size 초기값 설정
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]  # dx, dy에 각각의 이동 방향을 나타내는 리스트 할당

def bfs(x, y, visited):
    
    visited[x][y] = 1  # 시작 지점을 방문했음을 표시
    queue = deque()  # 빈 큐 생성
    queue.append((x, y, 0))  # 시작 지점을 큐에 추가, 거리는 0으로 초기화
    temp = 0  # temp 초기값 설정
    selected = (n, n, -1)  # selected 초기값 설정
    
    while queue:  # 큐가 비어있지 않은 동안 반복
        x, y, s = queue.popleft()  # 큐에서 좌표와 거리를 꺼냄
        
        if temp != s and selected[-1] != -1:  # temp와 s가 다르고, selected의 마지막 값이 -1이 아니라면
            return selected  # 선택된 좌표와 거리를 반환
        
        for i in range(4):  # 상하좌우 네 방향에 대해 반복
            nx, ny = x + dx[i], y + dy[i]  # 새로운 좌표 계산
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] or graph[nx][ny] > size:
                continue  # 만약 새로운 좌표가 범위를 벗어나거나 이미 방문한 곳이거나 물고기 크기가 현재 크기보다 크다면 무시
            
            if graph[nx][ny] and graph[nx][ny] < size:  # 만약 새로운 좌표에 물고기가 있고, 그 크기가 현재 크기보다 작다면
                selected = min(selected, (nx, ny, s+1))  # selected를 갱신하여 최소값으로 설정
                
            visited[nx][ny] = 1  # 새로운 좌표를 방문했음을 표시
            queue.append((nx, ny, s+1))  # 새로운 좌표와 거리를 큐에 추가
        temp = s  # temp를 현재 거리로 갱신
        
    return (-1, -1, -1)  # 만약 선택된 좌표가 없다면 (-1, -1, -1) 반환

result, count = 0, 0  # result와 count 초기값 설정
graph[x][y] = 0  # 시작 지점의 물고기 크기를 0으로 업데이트

while 1:  # 무한 루프
    visited = [[0]*n for _ in range(n)]  # visited 리스트 초기화
    x, y, s = bfs(x, y, visited)  # BFS 함수 호출하여 선택된 좌표와 거리를 반환
    
    if s == -1:  # 만약 선택된 좌표가 없다면
        break  # 반복문 종료
    
    graph[x][y] = 0  # 선택된 좌표의 물고기 크기를 0으로 업데이트
    result += s  # 결과값에 거리를 더함
    count += 1  # count를 1 증가시킴
    
    if count == size:  # 만약 count가 현재 크기와 같다면
        size += 1  # 크기를 1 증가시키고
        count = 0  # count를 0으로 초기화
        
print(result)  # 결과값 출력
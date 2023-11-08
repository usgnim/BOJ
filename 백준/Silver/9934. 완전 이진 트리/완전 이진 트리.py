import sys
input = sys.stdin.readline

K = int(input())  # 정수 K를 입력 받음
_input = list(map(int, input().split()))  # K개의 정수를 입력받아 리스트로 저장
tree = [[] for _ in range(K)]  # K개의 빈 리스트를 원소로 가지는 리스트 'tree' 생성

def makeTree(arr, x):
    mid = (len(arr)//2)  # 현재 리스트의 중간 지점 인덱스 계산
    tree[x].append(arr[mid])  # 현재 노드에 중간 값 추가
    
    if len(arr) == 1:  # 현재 리스트의 길이가 1이라면 (리스트에 원소가 하나만 있는 경우)
        return  # 재귀 종료
    
    makeTree(arr[:mid], x+1)  # 왼쪽 서브트리를 만들기 위해 왼쪽 부분 리스트를 재귀 호출
    makeTree(arr[mid+1:], x+1)  # 오른쪽 서브트리를 만들기 위해 오른쪽 부분 리스트를 재귀 호출

makeTree(_input, 0)  # makeTree 함수 호출하여 트리 생성
for i in range(K):  # 생성된 트리를 출력
    print(*tree[i])
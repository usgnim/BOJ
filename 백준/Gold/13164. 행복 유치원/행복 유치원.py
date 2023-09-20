N,K = map(int, input().split())
h = list(map(int, input().split()))
 
arr = []
 
for i in range(N-1):
    a = h[i+1] - h[i]
    arr.append(a)
 
arr.sort()
cost_result = 0
 
for i in range(N-K):
    cost_result += arr[i]
 
print(cost_result)

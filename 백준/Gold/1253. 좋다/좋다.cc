#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int n = 0, ans = 0;
    cin >> n;
    vector<int> v(n);
    
    for(int i=0; i<n; i++) cin >> v[i];
    // 백터에 n개의 숫자를 입력받고 오름차순으로 정렬해준다.
    sort(v.begin(),v.end()); 
    
    // n개의 숫자만큼 for문을 돌린다.
    for(int i=0; i<n; i++){
        int l=0, r=n-1; // l=0, r=n-1로 초기값을 두고 시작한다.
        
        // l<r의 조건일때까지만 while문을 돌린다
        while(l<r){
            // 만약 l==i이거나 r==i일 경우, 서로 다른 두 숫자의 합으로 나타낼 때, i번째 숫자는 포함시켜선 안된다는 규칙을 지키지 못한다.
            // l==i일 경우 l++을 하고, r==i일 경우 r--를 한다.
            if(l==i){l++; continue;}
            if(r==i){r--;continue;}
            
            // 만약 v[i] > v[l]+v[r]일 경우, l++을 한다.
            if(v[i]>v[l]+v[r]) l++;
            
            // v[i] == v[l]+v[r]일 경우 정답을 찾았으니 ans를 +1하고 break한다.
            else if(v[i]==v[l]+v[r]){
                ans++;
                break;
            }
            else r--; // v[i] < v[l] + v[r]일 경우, r--을 한다.
        }
    }
    cout << ans << "\n"; // 최종적으로 정답을 출력한다.
    return 0;
}
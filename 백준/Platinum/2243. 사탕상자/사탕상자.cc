#include <iostream>
using namespace std;
const int MAXN = 1000001;

int n;
int tree[MAXN * 4];

// 쿼리합 갱신
void update(int index, int target, int diff, int start, int end) {
	if (target < start || target > end)
		return;
	tree[index] += diff;
	if (start == end)
		return;
	int mid = (start + end) / 2;
	update(index * 2, target, diff, start, mid);
	update(index * 2 + 1, target, diff, mid + 1, end);
}

// 순위 얻는 쿼리
int query(int index, int target, int start, int end) {
	if (start == end)
		return start;
	int mid = (start + end) / 2;
	if (target <= tree[index * 2])
		return query(index * 2, target, start, mid);
	else
		return query(index * 2 + 1, target - tree[index*2], mid + 1, end);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n;
	while (n--) {
		int a, b, c;
		cin >> a;
        
		// B순위 사탕을 꺼내는 경우
		if (a == 1) {
			cin >> b;
			int favor = query(1, b, 1, MAXN);
			cout << favor << '\n';
			update(1, favor, -1, 1, MAXN);
		}
        
		// B맛의 C개의 사탕을 넣는 경우(음수인경우는 뺀다)
		else {
			cin >> b >> c;
			update(1, b, c, 1, MAXN);
		}
	}
	return 0;
}
#include <stdio.h>

int arr[20][2];
int n;
int ans = 0; // 답
int maxx = 0;

void dfs(int num)
{
    if ((num + arr[num][0] - 1) >= n)
        return;
    else
    {
        maxx += arr[num][1];
        if (maxx > ans)
            ans = maxx;
        for (int i = num + arr[num][0]; i < n; i++)
            dfs(i);
        maxx -= arr[num][1]; // for문이 끝나면 전으로 돌아가기 위해 자기자신 수익을 빼줌.
    }
}

int main()
{
    int ti, pi;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d %d", &ti, &pi);
        arr[i][0] = ti;
        arr[i][1] = pi;
    }

    for (int i = 0; i < n; i++)
        dfs(i); // 처음 시작을 달리하여 dfs 돔.
    printf("%d", ans);
    return 0;
}
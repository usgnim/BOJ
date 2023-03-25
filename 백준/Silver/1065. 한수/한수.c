#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int Han(int n) // 한수 함수 정의
{
	int i, cnt = 0, hund, ten, one;
	if (n < 100)  // 입력 값 n이 100보다 작을 경우, n 그대로 출력
		return n;
	else
	{
		// 입력 값 n이 100보다 클 경우 이므로 i의 초기값은 100, n보다 작거나 같을 때까지
		// i에 1씩 더하며 반복한다.
		for (i = 100; i <= n; i++)
		{
			hund = i / 100;
			ten = (i % 100) / 10;
			one = (i % 100) % 10;
			// (백의 자리수의 숫자 - 십의 자리수의 숫자) = (십의 자리수의 숫자 - 일의자리 숫자)
			// 위 식이 성립된다면 count에 1씩 더함
			if ((hund - ten) == (ten - one))
				cnt++;
		}
		// 100 이전에 한수는 99까지 99개 이므로 99에 count 값을 더해준다.
		return (99 + cnt); 
	}
}

int main(void)
{
	int input, result;

	scanf("%d", &input);
	result = Han(input);
	printf("%d", result);
    
    return 0;
}
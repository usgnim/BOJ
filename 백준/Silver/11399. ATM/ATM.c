#define _CRT_SECURE_NO_WARNINGS 
#include<stdio.h>

int main()
{
	int People = 0;
	int time[1000] = { 0, };
	int swap = 0;
	int Sum = 0;
	scanf("%d", &People);

	for (int i = 0; i < People; i++)
	{
		scanf("%d", &time[i]);
	}

	// 정렬해주는 부분
	for (int j = 0; j < People; j++)
	{
		for (int i = 0; i < People-1; i++)
		{
			if (time[i] > time[i + 1])
			{
				swap = time[i];
				time[i] = time[i + 1];
				time[i + 1] = swap;
			}
		}
	}

	// 앞으로 나아가며 합산
	for (int i = 0; i < People; i++)
	{
		for (int j = 0; j <= i; j++)
		{
			Sum = Sum + time[j];
		}
		if(i == People-1)
			printf("%d", Sum);
	}
}
//day3(이중 포인터)
#include <stdio.h>

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int num[4];

void find_max(int** a, int** max_n) 
{
	if (**a > **max_n)
		*max_n = *a;
}


int main()
{
	int* ptr = &num[0];
	int** max_n = &ptr; 


	for (int i = 0; i < 4; ++i)
		scanf("%d", &num[i]);


	for (int i = 1; i < 4; ++i)
	{
		int* val = &num[i];
		find_max(&val, &ptr);
	}


	printf("최대 값 : %d", **max_n);
}

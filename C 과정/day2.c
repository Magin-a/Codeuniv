//day2
#include <stdio.h>

// int main(void)
// {
//     int array[3][4]=
//     {
//         {1, 2, 3, 4},
//         {5, 6, 7, 8,},
//         {9, 10, 11, 12},
//     };

//         for (int i = 0; i < 3; i++)
//     {
//         for (int j = 0; j < 4; j++)
//         {
//             printf("%d.", array[i][j]);
//         }
//         printf("\n");
//     }
//     return 0;
// }

int arr[4][4];


void main()
{
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			scanf("%d", &arr[i][j]);
	
	printf("[변경 전]\n");
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			printf("%d ", arr[i][j]);
		}
		printf("\n");
	}
		
	printf("[변경 후]\n");
	for (int j = 0; j < 4; j++)
	{
		for (int i = 0; i < 4; i++)
		{
			printf("%d ", arr[i][j]);
		}
		printf("\n");
	}
}


#define _CRT_SECURE_NO_WARNING
#include<stdio.h>


int main(void) {
	int arr[4][4];
	int rowLen, colLen;


	rowLen = sizeof(arr) / sizeof(arr[0]);
	colLen = sizeof(arr[0]) / sizeof(arr[0][0]);




	for (int i = 0; i < rowLen; i++) {  // 행
		for (int j = 0; j < colLen; j++) {  //열
			scanf("%d", &arr[i][j]);
		}
	}
	printf("\n");


	printf("[변경 전]\n");
	for (int i = 0; i < rowLen; i++) {  // 변경 전출력
		for (int j = 0; j < colLen; j++) {  
			printf("%3d", arr[i][j]);
		}
		printf("\n");
	}
	printf("\n");


	printf("[변경 후]\n");
	for (int i = 0; i < rowLen; i++) {  // 변경 후 출력
		for (int j = 0; j < colLen; j++) {
			printf("%3d ", arr[j][i]);
		}
		printf("\n");
	}
}


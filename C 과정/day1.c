//day2
#define _CRT_SECURE_NO_WARNINGS   
#include <stdio.h>

typedef struct _Person {
	char name[10];
	int age;
	int year;
	int math;
	int eng;
	int kor;
	int sum;
	int avg;


}Person;


int main(void) {
	Person person;
	
	printf("[학생 정보]\n");
	printf("이름:");
	scanf("%s", person.name);
	printf("나이:");
	scanf("%d", &person.age);
	printf("학년:");
	scanf("%d", &person.year);
	printf("수학:");
	scanf("%d", &person.math);
	printf("영어:");
	scanf("%d", &person.eng);
	printf("국어:");
	scanf("%d", &person.kor);
	
	person.sum = (person.math + person.eng + person.kor);
	person.avg = person.sum / 3;


	printf("평균 점수: %d\n", person.avg);


	return 0;
}

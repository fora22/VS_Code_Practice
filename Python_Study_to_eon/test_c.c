#include<stdio.h>

int a = 31;

int print_number(int num)
{
    int number = num;
    return number;
}

int main(void)
{
    int number = 3;
    print_number(number);
    int n;
    scanf("%d", &n);
    int* point = (int *)malloc(sizeof(int) * n);

    return 0;
}
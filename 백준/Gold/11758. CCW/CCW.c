#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

// ccw 알고리즘
int ccw(int x1, int y1, int x2, int y2, int x3, int y3) {
    int temp = x1*y2+x2*y3+x3*y1;
    temp = temp - y1*x2-y2*x3-y3*x1;
    if (temp > 0) {
        return 1;
    } else if (temp < 0) {
        return -1;
    } else {
        return 0;
    }
}

int main(){
    int a,b,a1,b1,a2,b2;
    scanf("%d %d",&a,&b);
    scanf("%d %d",&a1,&b1);
    scanf("%d %d",&a2,&b2);
    printf("%d",ccw(a,b,a1,b1,a2,b2));
}
#include <stdio.h>
#include <stdlib.h>
#include "new_2x2.h"
#include <math.h>

#define N 8

int fpow(int a , int b){
    int i;
    int n=1;
    for (i=0;i<b;i++) 
        n*=a;
    return n;
}

void assign_value(int * array, int i)
{
    int n,j;
    n=i;
    for(j=0;j<N;j++) {
        array[j]=n%N;
        n/=N;
    }
    return ;
}

void print_out(int * array) {
    int j;
    int a0;
    a0=array[0];
    for(j=0;j<N;j++) {
        printf("%d\t",array[j]-a0>=0?array[j]-a0:array[j]+N-a0);
    }
    printf("\n");
    return ;
}
   
int right(int * array )  {
    int i,j;
    for(i=0;i<N;i++) {
        for(j=0;j<i;j++) {
            if(array[i]==array[j])
                return 0;
        }
    }
    return 1;
} 


int main()
{
    int MAX;
    int i,j;
    int array[8];
    int n;
    
    MAX=fpow(8,8);
    for(i=0;i<MAX;i++){
        assign_value(array,i);
        if (right(array))
            print_out(array);
    }

    return;
}

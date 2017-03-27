#include <stdio.h>
#include <stdlib.h>

#define  PATH_L 100
#define  CUBE_L 24
#define  PATH_STOP 65535

int L_value = 11;
int cube[CUBE_L]={0};

void four_swap(int* a , int * tu ,int r) {
    int tmp;
    if ( r ) {
        tmp=a[tu[0]];
        a[tu[0]]=a[tu[1]];
        a[tu[1]]=a[tu[2]];
        a[tu[2]]=a[tu[3]];
        a[tu[3]]=tmp;
    }
    else {
        tmp=a[tu[0]];
        a[tu[0]]=a[tu[3]];
        a[tu[3]]=a[tu[2]];
        a[tu[2]]=a[tu[1]];
        a[tu[1]]=tmp;
    }
}

void four_swap_2(int * a , int * tu , int r ) {
    int tmp;
    tmp=a[tu[0]];
    a[tu[0]]=a[tu[2]];
    a[tu[2]]=tmp;
    tmp=a[tu[1]];
    a[tu[1]]=a[tu[3]];
    a[tu[3]]=tmp;
}

void R(int * a, int r) {
    int b1[4]={8,9,11,10};
    int b2[4]={1,7,19,15};
    int b3[4]={5,17,13,3};
    four_swap(a,b1,r);
    four_swap(a,b2,r);
    four_swap(a,b3,r);
}

void R2(int * a, int r) {
    int b1[4]={8,9,11,10};
    int b2[4]={1,7,19,15};
    int b3[4]={5,17,13,3};
    four_swap_2(a,b1,r);
    four_swap_2(a,b2,r);
    four_swap_2(a,b3,r);
}

void U(int * a, int r ) {
    int b1[4]={5,4,6,7};
    int b2[4]={1,20,16,9};
    int b3[4]={0,21,17,8};
    four_swap(a,b1,r);
    four_swap(a,b2,r);
    four_swap(a,b3,r);
}

void U2(int * a, int r ) {
    int b1[4]={5,4,6,7};
    int b2[4]={1,20,16,9};
    int b3[4]={0,21,17,8};
    four_swap_2(a,b1,r);
    four_swap_2(a,b2,r);
    four_swap_2(a,b3,r);
}
        
void F(int * a, int r ) {
    int b1[4]={0,1,3,2};
    int b2[4]={5,10,14,20};
    int b3[4]={4,8,15,22};
    four_swap(a,b1,r);
    four_swap(a,b2,r);
    four_swap(a,b3,r);
}

void F2(int * a, int r ) {
    int b1[4]={0,1,3,2};
    int b2[4]={5,10,14,20};
    int b3[4]={4,8,15,22};
    four_swap_2(a,b1,r);
    four_swap_2(a,b2,r);
    four_swap_2(a,b3,r);
}

void R_r(int * a ,int r) {
    R(a,1);
}

void U_r(int * a ,int r) {
    U(a,1);
}

void F_r(int * a ,int r) {
    F(a,1);
}

typedef void (*turn_type)(int * a, int r);
turn_type  Turn[9]={R,U,F,R_r,U_r,F_r,R2,U2,F2};
turn_type  Rev[9] ={R_r,U_r,F_r,R,U,F,R2,U2,F2};
char       TurnStr[9][3]={"R","U","F","R'","U'","F'","R2","U2","F2"};
int        Free=9;

int check(int * a){
    int i;
    for(i=0;i<6;i++){
        if(a[4*i+0]!=a[4*i+1])
            return 0;
        if(a[4*i+0]!=a[4*i+2])
            return 0;
        if(a[4*i+0]!=a[4*i+3])
            return 0;
    }
    return 1;
}

int path[PATH_L]={PATH_STOP};
int * p0;
int * pmax;
int * p ;
int run(int * cube, int last){
    int   i;
    if (check(cube)) 
        return 1;
    if (p>=pmax)
        return 0;
    for(i=0;i<Free;i++){
        if (i%3==last%3)
            continue;
        *p=i;
        p++;
        Turn[i](cube,0);
        if (run(cube,i)) 
            return 1;
        Rev[i](cube,0);
        p--;
    }
    return 0;
}

int solve(int * cube) {
    p0=path;
    int i;
    int answer;
    for(i=0;i<=L_value;i++){
        p=p0;
        pmax=p0+i;
        answer=run(cube,0);
        if (answer){
            printf("OK %d\n",i);
            fflush(stdout);
            return 1;
        }
        printf("MORE %d\n",i);
        fflush(stdout);
    }
    return 0;
}

void load_cube(int * cube, int len, char * values[]){
    int i;
    int tmpvalue;
    if (len != CUBE_L)
        exit(1);
    for(i=0;i<CUBE_L;i++){
        cube[i]=atoi(values[i+1]);
    }
    return ;
}

void printsummary() {
    printf("SEQ ");
    p=p0;
    while(1){
        if(p==pmax)
            break;
        printf("%d ",*p);
        p++;
    }
    printf("\n");
    return;
}

int main(int argc, char * argv[] ){
    int i;
    int  cube[CUBE_L];
    load_cube(cube,argc-1,argv);
    solve(cube);
    printsummary();
    return 0;
}


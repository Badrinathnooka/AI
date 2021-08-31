#include<stdio.h>
#include<stdlib.h>
void graph(int n){
	int a[8][8]={
		{1,1,0,0,1,0,0,0},
		{1,1,0,1,0,0,0,0},
		{0,0,1,1,0,0,1,0},		
		{0,0,1,1,0,0,0,0},
		{0,0,0,0,1,1,0,0},
		{0,0,0,0,1,1,0,1},
		{0,0,0,0,0,0,1,1},
		{0,0,0,0,0,0,1,1}
};	

}
int main(){
	int i,j,n;
	printf("Enter the position :");
	scanf("%d",&n);
	graph(n);
}

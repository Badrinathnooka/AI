#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
void wumpurs(int a[][10],int r,int c){
	int i=0,j=0,t;
	bool k=1;
	while(k){
		j=j+1;
		if(a[i][j]==1)
		k=0;
	}
}
void main(){
	int i,j,r,c,l,k;
	printf("Enter number of rows and columns :");
	scanf("%d %d",&r,&c);
	printf("Enter 3)Danger 4)pit 5)gold else 0");
	int a[r][c];
	for(i=0;i<r;i++){
		for(j=0;j<c;j++){
			printf("Enter %d,%d:",i,j);
			scanf("%d",&a[i][j]);
		}
	}
	for(i=0;i<r;i++){
		for(j=0;j<c;j++){
			if(a[i][j]==3){
				l = i+1;
				k = j;
				if(l<r & a[l][k]==0){
					a[l][k] = 1;
				}
				l=i-1;
				if(l>=0 & a[l][k]==0){
					a[l][k] = 1;
				}
				l=i;
				k=j+1;
				if(k<r & a[l][k]==0){
					a[l][k] = 1;
				}
				k = j-1;
				if(k>=0 & a[l][k]==0){
					a[l][k] = 1;
				}
			}
			if(a[i][j]==4){
				l = i+1;
				k = j;
				if(l<r & a[l][k]==0){
					a[l][k] = 2;
				}
				l=i-1;
				if(l>=0 & a[l][k]==0){
					a[l][k] = 2;
				}
				l=i;
				k=j+1;
				if(k<r & a[l][k]==0){
					a[l][k] = 2;
				}
				k = j-1;
				if(k>=0 & a[l][k]==0){
					a[l][k] = 2;
				}
			}
			if(a[i][j]==5){
				l = i+1;
				k = j;
				if(l<r & a[l][k]==0){
					a[l][k] = 6;
				}
				l=i-1;
				if(l>=0 & a[l][k]==0){
					a[l][k] = 6;
				}
				l=i;
				k=j+1;
				if(k<r & a[l][k]==0){
					a[l][k] = 6;
				}
				k = j-1;
				if(k>=0 & a[l][k]==0){
					a[l][k] = 6;
				}
			}
		}
	}
	wumpurs(a,r,c);
	for(i=0;i<r;i++){
		for(j=0;j<c;j++){
			printf("%d ",a[i][j]);
		}
	}
}

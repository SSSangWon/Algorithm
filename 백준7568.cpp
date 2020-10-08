#include <iostream>
#include<map>

using namespace std;

int ans(int a){

}
int main(){
    int a, rank;
    scanf("%d", &a);

    int *x = new int[a]; 
    int *y = new int[a];

    for(int i=0; i<a; i++){
        scanf("%d %d", &x[i], &y[i]);
    }

    for(int i=0; i<a; i++){
        rank=1;
        for(int j=0; j<a; j++){
            if(x[i]<x[j] && y[i]<y[j]){
                rank++;
            }
        }
        printf("%d ",rank);
    }

    return 0;
}
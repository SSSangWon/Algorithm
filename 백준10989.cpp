#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
    int n, n1;
    int arr[10001]={0,};

    scanf("%d", &n);

    for(int i=0; i<n; i++){
        scanf("%d", &n1);
        arr[n1]+=1;
    }
    for(int i=0; i<10001; i++){
        if(arr[i] != 0){
            for(int j=0; j<arr[i]; j++) printf("%d\n",i);
        }
    }
    return 0;
}
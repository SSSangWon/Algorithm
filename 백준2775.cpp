#include <iostream>

using namespace std;

int main(){
    int k, n, a;
    int arr[15][15];

    for(int i=0; i<15; i++){
        for(int j=0; j<15; j++){
            if(i==0){
                arr[i][j]=j+1;
            }else if(j==0){
                arr[i][j]=1;
            }else{
                arr[i][j]=arr[i][j-1]+arr[i-1][j];
            }
        }
    }

    cin >> a;
    for(int i=0; i<a; i++){
        cin >> k >> n;
        cout << arr[k][n-1]<<endl;
    }

    return 0;
}

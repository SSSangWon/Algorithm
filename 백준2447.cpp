#include <iostream>

using namespace std;


void star(int n){
    //if(n==3){
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(i%3==1 && j%3==1) cout << ' ';
                else cout << '*';
            }
            if(n!=(n-1))cout << '\n';
        }
   // }
}

int main(){
    int n;
    cin >> n;
    star(n);
    return 0;
}
#include <iostream>
using namespace std;

int honeycomb(int n){
    if(n==0) return 1;
    int cnt=0;
    int d=6;
    while(n>0){
        n-=d;
        d+=6;
        cnt++;
    }
    return cnt+1;

}

int main(){
    int n;
    cin >> n;
    cout << honeycomb(n-1);

}
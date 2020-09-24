#include <iostream>
using namespace std;

int a(int x){
    for(int i=0; i<x; i++){
        int sum=0;
        int ii=i;
        while(ii > 0){
            sum+=ii%10;
            ii/=10;
        }
        if(i+sum==x){
            return i;
        }

    }
    return 0;
}

int main(){
    int x;
    cin >> x;
    cout << a(x);
    return 0;
}
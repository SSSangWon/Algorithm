#include <iostream>
#include <math.h>

using namespace std;

int sp(int n){    
    int a = sqrt(n);
    if(n<2){
        return 1;
    } else if (n==2){
        return 2;
    } else if(a*a==n){
        return a+a-1;
    } else {
        if(n>(a*a+a)){
            return a+a+1;
        }else{
            return a+a;
        }
    }


}

int main(){

    int n;
    cin >> n;


    for(int i=0; i<n; i++){
        int x, y;
        cin >> x >> y;

        cout << sp(abs(y-x))<<endl; 
    }



    return 0;
}
#include <iostream>
using namespace std;

int del(int kg){
    int cnt=0;

    while(kg>0){
        if(kg%5 == 0){
            return kg/5+cnt;
        }
        else{
            kg-=3;
            cnt++;
            if(kg<0){
                return -1;
            }
        }
    }
}

int main(){
    int kg = 0;
    cin >> kg;
    cout << del(kg);
    return 0;
}
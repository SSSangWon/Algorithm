#include <iostream>

using namespace std;

int s(int a){
    int newa=0;
    while( a != 0){
        if(newa != 0){
            newa = newa*10;
        }
        newa = newa + a%10;
        a = a/10;
    }
    return newa;
}

int main(){
    int a,b;
    cin >> a;
    cin >> b;

    if(s(a)>s(b)){
        cout << s(a);
    }else if(s(a)<s(b)){
        cout << s(b);
    }


    return 0;
}
#include <iostream>

using namespace std;

int main(){
    int a,b,c,d,e,f;
    int x,y;
    cin >> a >> b >> c >> d >> e >> f;
    
    if(a==c){
        x=e;
    }else if(a==e){
        x=c;
    }else{
        x=a;
    }

    if(b==d){
        y=f;
    }else if(b==f){
        y=d;
    }else{
        y=b;
    }

    cout << x << " " << y << endl;
    

    return 0;
}
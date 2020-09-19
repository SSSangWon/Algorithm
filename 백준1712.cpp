#include <iostream>
using namespace std;

int sonic(){
    int A,B,C;
    cin >> A >> B >> C;
    if(B>=C){
        return -1;
    }
    else{
        return A/(C-B)+1;
    }
}

int main (){
    cout << sonic();
  return 0;
}
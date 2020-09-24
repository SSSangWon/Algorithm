#include <iostream>
#include<math.h>
using namespace std;
int climb(int a, int b, int v){
    if(a>=v) {
        return 1;
    }
    else if(a<=b){
        return -1;
    }
    else{
        return (v-b-1)/(a-b)+1;
    }

}



int main(){ 
    int a,b,v;
    cin >> a >> b >> v;
    cout << climb(a,b,v);
    return 0;
} 
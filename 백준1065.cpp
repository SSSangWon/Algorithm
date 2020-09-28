#include <iostream>
using namespace std;

int h(int n){
    int count=99;
    if(n<100){
        return n;
    }
    for(int i=100; i<n+1; i++){
        if((i/100)-(i/10%10) == (i/10%10)-(i%10)){
            count++;
        }
        
    }
    return count;

}

int main(){
    int n;
    cin >> n;
    cout << h(n);
    
    return 0;
}
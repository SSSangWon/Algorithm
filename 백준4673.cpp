#include <iostream>
#include <vector>
using namespace std;
int d(int n){
    int answer = n;

    while(n != 0){
        answer = answer + n%10;
        n = n/10;
    }

    return answer;
}


int main(){
    vector<int> v;

    for(int i=0; i<10001; i++){
        v.push_back(i);
    }

    for(int i=0; i<9999; i++){
        if(v[d(i)] != 0){
            v[d(i)]=0;
        }   
    }

    for(int i=0; i<10001; i++){
        if(v[i] != 0){
            cout<<i<<endl;
        }
    }

    return 0;
}
#include <iostream>

using namespace std;

void eratos(int n){
    bool* primeNum = new bool[2*n+1];
    int cnt=0;

    for(int i=0; i<2*n+1; i++){
        primeNum[i]=true;
    }

    primeNum[1]=false;

    for(int i=2; i*i<2*n+1; i++){
        if(primeNum[i]){
            for(int j=i*i; j<2*n+1; j+=i){
                primeNum[j]=false;
            }
        }
    }

    for(int i=n+1; i<2*n+1; i++){
        if(primeNum[i]==true){
            cnt++;
        }
    }
        cout << cnt << endl;

}

int main(){
    while(1){
        int n;
        cin >> n;
        if(n==0){
            break;
        } else{
            eratos(n);
        }
    }
    return 0;
}
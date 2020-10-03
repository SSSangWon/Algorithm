#include <iostream>

using namespace std;

int main(){
    bool* primeNum = new bool[10001];

    for(int i=2; i<10001; i++){
        primeNum[i]=true;
    }
    primeNum[1]=false;

    for(int i=2; i*i<10001; i++){
        if(primeNum[i]){
            for(int j=i*i; j<10001; j+=i){
                primeNum[j]=false;
            }
        }
    }

    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        int a;
        int x;
        cin >> a;

        for(int i=a/2; i<a; i++){
            bool sw=true;
            for(int j=0; j<a/2+1; j++){
                if(primeNum[i] && primeNum[j]){
                    if((j+i)==a){
                        cout << j << " " << i << endl;
                        sw=false;
                        break;
                    }
                }
            }
            if(sw==false){
                break;
            }
        }

    }
    return 0;
}
#include <iostream>

using namespace std;

int main(){
    int n, cnt=0;
    bool* eratos = new bool[1001];
    eratos[1]=false;

    for(int i=2; i<1001; i++){
        eratos[i]=true;
    }

    for(int i=2; i*i<1002; i++){
        if(eratos[i]){
            for(int j=i*i; j<1002; j+=i){
                eratos[j]=false;
            }
        }
    }

    cin >> n;
    for(int i=0; i<n; i++){
        int a;
        cin >> a;
        if(eratos[a]==1){
            cnt++;
        }
        
    }
    cout << cnt << endl;

    return 0;
}
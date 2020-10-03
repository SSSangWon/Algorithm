// #include <iostream>

// using namespace std;
// void eratos(int m, int n){
//     bool* primeNum = new bool[n+1];

//     for(int i=2; i<n+1; i++){
//         primeNum[i]=true;
//     }
//     primeNum[1]=false;

//     for(int i=2; i*i<n+1; i++){
//         if(primeNum[i]){
//             for(int j=i*i; j<n+1; j+=i){
//                 primeNum[j]=false;
//             }
//         }
//     }

//     for(int i=m; i<n+1; i++){
//         if(primeNum[i]){
//             cout<<i<<endl;
//         }
//     }
// }

// int main(){
//     int m, n;
//     cin >> m >> n;
//     eratos(m,n);
//     return 0;
// }


#include <iostream>

using namespace std;

int main(){
    int m, n;
    cin >> m >> n;
    bool* primeNum = new bool[n+1];

    for(int i=2; i<n+1; i++){
        primeNum[i]=true;
    }
    primeNum[1]=false;

    for(int i=2; i*i<n+1; i++){
        if(primeNum[i]){
            for(int j=i*i; j<n+1; j+=i){
                primeNum[j]=false;
            }
        }
    }

    for(int i=m; i<n+1; i++){
        if(primeNum[i]){
            cout<<i<<endl;
        }
    }
    return 0;
}
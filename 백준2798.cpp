#include <iostream>
#include <vector>
using namespace std;
int blackjack(int n, int m){
    int a,max=0;
    vector <int> v;
    for(int i=0; i<n; i++){
        cin >> a;
        v.push_back(a);   
    }

    for(int i=0; i<n-3; i++){
        for(int j=i+1; j<n-2; j++){
            for(int x=j+1; x<n-1; x++){
                if(v[i]+v[j]+v[x]<=m && v[i]+v[j]+v[x]>max){
                    max=v[i]+v[j]+v[x];
                }
             }
        }
    }


    return max;

}
int main(){
    int n,m;
    cin >> n >> m; 
    cout << blackjack(n,m);
    return 0;
}
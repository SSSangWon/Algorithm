#include <iostream>
#include <vector>

using namespace std;

int ans(int a){

}
int main(){
    int a,d,k;
    cin >> a;

    vector<int> v;
    vector<vector<int>> v1;
    for(int i=0; i< a; i++){
        cin >> d;
        cin >> k;
        v.push_back(d);
        v.push_back(k);
        v1.push_back(v);
    }
    cout<< v1[0][0];
    return 0;
}
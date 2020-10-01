#include <iostream>
#include <vector>

using namespace std;

int main(){
    int a, h, w, n, ab, di;
    cin >> a;
    vector<int> v;
    for(int j=0; j<a; j++){
        cin >> h >> w >> n;

        for(int i=1; ;i++){
            if(n/h == 0){
                ab = n; 
                di = i;
                break;
            }else if(n/h == 1 && n%h == 0){
                ab = h;
                di = i;
                break;
            }else{
                n = n-h;
            }
        }
        v.push_back(ab*100+di);
    }
    for(int i=0; i<v.size(); i++){
        cout << v[i] <<endl;
    }
    return 0;
}
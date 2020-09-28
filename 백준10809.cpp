#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){

    vector<int> v;
    string a;

    for(int i=0; i<26; i++){
        v.push_back(-1);
    }

    cin >> a;

    for (int i=0; i<a.length(); i++){
        
        int alpa = int(a[i]);
        
        if( v[alpa-97] == -1 ){
            v[alpa-97]=i;
        }
    }

    for (int i=0; i<26; i++ ){
        cout << v[i]<<" ";
    }

    return 0;
    
}
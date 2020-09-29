#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
    vector <int> v;
    string a;

    int max=0;
    int spot=0;

    for(int i=0; i<26; i++){
        v.push_back(0);
    }
    
    cin >> a;
    
    for(int i=0; i<a.length(); i++){
        if(int(a[i])<91){
            v[int(a[i])-65]++;
        }
        else{
            v[int(a[i])-97]++;
        }
    }

    for(int i=0; i<v.size(); i++){
        if(v[i]>max){
            max=v[i];
            spot=i;
        } else if (v[i]==max){
            spot=-1;
        }

    }
    if (spot == -1){
         cout << "?";
    }else{
        cout << char(spot+65);
    }
    return 0;
}
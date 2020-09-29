#include <iostream>
#include <string>
#include <vector>

using namespace std;

int cnt=0;

void zz(string s){

    for(int i=0; i<s.length(); i++){
        if(s[i] != s[i+1]){
            for(int j=i+1; j<s.length(); j++){
                if(s[i]==s[j]){
                    return;
                }
            }
        }

    }
    
    cnt++;
}

int main(){
    int num;
    string s;
    
    cin>>num;

    for(int i=0; i<num; i++){
        cin >> s;
        zz(s);
    }
    
    cout << cnt;


    return 0;
}
#include <iostream>
#include <string>
using namespace std;

int main(){
    int cnt=0;
    string s;
    
    cin >> s;

    for(int i=0; i<s.length(); i++){
        if(s[i]=='c'){
            if(s[i+1]=='=' || s[i+1]=='-'){
                i++;
            }
        }else if(s[i]=='d'){
            if(s[i+1]=='z' && s[i+2]=='='){
                i=i+2;
            }
            else if(s[i+1]=='-'){
                i++;
            }
        }else if(s[i]=='l'){
            if(s[i+1]=='j'){
                i++;
            }
        }else if(s[i]=='n'){
            if(s[i+1]=='j'){
                i++;
            }
        }else if(s[i]=='s'){
            if(s[i+1]=='='){
                i++;
            }
        }else if(s[i]=='z'){
            if(s[i+1]=='='){
                i++;
            }
        }
        cnt++;
    }
    cout << cnt;

    return 0;
}
#include <iostream>
#include <string>

using namespace std;

int main(){
    string str;
    bool sw=true;
    int cnt=1;

    getline(cin,str);
    
    if (int(str[0]) == 32){
        cnt=0;
    }
    

    for(int i=0; i<str.length(); i++){
        if(sw==true && int(str[i])==32){
            sw=false;
        } else if(sw==false && int(str[i])!=32){
            sw=true;
            cnt++;
        }
    }
    
    cout << cnt;
    return 0;
}
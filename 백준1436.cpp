#include <iostream>
#include <cstring>
#include <string>

using namespace std;

bool find(int n){
    string s=to_string(n);
    
    if(s.find("666") != string::npos){
        return true;
    }
    return false;
}

int result(int n){
    int cnt=1;
    int answer=666;
    while(cnt!=n){
        answer+=1;
        if(find(answer)){
            cnt+=1;
        }
    }
    return answer;
}
int main(){
    int n;
    cin >> n;
    cout << result(n);

    return 0;
}
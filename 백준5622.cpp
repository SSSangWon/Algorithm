#include <iostream>
#include <string>

using namespace std;

int main(){
    string a;
    cin >> a;

    int time=0;

    for(int i=0; i<a.length(); i++){
        if(a[i]=='A' || a[i]=='B' || a[i]=='C'){
            time = time + 3;
        }else if(a[i]=='D' || a[i]=='E' || a[i]=='F'){
            time = time + 4;
        }else if(a[i]=='G' || a[i]=='H' || a[i]=='I'){
            time = time + 5;
        }else if(a[i]=='J' || a[i]=='K' || a[i]=='L'){
            time = time + 6;
        }else if(a[i]=='M' || a[i]=='N' || a[i]=='O'){
            time = time + 7;
        }else if(a[i]=='P' || a[i]=='Q' || a[i]=='R' || a[i]=='S'){
            time = time + 8;
        }else if(a[i]=='T' || a[i]=='U' || a[i]=='V'){
            time = time + 9;
        }else if(a[i]=='W' || a[i]=='X' || a[i]=='Y' || a[i]=='Z'){
            time = time + 10;
        }
    }

    cout << time;
    return 0;
}
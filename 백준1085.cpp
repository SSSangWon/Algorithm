#include <iostream>
#include <math.h>

using namespace std;

int main(){
    int x,y,w,h, min;
    cin >> x;
    min=x;
    cin >> y;
    if(min>y) min=y;
    cin >> w;
    if(min>(abs(w-x))) min=abs(w-x);
    cin >> h;
    if(min>(abs(h-y))) min=abs(h-y);
    cout << min << endl;

    return 0;
}
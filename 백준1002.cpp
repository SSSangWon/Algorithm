#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int n;
    cin >> n;

    for(int i=0; i<n; i++){
        int x1,y1,r1,x2,y2,r2;
        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;

        double a = sqrt(pow(x2-x1,2)+pow(y2-y1,2));
        double b = r1 + r2;
        if(x1==x2 && y1==y2 && r1==r2) cout << "-1" << '\n';
        else if(a >= r1 && a >= r2){
            if(r1+r2 > a) cout <<'2' <<'\n';
            else if(r1+r2 == a) cout << '1' <<'\n';
            else cout << '0' <<'\n';
        }
        else{
            if(abs(r1-r2) < a) cout << '2' <<'\n';
            else if(abs(r1-r2) == a) cout << '1' <<'\n';
            else cout << '0' <<'\n';
        }

    }

    return 0;
}
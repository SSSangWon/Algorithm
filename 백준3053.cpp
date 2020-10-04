#include <iostream>

using namespace std;

const double pi = 3.14159265358979;

int main(){
    double R;
    cin >> R;
    cout << fixed;
    cout.precision(6);
    cout << R*R*pi <<endl;
    cout << 2.0*R*R <<endl;
    return 0;
}
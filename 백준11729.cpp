#include <iostream>
#include <cmath>

using namespace std;

void move(int from, int to){
    cout << '\n' << from <<' '<< to;
}

void hanoi(int n, int from, int by, int to){
    if(n==1) move(from, to);
    else{
        hanoi(n-1, from, to, by);
        move(from, to);
        hanoi(n-1, by, from, to);
    }

}

int main(){
    int n;
    int a, b, c;

    cin >> n;

    a = pow(2,n)-1;
    cout << a;

    hanoi(n, 1, 2, 3);

    return 0;
}
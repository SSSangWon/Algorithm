#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int n,x,y;
    vector <pair<int,int>> v;
    vector <pair<int, int>>::iterator it;

    scanf("%d", &n);

    for(int i=0; i<n; i++){
        scanf("%d %d", &x, &y);
        v.push_back(make_pair(y,x));
    }

    sort(v.begin(), v.end());

    for (it = v.begin(); it != v.end(); it++)
        printf("%d %d\n", it->second, it->first);
    return 0;
}
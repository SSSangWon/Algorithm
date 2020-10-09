#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
    int n;
    vector<int> v1;
    scanf("%d",&n);
    for(int i=0; i<n; i++){
        int n1;
        scanf("%d",&n1);
        v1.push_back(n1);
    }
    sort(v1.begin(),v1.end());
    for(int i=0; i<n; i++){
        printf("%d\n",v1[i]);
    }
    return 0;
}
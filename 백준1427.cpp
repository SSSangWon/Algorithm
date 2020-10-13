#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int n, cnt=0, ans=0, mul=1;
    scanf("%d",&n);

    int arr[11];

    for(int i=0; i<12; i++){
        arr[i]=n%10;
        n=n/10;
        cnt++;
        if(n==0) break;
    }

    sort(arr,arr+cnt);

    for(int i=0; i<cnt; i++){
        ans+=arr[i]*mul;
        mul*=10;
    }
    
    printf("%d", ans);
    return 0;
}
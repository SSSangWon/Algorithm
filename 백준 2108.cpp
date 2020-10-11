#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

bool cmp(const pair<int,int>& a, const pair<int,int>& b) {
	if (a.second == b.second) return a.first < b.first;
	return a.second < b.second;
}

int main(){
    int max,n,n1,mid,range, mode=0, sum=0, cnt=0;
    float aver;
    map <int, int> m;
    map <int, int>::iterator iter;

    scanf("%d",&n);
    for(int i=0; i<n; i++){
        scanf("%d",&n1);
        iter = m.find(n1);
        if ( iter == m.end() ) {
            m[n1]=1;
        } else {
            iter->second++;
        }

        sum+=n1;
    }

    aver = round(sum/(float)n);
    
    iter = m.begin();
    int p=n/2;
    while(1){
        p-=iter->second;
        if(p<0) break;
        iter++;
    }
    mid = iter->first;
    
    iter = --m.end();
    range = iter->first - m.begin()->first;


    vector<pair<int,int>> vec( m.begin(), m.end());
    vector<pair<int,int>>::iterator it;
	sort(vec.begin(), vec.end(), cmp);
    
    it=--vec.end();
    max = it->second;
	
    for (it=vec.begin(); it!=vec.end(); ++it) {
      
        if(it->second == max && cnt<2) {

            mode = it->first;
            cnt++;
        }
	}

    printf("%0.f\n", aver);
    printf("%d\n", mid);
    printf("%d\n", mode);
    printf("%d\n", range);

    return 0;
}
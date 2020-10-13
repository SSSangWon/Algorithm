#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool cmp(const string &a, const string &b){
    if(a.size() == b.size()) return a<b;
    return a.size() < b.size();
}

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    string s;
    vector <string> v;
    
    cin >> n;

    for(int i=0; i<n; i++){
        cin >> s;
        v.push_back(s);
    }
    
    sort(v.begin(), v.end(), cmp);

    for(int i=0; i<n; i++){
        if(v[i]== v[i+1]) continue;
        cout << v[i] << '\n';
    }
    return 0;
}
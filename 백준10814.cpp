#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

bool cmp(const pair<int,string> &a, const pair<int,string> &b) {
	return a.first < b.first;
}


int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, age;
    string name;

    vector <pair<int, string>> v;
    vector <pair<int, string>>::iterator it;

    cin >> n;

    for(int i=0; i<n; i++){
        cin >> age >> name;
        v.push_back(make_pair(age, name));
    }

    stable_sort(v.begin(), v.end(), cmp);
    
    for (it = v.begin(); it != v.end(); it++)
        cout << it->first << " " << it->second << '\n';

    return 0;
}
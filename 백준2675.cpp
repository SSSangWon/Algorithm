#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
    int num, sNum;
    string s;
    vector<int> vi;
    vector<string> vs;
    
    cin >> num;
    for(int i=0; i<num; i++){
        cin >> sNum >> s;
        vi.push_back(sNum);
        vs.push_back(s);
    }
    for(int i=0; i<num; i++){
        for(int j=0; j<vs[i].length(); j++){
            for(int x=0; x<vi[i]; x++){
                cout << vs[i][j];
            }
        }
        cout<<endl;
    }

    return 0;
}
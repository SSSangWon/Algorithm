#include <iostream>

using namespace std;

int main(){
    int bz,bm,num,max=0;

    cin >> num;

    for(int i=1; i<num+1; i++){
        max = max+i;
        if(max >= num){
            if(i%2 == 0){
                bz=i-(max-num);
                bm=1+(max-num);
                cout << bz << "/" << bm;
                break;
            }
            else{
                bz=1+(max-num);
                bm=i-(max-num);
                cout << bz << "/" << bm;
                break;
            }
        }
    }

    return 0;
}
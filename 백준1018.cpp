#include <iostream>

using namespace std;

int main(){
    int x, y, cnt, min=2500;
    char chess[8][8]=
    {
        {'B','W','B','W','B','W','B','W'},
        {'W','B','W','B','W','B','W','B'},
        {'B','W','B','W','B','W','B','W'},
        {'W','B','W','B','W','B','W','B'},
        {'B','W','B','W','B','W','B','W'},
        {'W','B','W','B','W','B','W','B'},
        {'B','W','B','W','B','W','B','W'},
        {'W','B','W','B','W','B','W','B'}
    };

    scanf("%d %d", &x, &y);
    //char board[50][50];

    char **board = new char*[x];
    for(int i=0; i<x; ++i) board[i]=new char[y];

    for(int i=0; i<x; i++){
        for(int j=0; j<y; j++){
            scanf(" %c", &board[i][j]);
        }
    }

    for(int i=0; i<x-7; i++){
        for(int j=0; j<y-7; j++){
            cnt=0;
            for(int n=0; n<8; n++){
                for(int m=0; m<8; m++){
                    if(board[i+n][j+m] == chess[n][m]){
                        cnt++;
                    }
                }
            }
            cnt = 64-cnt > cnt ? cnt : 64-cnt;
            if(cnt < min) min = cnt; 

        }
    }
    cout << min;
    return 0;

}
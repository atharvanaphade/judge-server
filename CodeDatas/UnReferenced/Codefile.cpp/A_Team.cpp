#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int tc, p, v, t, ret = 0;
    cin >> tc;
    while(tc--){
        cin >> p >> v >> t;
        if(p + v + t >= 2){
            ret += 1;
        }
    }
    cout << ret << endl;
}
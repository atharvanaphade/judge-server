#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int tc;
    cin >> tc;
    while(tc--){
        string a, b;
        cin >> a >> b;
        int common = 0;
        for(int i = 0; i < a.length(); i++){
            for(int j = 0; j < b.length(); j++){
                int p = i, q = j, temp = 0;
                while(p < a.length() and q < b.length() and a[p] == b[q]){
                    temp++;
                    p++;
                    q++;
                }
                common = max(common, temp);
            }
        }
        cout << a.length() + b.length() - 2 * common << endl;
    }
}
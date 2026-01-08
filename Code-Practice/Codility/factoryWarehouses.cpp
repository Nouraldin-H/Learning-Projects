// What comes to mind: declaring ans as array.

// you can use includes, for example:
#include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

vector<int> solution(vector<int>& puts) {
    vector<int> ans(puts.size()); // this part i hate
    for (int i = 0; i < puts.size(); i++) {
        if (puts[i] > 0) ans[i] = -1;
        if (puts[i] == 0) ans[i] = i;
    }
    return ans;
}
// what comes to mind: get all numbers in array/vector and append.

// you can use includes, for example:
#include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

string solution(vector<int> &nums) {
    string str = "";
    for (auto num : nums) {
        for (int i = 0; i < nums.size(); i++) {
            cout << "nums[num] < nums[num+1]: " << (bool)(nums[i] < nums[i+1]) << endl;
            if (nums[i] < nums[i+1]) {
                sort(nums.begin(), nums.begin() + 1);
            }
        }
        str.append(to_string(num));
        cout << "new str: " << str << endl;
    }
    cout << str << endl;
    return str;
}
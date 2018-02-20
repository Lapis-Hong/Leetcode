//
// Created by Lapis-Hong  on 2018/2/20.
//
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    // First, reverse the whole string, then reverse each word.
    void reverseWords(string &s) {
        reverse(s.begin(), s.end());  //  C++ std::reverse() reverses the order of the elements in the range [first, last), begin()函数返回一个迭代器,指向字符串的第一个元素.
        int storeIndex = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] != ' ') {
                if (storeIndex != 0) s[storeIndex++] = ' ';
                int j = i;
                while (j < s.size() && s[j] != ' ') { s[storeIndex++] = s[j++]; }
                reverse(s.begin() + storeIndex - (j - i), s.begin() + storeIndex);
                i = j;
            }
        }
        s.erase(s.begin() + storeIndex, s.end());  // delete

    }
};

int main() {
    string s = " I love  you";
    Solution solution;
    solution.reverseWords(s);
    cout << s << endl;
}
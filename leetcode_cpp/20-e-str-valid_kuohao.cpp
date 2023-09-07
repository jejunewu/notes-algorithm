/**
20. 有效的括号
提示
简单
4.1K
相关企业
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。


示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false


提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成

*/

//
// Created by junjie on 9/7/23.
//
#include "iostream"
#include "vector"
#include "tuple"
#include "string"
#include "stack"

using namespace std;

class Solution {
public:
    /**
     * 用栈方法
     * @param s
     * @return
     */
    bool isValid(string s) {
        stack<char> stk;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') stk.push(')');
            else if (s[i] == '[') stk.push(']');
            else if (s[i] == '{') stk.push('}');
            else if (stk.empty() || s[i] != stk.top()) return false;
            else stk.pop();
        }
        return stk.empty();
    }
};


int main() {
    Solution sol;
    std::vector<std::tuple<std::string, bool>> examples = {
            {"()",     true},
            {"()[]{}", true},
            {"(]",     false}
    };
    cout << "----------------------------------------" << endl;
    cout << "  ExampleID || PASS || MyRes || Label   " << endl;
    cout << "----------------------------------------" << endl;
    for (size_t i = 0; i < examples.size(); i++) {

        // 获得参数
        std::string arg1 = std::get<0>(examples[i]);
        bool label = std::get<1>(examples[i]);

        //调用
        bool my_res = sol.isValid(arg1);
        std::cout << to_string(i) + " || " + to_string(my_res == label) + " || " + to_string(my_res) + " || " +
                     to_string(label) << endl;

    }
    cout << "----------------------------------------" << endl;

}


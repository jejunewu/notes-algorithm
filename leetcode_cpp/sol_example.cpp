//
// Created by junjie on 9/7/23.
//
#include "iostream"
#include "vector"
#include "tuple"
#include "string"

using namespace std;

class Solution {
public:
    string func(int arg1, string agr2) {
        string result = std::to_string(arg1) + agr2;
        return result;
    }
};


int main() {
    Solution sol;
    std::vector<std::tuple<int, std::string, std::string>> examples = {
            {1, "aa", "1aa"},
            {2, "bb", "1aa"}
    };
    cout << "----------------------------------------" << endl;
    cout << "  ExampleID || PASS || MyRes || Label   " << endl;
    cout << "----------------------------------------" << endl;
    for (size_t i = 0; i < examples.size(); i++) {

        // 获得参数
        int arg1 = std::get<0>(examples[i]);
        std::string arg2 = std::get<1>(examples[i]);
        string label = std::get<2>(examples[i]);

        //调用
        string my_res = sol.func(arg1, arg2);
        std::cout << to_string(i) + " || " + to_string(my_res == label) + " || " + my_res + " || " + label << endl;

    }
    cout << "----------------------------------------" << endl;

}


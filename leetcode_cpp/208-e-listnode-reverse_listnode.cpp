//
// Created by junjie on 8/23/23.
//
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
#include "DataStructure.h"
#include "iostream"
#include "vector"

using namespace std;

class Solution {
public:
    /**
     * 定义tmp直接反转
     * @param head
     * @return
     */
    ListNode *reverseList(ListNode *head) {
        return head;
    }
};

int main() {
    Solution sol;
    vector<std::pair<std::vector<int>, int>> exps = {
            {{-2, 1,  -3, 4, -1, 2, 1, -5, 4}, 6},
            {{4,  -1, 2,  1},                  6},
            {{5,  4,  -1, 7, 8},               23},
    };
    for (const auto &exp: exps) {
        ListNode result = sol.reverseList(exp.first);
        std::cout << (result == exp.second) << " || " << result << " || " << exp.second << std::endl;
    }

}
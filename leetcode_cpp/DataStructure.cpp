//
// Created by junjie on 8/23/23.
//
#include "iostream"
#include "vector"
#include "DataStructure.h"

using namespace std;

std::vector<int> listNodeToArray(ListNode *head) {
    std::vector<int> result;
    while (head != nullptr) {
        result.push_back(head->val);
        head = head->next;
    }
    return result;
}

int main() {
    ListNode node;
}
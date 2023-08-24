//
// Created by junjie on 8/23/23.
//
#include "iostream"
#include "vector"
#include "DataStructure.h"

using namespace std;

/**
 * 将数组转换为 ListNode
 * @param arr
 * @param n
 * @return
 */
ListNode *vector2Node(int arr[], int n) {
    if (n == 0) {
        return nullptr;
    }
    ListNode *head = new ListNode(arr[0]);
    ListNode *cur = head;
    for (int i = 1; i < n; i++) {
        cur->next = new ListNode(arr[i]);
        cur = cur->next;
    }
    return head;
}

/**
 * 将 ListNode 转为 数组
 * @param head
 * @return
 */
vector<int> node2Vector(ListNode *head) {
    ListNode *cur = head;
    vector<int> arr;
    while (cur != nullptr) {
        arr.push_back(cur->val);
        cur = cur->next;
    }
    return arr;
}

/**
 * 打印 ListNode 到控制台
 */
void printNode(ListNode *head) {
    ListNode *cur = head;
    while (cur != nullptr) {
        cout << cur->val << " -> ";
        cur = cur->next;
    }
    cout << "null" << endl;
}


int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    ListNode *node = vector2Node(arr, n);
    printNode(node);
    vector<int> res = node2Vector(node);
    for (int n: res) {
        cout << n;
    }

}
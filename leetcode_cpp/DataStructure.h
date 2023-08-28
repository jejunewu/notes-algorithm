//
// Created by junjie on 8/23/23.
//

#ifndef NOTES_ALGORITHM_DATASTRUCTURE_H
#define NOTES_ALGORITHM_DATASTRUCTURE_H

/**
 * 链表结构
 */
struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}

    ListNode(int x) : val(x), next(nullptr) {}

    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


ListNode *vector2Node(int arr[], int n);

std::vector<int> node2Vector(ListNode *head);

void printNode(ListNode *head);


// ------------------------------- Binary Tree ------------------------------------- //

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}

    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
// ------------------------------------------------------------------------------------------- //

#endif //NOTES_ALGORITHM_DATASTRUCTURE_H

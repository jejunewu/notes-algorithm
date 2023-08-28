//
// Created by junjie on 8/28/23.
//
#include "DataStructure.h"
#include "iostream"
#include "vector"

using namespace std;

class Solution {
public:
    //递归方法
    void inorder(TreeNode *root, vector<int> *res) {
        if (root == nullptr) {
            return;
        }
        inorder(root->left, res);
        res->push_back(root->val);
        inorder(root->right, res);
    };

    vector<int> inorderTraversal(TreeNode *root) {
        vector<int> res;
        inorder(root, &res);
        return res;
    }
};
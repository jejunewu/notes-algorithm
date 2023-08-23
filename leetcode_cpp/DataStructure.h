//
// Created by junjie on 8/23/23.
//

#ifndef NOTES_ALGORITHM_DATASTRUCTURE_H
#define NOTES_ALGORITHM_DATASTRUCTURE_H

struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}

    ListNode(int x) : val(x), next(nullptr) {}

    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

#endif //NOTES_ALGORITHM_DATASTRUCTURE_H

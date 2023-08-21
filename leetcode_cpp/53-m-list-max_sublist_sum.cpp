//
// Created by Jejune on 2023/8/20.
//
/**
*
 * 53. 最大子数组和
中等
6.3K
相关企业
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。



示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23


提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104


进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
*/

#include "unordered_map"
#include <vector>
#include "iostream"
#include "utility"

using namespace std;

#include <iostream>
#include <vector>

class Solution {
public:
    //动态规划
    int maxSubArray(const std::vector<int> &nums) {
        int sub_sum = 0;
        int max_sum = nums[0];
        for (const int &n: nums) {
            sub_sum = max(sub_sum + n, n);
            max_sum = max(max_sum, sub_sum);
        }
        return max_sum;
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
        int result = sol.maxSubArray(exp.first);
        std::cout << (result == exp.second) << " || " << result << " || " << exp.second << std::endl;
    }

}

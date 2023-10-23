"""
原理参考参考视频教程：
https://www.bilibili.com/video/BV1vP411g7J3

- 时间复杂度
最好：O(nlogn)
最差：O(n^2)

- 空间复杂度
O(1)

- 稳定性
不稳定
"""


## 原版
def partition(arr, low, high):
    pivot = arr[low]
    while low < high:
        while low < high and arr[high] >= pivot:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] <= pivot:
            low += 1
        arr[high] = arr[low]
    arr[low] = pivot
    return low


def quick_sort(arr, low, high):
    if low >= high:
        return
    pivotpos = partition(arr, low, high)
    quick_sort(arr, low, pivotpos - 1)
    quick_sort(arr, pivotpos + 1, high)


if __name__ == '__main__':
    arr = [2, 9, 7, 3, 4, 6, 8, 1, 0, 5]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)

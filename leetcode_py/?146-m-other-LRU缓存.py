'''
146. LRU 缓存
中等
2.8K
相关企业
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。



示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4


提示：

1 <= capacity <= 3000
0 <= key <= 10000
0 <= value <= 105
最多调用 2 * 105 次 get 和 put
'''


# 未通过，有错误
class LRUCache:

    def __init__(self, capacity: int):
        self.lru = {capacity: -1}
        self.lru_order = [capacity]
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.lru:
            return self.lru[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.lru) == self.capacity:
            if key in self.lru:
                self.lru[key] = value
            else:
                key_pop = self.lru_order.pop(0)
                self.lru.pop(key_pop)
                self.lru_order.append(key)
                self.lru[key] = value
        else:
            if key in self.lru:
                self.lru[key] = value
            else:
                self.lru_order.append(key)
                self.lru[key] = value
        # if len(self.lru) == self.capacity and key not in self.lru:
        #     key_pop = self.lru_order.pop(0)
        #     self.lru.pop(key_pop)
        # elif key not in self.lru:
        #     self.lru_order.append(key)
        # self.lru[key] = value


class DLinkedNode:
    """ 双向链表 """
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None



class LRUCache2:
    """
    利用 HashMap + 双向链表的方式
    ref: https://leetcode.cn/problems/lru-cache/solutions/259678/lruhuan-cun-ji-zhi-by-leetcode-solution/
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        # 新建头尾，相互指向
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_node_to_tail(self, key):
        node = self.hashmap[key]

    def get(self, key: int) -> int:
        return

    def put(self, key: int, value: int) -> None:
        return


if __name__ == '__main__':
    lru = LRUCache(1)
    print(lru.put(2, 1))
    print(lru.get(2))
    print(lru.put(3, 2))
    print(lru.get(2))

# day07: 641. 设计循环双端队列

[641. 设计循环双端队列](https://leetcode-cn.com/problems/design-circular-deque/)

```

```
## Python

### 方法 使用数组实现

#### 思路

* 参考题解：[数组实现的循环双端队列](https://leetcode-cn.com/problems/design-circular-deque/solution/shu-zu-shi-xian-de-xun-huan-shuang-duan-dui-lie-by/)

```python
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.front = 0
        self.rear = 0
        self.capacity = k + 1
        self.bucket = [0 for _ in range(self.capacity)]
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.bucket[self.front] = value
        return True
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.bucket[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.bucket[self.front]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.bucket[(self.rear - 1 + self.capacity) % self.capacity]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.front == self.rear
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return (self.rear + 1) % self.capacity == self.front


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
```





# day07: 622. 设计循环队列

[622. 设计循环队列](https://leetcode-cn.com/problems/design-circular-queue/)

```

```
## Python

### 方法 使用数组实现循环队列

#### 思路

* 参考题解 [数组实现的循环队列](https://leetcode-cn.com/problems/design-circular-queue/solution/shu-zu-shi-xian-de-xun-huan-dui-lie-by-liweiwei141/)

```python
class MyCircularQueue:

    def __init__(self, k: int):
        self.front = 0
        self.rear = 0
        self.capacity = k + 1
        self.bucket = [0 for _ in range(self.capacity)]

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.bucket[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.bucket[self.front]


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.bucket[(self.rear - 1 + self.capacity) % self.capacity]


    def isEmpty(self) -> bool:
        return self.front == self.rear


    def isFull(self) -> bool:
        return (self.rear + 1) % self.capacity == self.front



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
```



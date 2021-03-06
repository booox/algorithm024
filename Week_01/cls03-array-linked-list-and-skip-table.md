
# 第1周 第3课 | 数组、链表、跳表 

* 本节课主要是两种最最基础的 **数据结构**：数组与链表
* **数据结构**: 军队中有对兵力的管理、调度的方式，在计算机对数据有存储、组织的方式，这种方式就叫**数据结构**
* 按数据的存储方式可以分为两种：
    * **顺序** 结构：数组
    * **链式** 结构：各种链表



## 3. 实战题目解析：盛水最多的容器、爬楼梯

### 11. 盛最多水的容器 

* [11. 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/)

#### 暴力解法

* 双层循环，将当前的面积与前面的最大面积比较，取较大者


```java
int max = 0;
for (int i = 0; i < a.length - 1; ++i) {
    for (int j = i + 1; j < a.length; ++j) {
        int area = (j - i) * Math.min(a[i], a[j]);
        max = Math.max(max, area);
    }
    return max;
}
```


```python
res = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        // do something
```




#### 向中间收敛（左右夹逼）方法

```java
for (int i = 0; i < a.length - 1; i < j) {
    for (int j = i + 1; j < a.length; ++j) {
        // do something
    }
}
```


```python
# use for
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        // do something


# 使用 while
res = 0
i, j = 0, len(height) - 1

while i < j:
    tmp = (j - i) * min(height[i], height[j])
    res = max(res, tmp)
    if height[i] < height[j]:
        i += 1
    else:
        j -= 1

return res        
```

### 70. 爬楼梯

* [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs)

#### 思路

* 当看到题目没有思路时，可以用下面的流程思考
    * 能不能用暴力？
    * 不能用暴力，它的基本情况是什么（最简）？
    * 看一下，它的 **最近重复子问题** 是怎样的？
        * 在不涉及人工智能的一般算法中，最终都要归结到：`if...else...` , `for while` 与 `recursion` 
        * 既然如此，在处理很多题时，都要去思考它的 **重复子问题**


### 15. 三数之和

* [15. 三数之和](https://leetcode-cn.com/problems/3sum/)
* [1. 两数之和](https://leetcode-cn.com/problems/two-sum/)


#### 思路

* 要彻底理解三数之和，先来看两数之和
    * 题目：要在给定 nums 中，找满足 `a + b = target` 的整数对
    * 解法：
        * 使用暴力：两重循环，总的时间复杂度为 O(n^2)
        * 使用哈希表，使第 2 次遍历的时间复杂度变成 O(1)
* 三数之和
    * 解法 1：
        * 题目：要在给定 nums 中，找满足 `a + b + c = 0` 的三元组
        * 思路：
            * 所求可以转化为求 `a + b = -c` ，而这里的 `-c` 可以是 `nums` 中任一值

```java
int max = 0;
for (int i = 0; i < a.length - 1; ++i) {
    for (int j = i + 1; j < a.length; ++j) {
        int area = (j - i) * Math.min(a[i], a[j]);
        max = Math.max(max, area);
    }
    return max;
}
```
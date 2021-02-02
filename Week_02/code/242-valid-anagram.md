# 242. 有效的字母异位词: 

[242. 有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/)

```

```
## Python

### 方法 1: 暴力解法：排序后比较字符串是否相等

#### 思路

* 先判断 s 与 t 长度是否相等，不等直接返回 False
* 分别对两者排序，然后比较二者是否相等

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. 使用暴力：排序后比较字符是否相等
        # time: O(nlogn); space: O(logn)
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
```

#### 复杂度分析

* 时间复杂度：O(nlogn)
    * 排序：O(nlogn)；比较字符串相等：O(n)
    * 总的：O(nlogn + n) = O(nlogn)
* 空间复杂度：O(logn)
    * 排序需要 O(logn) 的空间复杂度


### 方法 2: 使用哈希表统计字母出现次数

#### 思路

* 先将 s 的字母放入哈希表中，值为出现的次数
* 再遍历 t
    * 如果 t 中字母不在哈希表，或对应的值 < 0，则返回 False
    * 如果 t 中字母存在哈希表，就将字母对应的值减 1

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1

        for c in t:
            d[c] = d.get(c, 0) - 1
            if d[c] < 0:
                return False
                
        return True
```

#### 复杂度分析

* 时间复杂度：O(n)
    * 获取字母频数：O(n)；遍历数组 t： O(n)
    * 总的：O(n + n) = O(2n) = O(n)
* 空间复杂度：O(n)
    * 创建哈希表所需空间：O(n)


### 方法 3: 使用 Python 内置

#### 思路

* 与方法 2 同，只是使用了 Python 内置数组结构 collections.Counter

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 3. 使用 collections.Counter
        if len(s) != len(t):
            return False
        
        import collections
        cnt = collections.Counter(s)

        for c in t:
            cnt[c] = cnt.get(c, 0) - 1
            if cnt[c] < 0:
                return False

        return True
```

#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(n)

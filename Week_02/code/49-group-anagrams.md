# 49. 字母异位词分组 

[49. 字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/)

```

```
## Python

### 方法 1: 使用暴力解法：排序后再分组

#### 思路

* 字母相同，但排列不同的字符串，排序后都一定是相同的。
* 可以将排序后的字符串，做为哈希表的 key，其余同组的字符串添加到列表中
* 这就需要使用 `collections.defaultdict`，将 `list` 设为默认值

```python
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. 暴力法
        # # 先排序，然后分组
        d = collections.defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            d[key].append(s)
        
        return list(d.values())
```

#### 复杂度分析

* n 为字符串数量
* k 为字符串最大长度

* 时间复杂度：O(nklogk)
    * 需要遍历 n 个字符串，每个字符串需要 O(klogk) 的时间排序
    * 此外还需要 O(1) 时间更新哈希表
    * 总的时间：O(nklogk)

* 空间复杂度：O(nk)


### 方法 2: 计数：统计每个字符串中字母出现的次数

#### 思路

* 主要思想，还是找到「异位词」的分组标准，在上一种方法是对字母进行排序
* 而现在则是统计每个字符串中字母出现的次数
* 可以预先创建一个长度为 26 的数组，用于存储每个字符串中字母出现的次数

```python
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 2. 计数，统计字母数字做为哈希表的 key
        d = collections.defaultdict(list)
        
        for s in strs:
            # 构造长度为 26 的数组，用于存储每个字母出现的次数
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            # list 可变不能做哈希表的 key，所以转成 tuple
            d[tuple(counts)].append(s)

        return list(d.values())
```

#### 复杂度分析

* 时间复杂度：O(nk)
    * 需要遍历 n 个字符串，每个字符串需要在 O(k) 时间计算每个字母出现的次数

* 空间复杂度：O(nk)


### 方法 3: 统计每个字符串出现次数 2

#### 思路

* 思路与方法 2 类似，只是这次是用另一种方式作为 key
    * 举例：将 "anagram" -> "a3g1m1n1"
* 但执行起来却很慢~~

```python
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 3. 计数
        d = collections.defaultdict(list)
        
        for s in strs:
            cnt = collections.Counter(s)
            # "anagram" -> "a3g1m1n1"
            key = ''.join([f"{k}{v}" for k, v in sorted(cnt.items())])
            d[key].append(s)

        return list(d.values())
```

#### 复杂度分析

* n 为字符串数量，k 为字符串的最大长度

* 时间复杂度：O(nk)
    * 不太好分析，头疼，但肯定超过了 O(nk)
* 空间复杂度：O(nk)


### 方法 4: 计数，来一种更慢的

#### 思路

* 

```python
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        
        for s in strs:
            # 构造长度为 26 的数组，用于存储每个字母出现的次数
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1

            key = ""
            for i in range(26):
                if counts[i] != 0:
                    key += f"{chr(97 + i)}{counts[i]}"
            d[key].append(s)     

        return list(d.values()) 
```

#### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()

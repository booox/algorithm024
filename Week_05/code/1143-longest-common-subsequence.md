# 1143. 最长公共子序列: 

[1143. 最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/)

```
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。

 

示例 1:

输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace"，它的长度为 3。
示例 2:

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。
示例 3:

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0。
 

提示:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
输入的字符串只含有小写英文字符。
```
## 方法 1: 动态规划 

### 思路

*  这题为什么要用动态规划，或者适合用动态规划来解决这题？
    * 比较 `abcde` 与 `ace`，可以 **从后面往前看起**，也即，**自底向上递推**
        * `e == e` 所以二者至少有一个公共子序列就是 `e`
        * 最终的 LCS 就等于 **前面** `abcd` 与 `ac` 这个子序列的 **公共子序列** 再加上 `1`
        * 同样的思路，原问题就可转换为一个带有 **重复性子问题** 的问题求解
        * 所以可以使用 **动态规划** 来求解
* 对于字符串比较的问题，大多是将两个字符串转换为 **二维动态规划** 
* 具体思路
    * 假设 `text1` 与 `text2` 的长度分别为 `m` 与 `n`
    * 定义一个二维数组 `dp` 来存储最长公共子序列的长度，二维数组的长度为 (m + 1) * (n + 1)
        * 这里可以不加 1，但是不加1你就要用其它限制条件来确保这个 index 是有效的
        * 而加 1 之后，就不需要去判断只是让索引为0的行和列表示空串。
    * `dp[i][j]` 表示 `text1[:i]` 与 `text2[:j]` 最长公共子序列的长度。
    * `dp[m][n]` 即为最终结果。
    * `text1[i]` 与 `text2[j]` 的值有两种情况：
        * 相等：
            * 此时的 LCS 就等于 `text1` 的前 `i - 1` 个字符 与 `text2` 的前 `j - 1` 个字符的LCS 再加上 `1`，即 `dp[i][j] = dp[i-1][j-1] + 1` 
        * 不相等：
            * 此时的 LCS 的 **来源** 有两种情况，要取它们的 **最大值**
                * `text1` 的 前 `i - 1` 个字符与 `text2` 的前 `j` 个字符的 LCS
                * `text1` 的 前 `i` 个字符与 `text2` 的前 `j - 1` 个字符的 LCS
            * 即 `dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])`


```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 因为i和j是从1开始循环的，
                # 这样 dp[i-1][j-1] 才是从 dp[0][0] 开始递推的，否则漏掉了一个元素
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
```

**或类似的另一种**

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[m][n]
```




### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()

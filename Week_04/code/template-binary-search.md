

## 二分查找模板

### Python

* 循环退出条件： `low <= high` 
* mid 的取值： 
    * `mid = low+(high-low)/2` 
    * 或使用位运算: `mid = low+((high-low)>>1)` 

```python
low, high = 0, len(array) - 1
while low <= high:
    mid = (low + high) / 2
    if array[mid] == target:
        return some
    elif array[mid] > target:
        high = mid - 1
    else:
        low = mid + 1
```


### 

```C++
int binarySearch(const vector<int>& nums, int target) {
	int left = 0, right = (int)nums.size()-1;
	
	while (left <= right) {
		int mid = left + (right - left)/ 2;
		if (nums[mid] == target) return mid;
		else if (nums[mid] < target) left = mid + 1;
		else right = mid - 1;
	}
	
	return -1;
}
```


### Java

```java
// Java
public int binarySearch(int[] array, int target) {
    int left = 0, right = array.length - 1, mid;
    while (left <= right) {
        mid = (right - left) / 2 + left;

        if (array[mid] == target) {
            return mid;
        } else if (array[mid] > target) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return -1;
}
```


### JavaScript

```javascript
/* JavaScript */
let left = 0, right = len(array) - 1
while (left <= right) {
  let mid = (left + right) >> 1
  if (array[mid] === target) { /*find the target*/; return }
  else if (array[mid] < target) left = mid + 1
  else right = mid - 1
}
```



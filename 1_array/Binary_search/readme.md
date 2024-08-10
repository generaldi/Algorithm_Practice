# 题目

给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
## 示例1
```
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
``` 
## 示例2
```
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中
``` 
## 提示
- 你可以假设 nums 中的所有元素是不重复的。
- n 的范围在 [1, 10000]。
- nums 的每个元素都是一个整数，范围在 [-9999, 9999]。

## 二分查找中的区间不变性

在二分查找算法的实现过程中，保持区间的不变性是确保算法正确性的重要原则之一。这意味着在算法的每一步中，我们必须严格遵循区间的定义（如左闭右闭、左闭右开等），并在相应操作中保持区间的一致性。下面是对这一思路的详细阐述：

### 区间的不变性

**定义区间：**  
在二分查找中，我们通常会选择一个搜索区间，比如左闭右闭区间 `[left, right]` 或左闭右开区间 `[left, right)`。一旦确定了区间的类型，就需要在整个算法中严格遵守这一定义。

**保持不变性：**  
无论是左闭右闭区间 `[left, right]` 还是左闭右开区间 `[left, right)`，在每次迭代中，我们都需要确保对区间的更新保持与初始定义一致。这意味着当我们调整 `left` 或 `right` 边界时，要注意不打破区间的定义。

以左闭右闭区间 `[left, right]` 为例：

- **计算中间点：** `mid = left + (right - left) / 2`
- **调整区间：** 如果目标值小于 `mid` 指向的元素，说明目标在左半部分，因此将 `right` 更新为 `mid - 1`，保持区间左闭右闭的特性。如果目标值大于 `mid` 指向的元素，说明目标在右半部分，因此将 `left` 更新为 `mid + 1`，同样保持区间左闭右闭的特性。

对于左闭右开区间 `[left, right)`：

- **计算中间点：** `mid = left + (right - left) / 2`
- **调整区间：** 如果目标值小于 `mid` 指向的元素，更新 `right` 为 `mid`，而不是 `mid - 1`，以保持右边界开区间的性质。若目标值大于 `mid` 指向的元素，更新 `left` 为 `mid + 1`。
  
以下python代码实现了二分查找算法，并采用了左闭右开的区间定义 `[left, right)`：

```python
class Solution:
    def binary_search(self, nums: list[int], target: int):
        # 初始化搜索区间为左闭右开区间 [left, right)
        left, right = 0, len(nums)
        
        # 只要区间不为空，就继续搜索
        while left < right:
            # 计算中间点
            middle = (left + right) // 2
            
            # 如果找到目标值，返回其索引
            if nums[middle] == target:
                return middle
            
            # 如果中间值大于目标值，目标在左半部分，调整右边界
            elif nums[middle] > target:
                right = middle  # 注意：这里保持右开区间性质，不减 1
            
            # 如果中间值小于目标值，目标在右半部分，调整左边界
            else:
                left = middle + 1  # 保持左闭区间性质
        
        # 如果未找到目标值，返回 -1
        return -1
        # 测试代码
        nums = [-1, 0]
        target_exist = 0
        target_not_exist = 2
        print('Searching', target_exist, 'in', nums, ', returning:', Solution().binary_search(nums, target_exist))
        print('Searching', target_not_exist, 'in', nums, ', returning:', Solution().binary_search(nums, target_not_exist))
```


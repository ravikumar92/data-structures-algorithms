class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = 0
        while left <= right:
            mid = int((left + right)/2)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid  + 1
            else:
                right = mid - 1
        if target < nums[mid]:
            return mid
        else:
            return mid + 1
nums = [1,3]
target = 2
sol = Solution()
print(sol.search(nums, target))

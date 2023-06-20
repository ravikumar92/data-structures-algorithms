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
        return -1

nums = [-1,0,3,5,9,12]
sol = Solution()
print(sol.search(nums, 9))

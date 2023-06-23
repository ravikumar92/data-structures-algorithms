''''
Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

'''
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        #This is the linear time complexity solution. We could also do this using O(log n) time complexity
        #for ch in letters:
        #    if target < ch:
        #        return ch 
        #return letters[0]
        
        ans = 0
        left = 0
        right = len(letters) - 1

        while left <= right:
            mid = int((left + right) /2)
            print(f'mid', mid)
            if letters[mid] == target:
                left = mid + 1
            elif letters[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid
        return letters[ans]



arr = ["c", "f", "j"]
sol = Solution()
print(sol.nextGreatestLetter(arr, "c"))


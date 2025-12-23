class Solution:
    def is_searching(self, nums: list[int], target: int) -> list[int]:
        def binary_search(nums, target, is_left):
            left = 0
            right = len(nums) - 1
            idx = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid -1
                elif nums[mid] < target:
                    left = mid -1
                else:
                    idx = mid
                    if is_left:
                        right = mid - 1
                    else:
                        left = mid + 1
            return idx
        left = binary_search(nums, target, True)
        right =binary_search(nums, target, False)
        return [left, right]
sol = Solution()
nums = list(map(int, input().split()))
target = int(input())
print(sol.is_searching(nums, target))

    
    
    
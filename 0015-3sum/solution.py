class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        nums.sort()

        for indx, val in enumerate(nums):
            if indx > 0 and val == nums[indx-1]:
                continue
            
            left = indx + 1
            right = len(nums) - 1

            while left < right:
                currsum = val + nums[left] + nums[right]

                if currsum > 0:
                    right -= 1
                elif currsum < 0:
                    left += 1
                else:
                    triplets.append([val, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left< right and nums[left] == nums[left-1]:
                        left += 1

        return triplets

        

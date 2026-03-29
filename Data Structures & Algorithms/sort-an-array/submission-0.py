class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums: List[int]):
            if len(nums)<=1:
                return nums
            m = len(nums)//2
            left = merge_sort(nums[:m])
            right = merge_sort(nums[m:])
            return merge(left, right)
        def merge(left: List, right: List):
            srt = []
            while left!=[] and right != []:
                if left[0]<=right[0]:
                    srt.append(left[0])
                    left.pop(0)
                elif left[0]>right[0]:
                    srt.append(right[0])
                    right.pop(0)
            else:
                srt.extend(left)
                srt.extend(right)
            return srt
        return merge_sort(nums)
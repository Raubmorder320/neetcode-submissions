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
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i]<=right[j]:
                    srt.append(left[i])
                    i+=1
                elif left[i]>right[j]:
                    srt.append(right[j])
                    j+=1

            else:
                srt.extend(left[i:])
                srt.extend(right[j:])
            return srt
        return merge_sort(nums)

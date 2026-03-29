from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        answer = []
        for i in range(len(nums)):
            dic[nums[i]]+=1
        heap = []
        heapq.heapify_max(heap)
        for _ in range(len(dic)):
            heapq.heappush(heap, dic.popitem()[::-1])
        heapq.heapify_max(heap)

        for _ in range(k):
            answer.append(heapq.heappop_max(heap)[1])
            heapq.heapify_max(heap)
        return answer
        
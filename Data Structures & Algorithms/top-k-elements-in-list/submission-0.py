class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        
        buckets = [[] for _ in range(len(nums)+1)]
        for val, count in counts.items():
            buckets[count].append(val)
        
        answer = []
        for _ in range(k):
            while len(buckets[-1]) == 0:
                buckets.pop()
            answer.append(buckets[-1].pop())
        
        return answer
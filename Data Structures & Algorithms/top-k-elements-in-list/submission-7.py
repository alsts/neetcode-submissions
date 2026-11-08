class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        # Counting:
        for n in nums:
            counts[n] += 1

        # fill heap
        max_heap_by_counts = []
        for num, count in counts.items():
            slot = (-1 * count, num)
            heapq.heappush(max_heap_by_counts, slot)

        # take k elements
        res = []
        while len(res) < k:
            res.append(heapq.heappop(max_heap_by_counts)[1])

        return res    


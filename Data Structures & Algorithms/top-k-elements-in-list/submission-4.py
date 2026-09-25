class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count each number
        num_counts = {}
        for num in nums:
            num_counts[num] = 1 + num_counts.get(num, 0)

        # push (counts, number) tuple to Max Heap:
        max_heap_by_count = []
        for num, counts in num_counts.items():
            tuple_count_num = (-1 * counts, num)  # negate to get Max Heap (heapq - is Min Heap)
            heapq.heappush(max_heap_by_count, tuple_count_num)  # first val in tuple would be used for sorting

        result = []
        for i in range(k):
            result.append(heapq.heappop(max_heap_by_count)[1])

        return result 



        
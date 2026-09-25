class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq_buckets = [[] for i in range(0, len(nums) + 1)]  # max bucket can be the size of nums

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        for num, count in counts.items():
            freq_buckets[count].append(num)

        res = []

        # loop through buckets in reverse order:
        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
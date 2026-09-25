class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count each number
        num_counts = {}
        for num in nums:
            num_counts[num] = 1 + num_counts.get(num, 0)

        # buckets sort
        buckets = [[] for i in range(len(nums) + 1)]  # +1 needed since counts would be represented by index
        for num, counts in num_counts.items():
            buckets[counts].append(num)

        # loop backwards in buckets to get the highest num counts first:
        result = []
        for i in range(len(buckets) - 1, 0, -1):  # range (from, to, step)
            if len(buckets[i]) > 0:
                for num in buckets[i]:
                    result.append(num)

                    if len(result) == k:
                        return result


        
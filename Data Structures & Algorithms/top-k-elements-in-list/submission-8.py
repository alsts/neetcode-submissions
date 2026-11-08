class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        # Counting:
        for n in nums:
            counts[n] += 1

        # fill heap
        bucket_count = [[] for _ in range(len(nums) + 1)] # can be equal to max count (index alignment)

        for num, count in counts.items():
            bucket_count[count].append(num)

        # take k elements
        res = []
        for i in range(len(bucket_count) - 1, 0,  -1):
            for bucket_num in bucket_count[i]:
                res.append(bucket_num)
                if len(res) == k:
                    return res

        return []    


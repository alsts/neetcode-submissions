class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        k_set = set()
        # min heap?

        for n in nums:
            frequency_map[n] = 1 + frequency_map.get(n, 0)

            if len(k_set) < k:
                k_set.add(n)
            elif n in k_set:
                continue
            else:
                for k_item in k_set:
                    if frequency_map[k_item] < frequency_map[n]:
                        k_set.remove(k_item)
                        k_set.add(n)
                        break

        return list(k_set)
        
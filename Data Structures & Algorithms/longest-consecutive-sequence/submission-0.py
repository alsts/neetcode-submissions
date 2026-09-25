class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # Conversion takes: O(n)
        max_seq = 0

        for num in nums:  # Loop through each number: O(n)
            if (num - 1) not in num_set:  # start of sequence (no left neighbour)
                seq_len = 0

                # count sequence length: O(n) - At Max items would be visited twice (not start of seq, part of seq)
                while (num + seq_len) in num_set:
                    seq_len += 1

                max_seq = max(max_seq, seq_len)

        return max_seq
        
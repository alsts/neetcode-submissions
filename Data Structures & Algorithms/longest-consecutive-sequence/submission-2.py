class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq_count = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set: # beginning of sequence, 2,[4],5,6 
                
                count = 1
                while num + count in nums_set: # loop through sequence 2,4,5,[6],8
                    count += 1

                seq_count = max(count, seq_count)    

        return seq_count
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1


        sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1]))

        return list(sorted_freq.keys())[-k:]


        
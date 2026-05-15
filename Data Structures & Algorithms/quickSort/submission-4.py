# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, pairs, start, end):
        if end - start + 1 <= 1:
            return
        
        pivot = pairs[end]
        swap = start

        for i in range(start, end):
            if pairs[i].key < pivot.key:
                tmp = pairs[i]
                pairs[i] = pairs[swap]
                pairs[swap] = tmp
                swap += 1
        
        pairs[end] = pairs[swap]
        pairs[swap] = pivot

        self.quickSortHelper(pairs, start, swap - 1)
        self.quickSortHelper(pairs, swap + 1, end)
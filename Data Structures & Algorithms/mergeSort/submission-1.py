# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # base case, already sorted
        if len(pairs) <= 1: # len 0, 1
            return pairs

        # split in half
        mid = len(pairs) // 2 # len 2 -> 1, 3 -> 1, 4 -> 2
        left = self.mergeSort(pairs[:mid])
        right = self.mergeSort(pairs[mid:])

        # merge left and right in order
        i = 0
        j = 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        if i < len(left):
            merged.extend(left[i:])
        else:
            merged.extend(right[j:])

        return merged
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num_map = [[n, arr1.count(n)] for n in arr2]
        seen = set(arr2)
        unseen = []
        res = []

        for arr in num_map:
            res.extend([arr[0]] * arr[1])

        for n in arr1:
            if n not in seen:
                unseen.append(n)
        
        unseen.sort()
        res.extend(unseen)
        arr1 = res
        return arr1
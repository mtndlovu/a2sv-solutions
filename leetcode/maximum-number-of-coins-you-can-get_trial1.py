class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        max_idx = n - 1
        num_coins = 0
        
        for i in range(n // 3):
            num_coins += piles[max_idx - 1]
            max_idx -= 2

        return num_coins
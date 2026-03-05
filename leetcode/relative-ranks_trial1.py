class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scores = sorted(score, reverse=True)
        ranks = []

        for n in score:
            rank = scores.index(n) + 1
            if rank == 1:
                ranks.append("Gold Medal")
            elif rank == 2:
                ranks.append("Silver Medal")
            elif rank == 3:
                ranks.append("Bronze Medal")
            else:
                ranks.append(str(rank))

        return ranks
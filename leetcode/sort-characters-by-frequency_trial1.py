class Solution:
    def frequencySort(self, s: str) -> str:
        char_map = {}
        chars = [c for c in s]
        
        for char in s:
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1

        chars = sorted(chars, reverse=True, key=lambda x: (char_map[x], x))
        return "".join(chars)
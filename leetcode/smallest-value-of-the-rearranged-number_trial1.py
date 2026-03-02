class Solution:
    def smallestNumber(self, num: int) -> int:
        if 0 <= num <= 20:
            return num

        digits = [token for token in str(num)]
        n = len(digits)
        if num > 20:
            digits.sort()
            i = 0
            while digits[i] == '0' and i < n:
                i += 1

            if digits[0] == "0":
                digits[0] = digits[i]
                digits[i] = "0"
            return int("".join(digits))
        else:
            digits = digits[1:]
            digits.sort(reverse=True)
            return -1 * int("".join(digits))
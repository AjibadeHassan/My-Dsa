class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        if t == 1:
            return n

        result = n
        n %= 100

        first = n // 10 or 1
        second = n % 10

        for _ in range(10):
            # Check divisibility
            if (first * second) % t == 0:
                return result

            # Increment last two digits
            if second == 9:
                second = 0
                first += 1
            else:
                second += 1

            result += 1

        return result

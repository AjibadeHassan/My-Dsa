class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):

        reservedSeats.sort()

        m = len(reservedSeats)

        reserved = [False] * 11

        ans = 0
        l = 0
        r = 0
        prev = 0

        def check(left, right):
            for seat in range(left, right + 1):
                if reserved[seat]:
                    return False
            return True

        while r < m:

            # Count completely empty rows
            ans += 2 * (reservedSeats[r][0] - prev - 1)

            prev = reservedSeats[r][0]

            # Mark all reserved seats in the current row
            while r < m and reservedSeats[r][0] == reservedSeats[l][0]:
                reserved[reservedSeats[r][1]] = True
                r += 1

            two_to_five = check(2, 5)
            four_to_seven = check(4, 7)
            six_to_nine = check(6, 9)

            if two_to_five and six_to_nine:
                ans += 2
            elif two_to_five or four_to_seven or six_to_nine:
                ans += 1

            l = r

            # Reset for the next row
            reserved = [False] * 11

        # Remaining rows are completely empty
        ans += 2 * (n - prev)

        return ans

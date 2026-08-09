class Solution:

    def __init__(self):
        self.primes = [2, 3, 5, 7]

    def smallestNumber(self, num: str, t: int) -> str:

        primeCount = [0] * 8
        numLength = len(num)
        firstZeroIndexFromLeft = 0

        for prime in self.primes:
            while t % prime == 0:
                t //= prime
                primeCount[prime] += 1

        if t != 1:
            return "-1"

        minLength = self.getMinLength(primeCount)

        if numLength < minLength:
            return self.buildSuffix(primeCount, minLength, [''] * minLength)

        result = [''] * (numLength + 1)

        i = 0
        while firstZeroIndexFromLeft < numLength:

            i += 1
            result[i] = num[firstZeroIndexFromLeft]

            if result[i] == '0':
                break

            self.logNum(primeCount, result[i], -1)
            firstZeroIndexFromLeft += 1

        if self.getMinLength(primeCount) == 0:

            if firstZeroIndexFromLeft == numLength:
                return num

            firstZeroIndexFromLeft += 1

            for j in range(firstZeroIndexFromLeft, len(result)):
                result[j] = '1'

            return ''.join(result[1:])

        last = numLength - 1

        for end in range(min(firstZeroIndexFromLeft, last), -1, -1):

            self.logNum(primeCount, result[end + 1], 1)

            while True:

                nxt = chr(ord(result[end + 1]) + 1)

                if nxt > '9':
                    break

                result[end + 1] = nxt

                self.logNum(primeCount, result[end + 1], -1)

                if self.getMinLength(primeCount) <= last - end:
                    return self.buildSuffix(primeCount, last - end, result)

                self.logNum(primeCount, result[end + 1], 1)

        return self.buildSuffix(primeCount, len(result), result)

    def logNum(self, primeCount, ch, value):

        if ch < '2':
            return

        if ch == '9':
            primeCount[3] += value * 2

        elif ch == '4':
            primeCount[2] += value * 2

        elif ch == '8':
            primeCount[2] += value * 3

        elif ch == '6':
            primeCount[2] += value
            primeCount[3] += value

        else:
            primeCount[ord(ch) - ord('0')] += value

    def buildSuffix(self, primeCount, targetLength, result):

        primeCount = primeCount[:]
        index = len(result)

        while primeCount[3] > 1:
            primeCount[3] -= 2
            index -= 1
            result[index] = '9'

        while primeCount[2] > 2:
            primeCount[2] -= 3
            index -= 1
            result[index] = '8'

        while primeCount[7] > 0:
            primeCount[7] -= 1
            index -= 1
            result[index] = '7'

        if primeCount[2] > 0 and primeCount[3] > 0:
            index -= 1
            result[index] = '6'
            primeCount[2] -= 1
            primeCount[3] -= 1

        while primeCount[5] > 0:
            primeCount[5] -= 1
            index -= 1
            result[index] = '5'

        while primeCount[2] > 1:
            primeCount[2] -= 2
            index -= 1
            result[index] = '4'

        while primeCount[3] > 0:
            primeCount[3] -= 1
            index -= 1
            result[index] = '3'

        while primeCount[2] > 0:
            primeCount[2] -= 1
            index -= 1
            result[index] = '2'

        while index + targetLength != len(result):
            index -= 1
            result[index] = '1'

        if targetLength == len(result):
            return ''.join(result)

        return ''.join(result[1:])

    def getMinLength(self, primeCount):

        count2 = max(0, primeCount[2])
        count3 = max(0, primeCount[3])

        count23 = (count3 & 1) + (count2 % 3)

        return (
            count3 // 2
            + count2 // 3
            + max(0, primeCount[7])
            + max(0, primeCount[5])
            + (2 if count23 == 3 else (1 if count23 > 0 else 0))
        )

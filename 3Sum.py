class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        a + b + c = 0 => b + c = -a
        so we can loop in each of array then get b + c = -a
        """
        numbers.sort()
        output = []
        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue

            self.findTwoSum(numbers, i + 1, len(numbers) - 1, -numbers[i], output)

        return output

    def findTwoSum(self, numbers, left, right, target, output):
        lastPair = (None, None)
        while left < right:
            if numbers[left] + numbers[right] == target:
                if (numbers[left], numbers[right]) != lastPair:
                    output.append([-target, numbers[left], numbers[right]])

                lastPair = (numbers[left], numbers[right])
                left = left + 1
                right = right - 1
            elif numbers[left] + numbers[right] > target:
                right = right - 1
            else:
                left = left + 1

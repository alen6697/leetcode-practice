class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # make maximum number of subarray to be first element
        # then make first element to last position in subarray
        """
        3 2 4 1 -> choose 4 because it is max number
        4 2 3 1 -> flip subarray arr[0:(max's index)]
        1 3 2 4 -> move 4 to last position
        """
        result = []
        for i in range(len(arr), 0, -1):
            pos = arr.index(i) # get i's index
            if pos == i - 1: # number i is in ith position so we don't have to flip
                continue
                
            if pos != 0:
                result.append(pos + 1) # append index + 1 means we append maximum number in subarray
                arr[:pos + 1] = arr[:pos + 1][::-1] # move max number to first position
                
            result.append(i) # append i because we choose max number
            arr[:i] = arr[:i][::-1]
            
        return result

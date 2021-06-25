class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        quotient = 0
        sign = 1
        if divisor < 0:
            divisor = divisor * (-1)
            sign = sign * (-1)
            
        if dividend < 0:
            dividend = dividend * (-1)
            sign = sign * (-1)
                     
        while dividend >= divisor:
            tmp = divisor
            mul = 1
            while dividend >= tmp:
                dividend = dividend - tmp
                quotient = quotient + mul
                mul = mul + mul
                tmp = tmp + tmp
        
        quotient = quotient * sign
        
        return min(2147483647, max(-2147483648, quotient))

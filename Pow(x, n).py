class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 0
        pos_neg = True
        if n < 0:
            pos_neg = False
            n = n * -1
        def power(number,to_power):
            if(to_power == 1):
                return number
            if to_power % 2 == 0:
                return power(number,to_power/2) * power(number, to_power/2)
            else:
                to_power = to_power - 1
                return power(number,(to_power)/2) * power(number,(to_power)/2) * number
        
        if n == 0:
            return 1
        result =  power(x,n)

            
        if not pos_neg:
            return 1 / result
        else: 
            return result
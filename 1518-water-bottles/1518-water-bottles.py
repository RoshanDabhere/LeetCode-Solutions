class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            newBottles = empty // numExchange
            total += newBottles
            empty = (empty % numExchange)+ newBottles
        
        return total

        
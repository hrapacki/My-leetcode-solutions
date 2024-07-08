class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        how_many_to_drink = numBottles
        while numBottles >= numExchange:
            how_many_to_drink += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange
        return how_many_to_drink
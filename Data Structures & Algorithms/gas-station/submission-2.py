class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # run through sstations once
        # calculate total gas and cost, if cost greater than gas, return -1 immediately
        # 
        total_gas = 0
        total_cost = 0
        index = -1
        surplus = float('-inf')

        for i in range(len(gas)-1, -1, -1):
            total_gas+=gas[i]
            total_cost+=cost[i]
            if total_gas - total_cost > surplus:
                index = i
                surplus = total_gas-total_cost
        
        return -1 if total_cost > total_gas else index
            

class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        gas_cost = [gas[i] - cost[i] for i in range(len(gas))]
        start_index = 0
        current_cost_sum = 0
        total_cost = sum(gas_cost)
        while start_index < len(gas):
            if gas_cost[start_index] >= 0:
                if total_cost - current_cost_sum >= 0:
                    s = 0
                    check = True
                    for idx in range(start_index, len(gas)):
                        s += gas_cost[idx]
                        if s < 0:
                            check = False
                            break
                    if check and s + current_cost_sum >= 0:
                        return start_index
            current_cost_sum += gas_cost[start_index]
            start_index += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.canCompleteCircuit(gas=[1, 2, 3, 4, 5],
                               cost=[3, 4, 5, 1, 2]))
    print(s.canCompleteCircuit(gas=[2, 3, 4],
                               cost=[3, 4, 3]))

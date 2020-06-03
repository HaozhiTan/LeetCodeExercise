class Solution:
    def twoCitySchedCost(self, costs) -> int:
        # sum of cost for all people to A
        list_a = [a for a, b in costs]
        # refund of cost if these people choose B, negative means positive refund
        refund = [b-a for a, b in costs]
        # choose the half of people of the highest refund to go to B
        return sum(list_a) + sum(sorted(refund)[:(len(refund) // 2)])


if __name__ == '__main__':
    s = Solution()
    print(s.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))

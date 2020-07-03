class Solution:
    def prisonAfterNDays(self, cells, N: int):
        # in maximum, we have 2 ^ 8 different situations
        # PS there are also solutions which are using the fact that if there is a loop,
        # it will always have length 14 (or divisor of it).
        if N <= 0:
            return cells
        days = N
        count = 0
        d = {tuple(cells): 0}
        while days > 0:
            prev_cells = cells.copy()
            for i in range(8):
                if i == 0 or i == 7:
                    cells[i] = 0
                else:
                    cells[i] = int(prev_cells[i - 1] == prev_cells[i + 1])
            count += 1
            days -= 1
            if tuple(cells) in d.keys():
                break
            d[tuple(cells)] = count
        if days == 0:
            return cells
        else:
            cycle_length = count - d[tuple(cells)]
            days = (N - d[tuple(cells)]) % cycle_length
            while days > 0:
                prev_cells = cells.copy()
                for i in range(8):
                    if i == 0 or i == 7:
                        cells[i] = 0
                    else:
                        cells[i] = int(prev_cells[i - 1] == prev_cells[i + 1])
                days -= 1
            return cells


if __name__ == '__main__':
    s = Solution()
    print(s.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7))
    print(s.prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0], 1000000000))

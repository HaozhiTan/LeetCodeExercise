class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # if the robot cannot go back to the origin within 4 steps, it will diverge.
        instructions = 4 * instructions
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        current_pos = [0, 0]
        current_dir = 0
        for instruction in instructions:
            if instruction == 'L':
                current_dir = (current_dir + 1) % 4
            elif instruction == 'R':
                current_dir = (current_dir - 1) % 4
            else:
                current_pos[0] += directions[current_dir][0]
                current_pos[1] += directions[current_dir][1]
        if current_pos == [0, 0]:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isRobotBounded('GL'))
    print(s.isRobotBounded('GG'))
    print(s.isRobotBounded('GR'))
    print(s.isRobotBounded('GLR'))
    print(s.isRobotBounded('GGLLGG'))

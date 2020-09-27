import sys


def dynamic_programming(index, used):
    if index >= n:
        return 1
    if dp[index][used]:
        return dp[index][used]
    chains = 1
    for i in range(index+1, n):
        if triangles[i][3] != triangles[index][3]:  # must find the larger grey scale
            for j in range(1, 4):
                if j != used:  # cannot use the connected side of triangle to chain with another triangle
                    for k in range(1, 4):
                        if triangles[index][j - 1] == triangles[i][k - 1]:  # find the side to connect
                            chains = max(chains, dynamic_programming(i, k) + 1)
    dp[index][used] = chains
    return chains


if __name__ == '__main__':
    line = sys.stdin.readline()  # read one line only
    line = line.strip()
    input_list = line.split(' ')
    n = int(input_list[0])
    triangles = []
    for i in range(n):
        line = sys.stdin.readline()  # read one line only
        line = line.strip()
        input_list = line.split(' ')
        triangles.append((int(input_list[0]), int(input_list[1]), int(input_list[2]), float(input_list[3])))
    triangles = sorted(triangles, key=lambda t: t[3])  # sort by the color in ascending order
    # dp[i][j] refers to the longest chain when the i-th triangle are connected with the j-th side
    # j == 0 refers to not connected
    dp = [[0 for j in range(4)] for i in range(n)]
    ans = 0
    for idx in range(n):
        ans = max(ans, dynamic_programming(idx, 0))
    print(ans)


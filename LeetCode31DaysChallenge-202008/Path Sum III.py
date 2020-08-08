from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # dfs with cumulative sum and hash table
        def dfs(root, target, path_sum, count_dict):
            if not root:
                return 0
            path_sum += root.val

            if path_sum == target:
                n_paths = 1
            else:
                n_paths = 0

            # try to find if there is path where
            # target = current path_sum - previous path_sum

            previous_needed_path_sum = path_sum - target
            n_paths += count_dict[previous_needed_path_sum]

            count_dict[path_sum] += 1

            n_paths += dfs(root.left, target, path_sum, count_dict)
            n_paths += dfs(root.right, target, path_sum, count_dict)

            count_dict[path_sum] -= 1
            return n_paths

        return dfs(root, sum, 0, defaultdict(int))


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    print(s.pathSum(root, 3))


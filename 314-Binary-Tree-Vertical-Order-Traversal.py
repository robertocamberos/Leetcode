# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      if not root:
        return []
      q = deque([(root,0)])
      cols = defaultdict(list)
      res = []
      minDepth = float('inf')
      maxDepth = float('-inf')
      while q:
          for i in range(len(q)):
              node, column = q.popleft()
              if node:
                  cols[column].append(node.val)
                  minDepth = min(minDepth, column)
                  maxDepth = max(maxDepth,column)
                  q.append((node.left, column - 1))
                  q.append((node.right, column + 1))
          
      return [cols[x] for x in range(minDepth, maxDepth+1)]
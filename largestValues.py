from collections import deque
class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def largestValues(self,root):
        if not root:
            return[]
        
        result=[]
        queue=deque([root])

        while queue:
            level_size=len(queue)
            max_val=float('-inf')

            for _ in range(level_size):
                node=queue.popleft()
                max_val=max(max_val,node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(max_val)
        return result

def buildTree(nodes):
    if not nodes or nodes[0] is None:
        return None
    root = TreeNode(nodes[0])
    queue=deque([root])
    i=1
    while queue and i < len(nodes):
        node=queue.popleft()
        if nodes[i] is not None:
            node.left=TreeNode(nodes[i])
            queue.append(node.left)
        i+=1
        if i < len(nodes) and nodes[i] is not None:
            node.right=TreeNode(nodes[i])
            queue.append(node.right)
        i +=1
    return root

root_list=[1,3,2,5,3,None,9]
root=buildTree(root_list)
sol=Solution()
print(sol.largestValues(root))
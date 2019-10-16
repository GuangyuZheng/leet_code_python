from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # using one queue version
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        current_node = 0
        miss_node = 0
        results = []
        queue = []
        layer_nodes_upper_bound = 1
        current_upper_bound = 1
        current_layer_nodes = []
        if root is None:
            return results
        else:
            queue.append(root)
        while len(queue) != 0:
            node = queue.pop(0)
            current_layer_nodes.append(node.val)
            if node.left is None:
                miss_node += 1
            else:
                queue.append(node.left)
            if node.right is None:
                miss_node += 1
            else:
                queue.append(node.right)
            current_node += 1
            if current_node == current_upper_bound:  # finish one layer
                if len(current_layer_nodes) != 0:
                    results.insert(0, current_layer_nodes)
                current_layer_nodes = []
                layer_nodes_upper_bound *= 2
                current_upper_bound = current_upper_bound + layer_nodes_upper_bound
                current_node += miss_node
                miss_node *= 2
        return results

    # using two queues version
    def levelOrderBottomV2(self, root: TreeNode) -> List[List[int]]:
        current_layer_results = []
        total_results = []
        current_layer_queue = []
        next_layer_queue = []
        if root is None:
            return total_results
        else:
            current_layer_queue.append(root)
        while len(current_layer_queue) != 0:
            node = current_layer_queue.pop(0)
            current_layer_results.append(node.val)
            if node.left is not None:
                next_layer_queue.append(node.left)
            if node.right is not None:
                next_layer_queue.append(node.right)
            if len(current_layer_queue) == 0:
                total_results.insert(0, current_layer_results)
                current_layer_queue = next_layer_queue
                next_layer_queue = []
                current_layer_results = []
        return total_results




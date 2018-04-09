# Prob 797. All Paths From Source to Target

# Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

# Example:
# Input: [[1,2], [3], [3], []]
# Output: [[0,1,3],[0,2,3]]
# Explanation: The graph looks like this:
# 0--->1
# |    |
# v    v
# 2--->3
# There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# Note:

# The number of nodes in the graph will be in the range [2, 15].
# You can print different paths in any order, but you should keep the order of nodes inside one path.


def allPathsSourceTarget(graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        target = len(graph)-1
        stack = [[0]] # save paths
        ret = []
        while stack:
            cur = stack.pop()
            for n in graph[cur[-1]]:
                if n == target:
                    ret.append(cur+[n])
                else:
                    stack.append(cur+[n])
        return ret


def allPathsSourceTarget2(graph):
    res = []
    def dfs(i, path):
        if i == len(graph) - 1:
            res.append(path)
        [dfs(j, path + [j]) for j in graph[i]]
    dfs(0, [0])
    return res

if __name__ == "__main__":
    print(allPathsSourceTarget([[1,2], [3], [3], []]))
    


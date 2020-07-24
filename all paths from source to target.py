'''Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.'''

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if graph is None:
            return []
        res = [[0]]
        #res.insert(0,0)
        print(res)
        for i in range(len(graph)):
            graph[i].sort()
            if(i==0):
                for j in range(1,len(graph)):
                    if j in graph[i]:
                        res.insert(j,[res[i]+[j]])
                    else:
                        res.insert(j,[])
                print(res)
            else:
                for j in graph[i]:
                    for k in res[i]:
                        res[j].append(k+[j])
        return(res[len(res)-1])
            
        

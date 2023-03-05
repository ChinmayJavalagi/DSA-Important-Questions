'''The Bellman–Ford algorithm is an algorithm that computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph.

Dijkstra doesn’t work for Graphs with negative weights/negative cycles, Bellman-Ford works for such graphs.'''

#TC - V*E

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    
    def bellman_ford(self, V, edges, S):
        #code here
        adj = defaultdict(list)
        dist = [10**8]*V
        dist[S] = 0
        for i in range(V-1):
            for s in edges:
                u = s[0]
                v = s[1]
                w = s[2]
                if dist[u]!=10**8 and dist[u]+w < dist[v]:
                    dist[v] = dist[u]+w
                    
        for s in edges:
            u = s[0]
            v = s[1]
            w = s[2]
            if dist[u]!=10**8 and dist[u]+w<dist[v]:
                return [-1]
            
                
        return dist
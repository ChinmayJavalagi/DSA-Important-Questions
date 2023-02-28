''''It finds the shortest paths from a single source vertex to all other vertices in a graph.''''

#TC - E*log(V) 

import heapq
import math
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        pq = []
        dist = [math.inf]*V
        dist[S] = 0
        heapq.heappush(pq, (S, 0))
        while pq:
            s = heapq.heappop(pq)
            n = s[0]
            w = s[1]
            for i in adj[n]:
                u = i[0]
                if i[1]+w < dist[u]:
                    dist[u] = i[1]+w
                    heapq.heappush(pq, (u, dist[u]))
                    
        return dist

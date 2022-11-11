class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        edges = {u: [] for u in range(n)}
        for flight in flights:
            edges[flight[0]].append((flight[1], flight[2]))
            
        A = []
        A.append((0, src, K+1))
        
        while 0 < len(A):
            top = heapq.heappop(A)
            x, y, edge = top
            if dst == y: 
                return x
            if (edge > 0):
                for vertex in edges[y]:
                    heapq.heappush(A, (x + vertex[1], vertex[0], edge-1))
                    
        return -1
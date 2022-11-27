class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        temp = []
        
        for p1, p2 in points:
            distance = p1 **2 + p2 ** 2
            temp.append([distance, p1, p2])
            
        heapq.heapify(temp)
        res = []
        while k > 0:
            distance, p1, p2 = heapq.heappop(temp)
            res.append([p1,p2])
            k -= 1
        return res
            
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        q = deque()
        visit = set(deadends)
        turns = 0
        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
            
        q.append("0000")
        while q:
            for i in range(len(q)):
                lock = q.popleft()
                if lock == target:
                    return turns
                for child in children(lock):
                    if child not in visit:
                        q.append(child)
                        visit.add(child)
            turns += 1
        return -1
                    
            
        
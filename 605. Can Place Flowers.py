class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        
        for i in range(len(flowerbed)):
            if count >= n:
                break
            
            if flowerbed[i] == 0:
                if i == 0:
                    prev = 0
                else:
                    prev = flowerbed[i-1]
                if i == len(flowerbed)-1:
                    Next = 0
                else:
                    Next = flowerbed[i+1]
                
                if prev == 0 and Next == 0:
                    flowerbed[i] = 1
                    count += 1
                    
        return count == n
class Solution:
    def trap(self, height: List[int]) -> int:
        #find max
        if not height:
            return 0
        highest = 0
        highest_i = 0
        for h_i, h in enumerate(height):
            if h > highest:
                highest = h
                highest_i = h_i
        
        #to right
        raw_area = 0
        x_distance = 1
        prevHigh = height[0]
        
        for to_right in range(1,highest_i):
            curr = height[to_right]
            if curr <= prevHigh:
                x_distance+=1
            else:
                raw_area+=x_distance*prevHigh
                prevHigh = curr
                x_distance=1
        
        if highest_i != 0:
            raw_area += x_distance*prevHigh
            first_half = raw_area
            
        x_distance = 1
        prevHigh = height[-1]
        for to_left in range(len(height)-2,highest_i,-1):
            curr = height[to_left]
            if curr <= prevHigh:
                x_distance+=1
            else:
                raw_area+=x_distance*prevHigh
                prevHigh = curr
                x_distance=1
        
        if highest_i != len(height)-1:
            raw_area += x_distance*prevHigh

        res = raw_area-sum(height)+highest
        return res
        
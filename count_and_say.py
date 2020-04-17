class Solution:
    def countAndSay(self, n: int) -> str:
        res = [1,1]
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        for _ in range(1,n-1):
            new = []
            subList = []
            for num in res:
                if not subList:
                    subList.append(num)
                else:
                    if subList[-1] == num:
                        subList.append(num)
                    else:
                        new.append(subList.copy())
                        subList.clear()
                        subList.append(num)
            new.append(subList.copy())
            newRes = []
            for subList in new:
                count = len(subList)
                val = subList[0]
                newRes.append(count)
                newRes.append(val)
            res = newRes
        
        final = ""
        for char in newRes:
            final+=str(char)
        return final
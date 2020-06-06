class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ret = []
        num = {}
        for p in people:
            h = p[0]
            n = p[1]        
            if n in num:
                num[n].append(h)
            else:
                num[n] = [h]
        
        
        lenq = len(people)
        while len(ret) < lenq:
            minn = min(num)
            val = num[minn]
            if ret == []:
                val.sort()
                for v in val:
                    ret.append([v,minn])
            else:
                val.sort(reverse=True)
                for v in val:
                    lenr = len(ret)
                    i = 0 
                    chk = 0
                    c = 0
                    while i < lenr and chk == 0 and c < minn:
                        if ret[i][0] >= v:
                            c = c + 1
                        if c <= minn:
                            i = i + 1 
                    ret = ret[:i] + [[v,minn]] + ret[i:]
            del num[minn]
            # print(num,ret)
        return ret
                
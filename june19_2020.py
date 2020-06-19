class Solution:
    def longestDupSubstring(self, S: str) -> str:
        
        p = 2**63-1
        
        def rabin_karp(mid):
            cur_hash = 0
            for i in range(mid):
                cur_hash = (cur_hash * 26 + nums[i]) % p
            hashes = {cur_hash}
            pos = -1
            max_pow = pow(26, mid, p)
            for i in range(mid, len(S)):
                cur_hash = (26*cur_hash-nums[i-mid]*max_pow + nums[i]) % p
                if cur_hash in hashes:
                    pos = i + 1 - mid
                hashes.add(cur_hash)
            return pos

        nums = [ord(c)-ord('a') for c in S]        
        r = len(S)-1
        l = 0
        maxs = ""
        maxi = 0
        start,end = 0,0
        while l <= r:
            
            mid = int((l+r)//2)
            
            val = rabin_karp(mid)
            
            if val == -1:
                r = mid-1
            else:
                start,end = val,val+mid
                l = mid + 1 
        return S[start:start+l-1]
    

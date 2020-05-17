class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        len_s = len(s)
        len_t = len(t)
        target_dict = collections.Counter(t)
        curr_d = {}
        formed = 0
        required = len(target_dict)
        ans = float('inf'), None, None
        
        if len_t > len_s: return ""
        while r < len_s:
            curr_d[s[r]] = curr_d.get(s[r],0) + 1
            char = s[r]
            
            if char in target_dict and target_dict[char] == curr_d[char]:
                formed += 1
            while l <= r and formed == required:
                # we have formed all chars
                # now lets shrink the window by moving the left pointer
                el_char = s[l]
                # compare current window with previous smallest window
                if r-l+1 < ans[0]:
                    ans = r-l+1, l, r
                
                curr_d[el_char] -= 1
                if el_char in target_dict and curr_d[el_char] < target_dict[el_char]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]
                
                

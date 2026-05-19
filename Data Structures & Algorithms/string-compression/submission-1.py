class Solution:
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 0
        lst = []
        while l < len(chars):
            lC = chars[l]
            lst.append(lC)
            cnt = 0
            while r < len(chars) and chars[r] == lC:
                cnt += 1
                r += 1
            if cnt > 1:
                lst.extend(list(str(cnt)))
            l = r
        chars[0:len(lst)] = lst
        return len(lst)
                
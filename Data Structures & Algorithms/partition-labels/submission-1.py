class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, c in enumerate(s):
            last[c] = i
        arr = []
        sizes = []
        curSet = set()
        i = 0
        while i < len(s):
            c = s[i]
            start = i
            end = last[c]
            j = i
            while j <= end:
                end = max(end, last[s[j]])
                j += 1
            arr.append(s[start: end + 1])
            sizes.append(end + 1 - start)
            i = end + 1
        print(arr)
        print(sizes) 
        return sizes

            


        


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = []
        parts = []
        # i is each phone digit
        def dfs(i):
            if i == len(digits): # one combo of all digits done
                if parts:
                    res.append("".join(parts.copy()))
                return
            for c in phone[digits[i]]:
                parts.append(c)
                dfs(i + 1) # next digit char
                parts.pop()

        dfs(0)
        return res
        
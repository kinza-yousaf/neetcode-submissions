class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        adj = defaultdict(list)
        wordList.append(beginWord)
        wordSet = set(wordList)
        for word in wordList:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordSet:
                        adj[word].append(newWord)
                        adj[newWord].append(word)
        q = deque([beginWord])
        visited = {beginWord}
        res = 1
        found = False
        print(adj)
        while q:
            for i in range(len(q)):
                word = q.popleft()

                for nei in adj[word]:
                    if nei in visited:
                        continue
                    q.append(nei)
                    visited.add(nei)
                    if nei == endWord:
                        found = True
                        break
            res += 1
            if found:
                break
        return res if found else 0



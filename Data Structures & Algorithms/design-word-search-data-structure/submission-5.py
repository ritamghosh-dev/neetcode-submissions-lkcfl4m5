class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        

    def search(self, word: str) -> bool:
        def recur_search(node, l):
            curr = node
            for i in range(l, len(word)):
                if word[i] == ".":
                    for child in curr.children:
                        if recur_search(curr.children[child], i+1):
                            return True
                    return False
                elif word[i] not in curr.children:
                    return False
                else:
                    curr = curr.children[word[i]]
            return curr.word
        return recur_search(self.root,0)
        

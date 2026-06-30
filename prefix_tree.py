class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.is_end = False

    def contains_key(self, ch:str)-> bool:
        return self.links[ord(ch) - ord('a')]

    def put(self, ch:str, newNode: 'TrieNode')-> None:
        return self.links[ord(ch) - ord('a')] = node

    def se


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str)-> None:
        node = self.root
        for ch in word:
            if not node.contains_key(ch):
                node.put(ch, TrieNode())




t = Trie()
t.insert("le")

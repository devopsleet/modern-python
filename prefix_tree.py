class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.isEnd = False

    def contains(self, ch: str) -> bool:
        return self.links[ord(ch) - ord('a')] is not None

    def put(self, ch: str, node: 'TrieNode') -> None:
        self.links[ord(ch) - ord('a')] = node

    def get(self, ch: str) -> 'TrieNode':
        return self.links[ord(ch) - ord('a')]

    def set_end(self):
        self.isEnd = True


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        node = self.root
        for ch in word:
            if not node.contains(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.set_end()


t = Trie()
t.insert("le")

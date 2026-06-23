class TrieNode:
    def __init__(self):
        self.data = None
        self.children = {}

def build_trie(words):
    root = TrieNode()
    for word in words:

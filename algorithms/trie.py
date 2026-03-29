class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """Search for a word in the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def contains_any(self, text):
        """Check if the text contains any word in the trie."""
        # Simple implementation for finding any substring
        for i in range(len(text)):
            node = self.root
            for char in text[i:]:
                if char in node.children:
                    node = node.children[char]
                    if node.is_end_of_word:
                        return True
                else:
                    break
        return False

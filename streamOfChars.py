# Initialization:
# T: O(Σ |word|), where Σ is the sum of the lengths of all words.
# S: O(Σ |word|), for storing the Trie. ￼ ￼
# Query:
# T: O(L), where L is the length of the longest word.
# S: O(L), for storing the stream. ￼


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.stream = deque()
        self.max_len = 0

        # Insert reversed words into the Trie
        for word in words:
            self.max_len = max(self.max_len, len(word))
            node = self.root
            for char in reversed(word):
                node = node.children.setdefault(char, TrieNode())
            node.is_end = True

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        if len(self.stream) > self.max_len:
            self.stream.pop()

        node = self.root
        for char in self.stream:
            if char not in node.children:
                return False
            node = node.children[char]
            if node.is_end:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

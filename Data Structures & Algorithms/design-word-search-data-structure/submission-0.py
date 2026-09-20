class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = WordDictionary()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        return self._dfs(word, 0)   # start matching at index 0, from self (root)

    def _dfs(self, word: str, i: int) -> bool:
        node = self
        # base case: matched every character — was this path a real word?
        if i == len(word):
            return node.is_end

        c = word[i]
        if c == '.':
            # try EVERY child; if any leads to a full match, we're done
            for child in node.children.values():
                if child._dfs(word, i + 1):
                    return True
            return False
        else:
            if c not in node.children:
                return False
            return node.children[c]._dfs(word, i + 1)
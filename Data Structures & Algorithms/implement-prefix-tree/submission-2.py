class PrefixTree:

    def __init__(self): # understand that an instance of prefix tree is really just a node, with its own set of children and is_end condition. The root self is what will point to these children, who point to theirs, and so on
        self.children = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = PrefixTree()
            node = node.children[c]
        node.is_end = True
            

    def search(self, word: str) -> bool:
        node = self
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.websites = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        curr = len(self.websites)-1
        while curr != self.index:
            self.websites.pop()
            curr-=1
        self.websites.append(url)
        self.index+=1
        

    def back(self, steps: int) -> str:
        if self.index - steps < 0:
            self.index = 0
        else:
            self.index -= steps
        return self.websites[self.index]
        

    def forward(self, steps: int) -> str:
        if self.index + steps >= len(self.websites):
            self.index = len(self.websites)-1
        else:
            self.index += steps
        return self.websites[self.index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
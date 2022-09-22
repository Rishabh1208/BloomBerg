
# Time: O(1) for each method
# Space: O(N), where N is the most URLs we save
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.bound = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr == len(self.history):
            self.history.append(url)
        else:
            self.history[self.curr] = url
        self.bound = self.curr

    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps, 0)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, self.bound)
        return self.history[self.curr]

# use two stacks
class BrowserHistory:

    def __init__(self, homepage: str):
        self.curPage = homepage  # We keep track of the page we are currently on
        self.prevStack = []  # We keep track of the pages if we were to go back
        self.forwardStack = []  # We keep track of the pages if we were to go forward

    def visit(self, url: str) -> None:
        self.prevStack.append(self.curPage)  # Step 1
        self.forwardStack = []  # Step 2
        self.curPage = url  # Step 3

    def back(self, steps: int) -> str:
        possible = min(steps, len(self.prevStack))

        while possible:  # Step 0
            self.forwardStack.append(self.curPage)  # Step 1
            self.curPage = self.prevStack.pop()  # Step 2
            possible -= 1  # Step 3

        return self.curPage  # We need to return the page we're at currently

    def forward(self, steps: int) -> str:
        possible = min(steps, len(self.forwardStack))

        while possible:  # Step 0
            self.prevStack.append(self.curPage)  # Step 1
            self.curPage = self.forwardStack.pop()  # Step 2
            possible -= 1  # Step 3

        return self.curPage  # We need to return the page we're at currently
# ...................................................................................
# Use of DLL
## APPROACH : LINKED LISTS ##
## LOGIC : GREEDY ##

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = ListNode(homepage)

    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.root
        self.root.next = node
        self.root = self.root.next

    def back(self, steps: int) -> str:
        while(steps and self.root.prev):
            self.root = self.root.prev
            steps -= 1
        return self.root.val

    def forward(self, steps: int) -> str:
        while(steps and self.root.next):
            self.root = self.root.next
            steps -= 1
        return self.root.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# .....................................................................

class BrowserHistory:
    def __init__(self, homepage: str):
        self.homepage = homepage
        # history and forward stack
        self.history = []
        self.forwardHistory = []

    def visit(self, url: str) -> None:
        # simply push this url to history and clear forward history
        self.history.append(url)
        self.forwardHistory = []

    def back(self, steps: int) -> str:
        # go through steps amount or history amount
        for _ in range(min(steps, len(self.history))):
            # pop from history and add to forward history
            self.forwardHistory.append(self.history.pop())

        # return current in history (if history)
        return self.history[-1] if self.history else self.homepage

    def forward(self, steps: int) -> str:
        # go through steps amount or history amount
        for _ in range(min(steps, len(self.forwardHistory))):
            # pop from forward history and add to history
            self.history.append(self.forwardHistory.pop())

        # return current in history (if history)
        return self.history[-1] if self.history else self.homepage

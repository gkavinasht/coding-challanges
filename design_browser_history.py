# 1472. Design Browser History
# You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.
# Implement the BrowserHistory class:
# BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
# void visit(string url) Visits url from the current page. It clears up all the forward history.
# string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
# string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
 
# Double Linked List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.root = ListNode(homepage)

    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.root
        self.root.next = node
        self.root = self.root.next

    def back(self, steps: int) -> str:
        while steps and self.root.prev:
            self.root = self.root.prev
            steps -= 1
        return self.root.val

    def forward(self, steps: int) -> str:
        while steps and self.root.next:
            self.root = self.root.next
            steps -= 1
        return self.root.val

# Stack
# class BrowserHistory:
#     def __init__(self, homepage: str):
#         self.history = []
#         self.visit(homepage)

#     def visit(self, url: str) -> None:
#         self.history.append(url)
#         self.future = []

#     def back(self, steps: int) -> str:
#         while len(self.history) > 1 and steps > 0:
#             self.future.append(self.history.pop())
#             steps -= 1
#         return self.history[-1]

#     def forward(self, steps: int) -> str:
#         while self.future and steps > 0:
#             self.history.append(self.future.pop())
#             steps -= 1
#         return self.history[-1]

browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
print(browserHistory.back(1))
print(browserHistory.back(1))
print(browserHistory.forward(1))
browserHistory.visit("linkedin.com")
print(browserHistory.forward(2))
print(browserHistory.back(2))
print(browserHistory.back(7))

# ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
# [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
# Output:
# [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

# Explanation:
# BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
# browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
# browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
# browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
# browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
# browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
# browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
# browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
# browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
# browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
# browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
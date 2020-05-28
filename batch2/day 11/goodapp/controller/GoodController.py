class Good:

    def __init__(self,v):
        self.view = v
        print("Good Controller is invoked")

    def good_basic(self):
        self.view.label.config(text="This is good basic")

    def good_advanced(self):
        self.view.label.config(text="This is good advanced")
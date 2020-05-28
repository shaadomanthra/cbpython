class Good:

    def __init__(self,view):
        self.view = view
        # print("sample")

    def goodbasic(self):
        self.view.label.config(text="This is good basic")
        # print("good basic")

    def goodadvanced(self):
        self.view.label.config(text="This is good advanced")
        # print("good advanced")
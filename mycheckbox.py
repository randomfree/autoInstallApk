from tkinter import Checkbutton, IntVar


class MyCheckBox(Checkbutton):
    def __init__(self,text):
        super(MyCheckBox, self).__init__()
        self["text"] = text
        self["onvalue"] = 1
        self["offvalue"] = 0
        self.CheckVar = IntVar()
        self["variable"] = self.CheckVar

    def isCheck(self):
        return self.CheckVar.get() == 1

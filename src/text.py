from page import Abschnitt


class Text(Abschnitt):

    def __init__(self):
        self.var = "Text"

    def createScriptBlock(self):
        print(self.var)

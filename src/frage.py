from abschnitt import Abschnitt


class Frage(Abschnitt):

    def __init__(self):
        self.var = "Frage"

    def createScriptBlock(self):
        print(self.var)

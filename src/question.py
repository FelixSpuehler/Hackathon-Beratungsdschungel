from page import Page


class Question(Page):

    def __init__(self):
        self.var = "Frage"

    def create_script_block(self):
        print(self.var)

    def add_answer(self):
        print("add" + self.var)

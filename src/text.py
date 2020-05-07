from page import Page


class Text(Page):

    def __init__(self, q_id, title, formulation):
        self.id = q_id
        self.title = title
        self.formulation = formulation

    def create_script_block(self):
        print(self.title)

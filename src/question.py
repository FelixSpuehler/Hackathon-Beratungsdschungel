from page import Page


class Question(Page):

    def __init__(self, p_id, title, formulation, first_answer, first_goto):
        self.p_id = p_id
        self.title = title
        self.formulation = formulation
        self.answers = [first_answer]
        self.gotos = [first_goto]

    def add_answer(self, new_answer, new_goto):
        self.answers.append(new_answer)
        self.gotos.append(new_goto)

    def create_script_block(self):
        print(self.title)

    def __str__(self):
        return 'Question: {}, {}, {}, {}, {}' .format(self.p_id, self.title, self.formulation, self.answers, self.gotos)

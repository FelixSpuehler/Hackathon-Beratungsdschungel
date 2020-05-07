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

    def create_block_page(self):
        # start page block
        script_block = """
        // Page {p_id}
        var Page{p_id} = form.addPageBreakItem().setTitle("{title}");
        var item{p_id} = form.addMultipleChoiceItem();""".format(p_id=self.p_id,
                                                                 title=self.title)
        return script_block

    def create_block_question(self):
        # start page block
        script_block = """
        item{p_id}.setTitle("{formulation}").setChoices([""".format(p_id=self.p_id,
                                                                    formulation=self.formulation)

        # add questions and gotos
        for index, (answer, goto) in enumerate(zip(self.answers, self.gotos)):
            if index < len(self.answers) - 1:
                script_block += """item{p_id}.createChoice('{answer}', Page{goto}), """.format(p_id=self.p_id, answer=answer, goto=goto)
            else:
                script_block += """item{p_id}.createChoice('{answer}', Page{goto})])""".format(p_id=self.p_id, answer=answer, goto=goto)
        # finish code block
        script_block += """.setRequired(true);"""
        return script_block

    def __str__(self):
        return 'Question: {}, {}, {}, {}, {}' .format(self.p_id, self.title, self.formulation, self.answers, self.gotos)

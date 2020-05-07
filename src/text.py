from page import Page


class Text(Page):

    def __init__(self, p_id, title, formulation):
        self.p_id = p_id
        self.title = title
        self.formulation = formulation

    def create_script_block(self):
        # start page block
        script_block = """
        // Page {p_id}
        var Page{p_id} = form.addPageBreakItem().setTitle("{title}").setHelpText("{formulation}").setGoToPage(FormApp.PageNavigationType.GO_TO_PAGE.endPage);"""\
            .format(p_id=self.p_id, title=self.title, formulation=self.formulation)
        return script_block

    def __str__(self):
        return 'Text: {}, {}, {}' .format(self.p_id, self.title, self.formulation)


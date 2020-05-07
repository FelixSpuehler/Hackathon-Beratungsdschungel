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
        var Page{p_id} = form.addPageBreakItem().setTitle("{title}").setHelpText("{formulation}");"""\
            .format(p_id=self.p_id, title=self.title, formulation=self.formulation)
        print(script_block)

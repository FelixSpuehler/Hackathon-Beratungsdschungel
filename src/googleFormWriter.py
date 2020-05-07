from datetime import datetime

from page import Page
from question import Question
from text import Text


class GoogleFormWriter:
    @staticmethod
    def write(pages_dict, project_title, file_name=""):
        print("Writing: Start")

        text_start = """function createForm() {{
        // create & name Form
        var item = "{project_title}";
        var form = FormApp.create(item).setTitle(item);""".format(project_title=project_title)

        text_page_end = """
        // end page
        var endPage = form.addPageBreakItem().setTitle("Bis bald!").setHelpText("Hoffentlich konnte ich dir helfen!");"""

        text_end = """
        endPage.setGoToPage(FormApp.PageNavigationType.SUBMIT);
}"""

        if file_name == "":
            dt_string = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = "../data/{}_{}.gs".format(dt_string, project_title)

        with open(file_name, "w") as file:
            file.write(text_start)
            for p_id, page in pages_dict.items():
                file.write(page.create_block_page())

            file.write(text_page_end)

            for p_id, page in pages_dict.items():
                if isinstance(page, Question):
                    file.write(page.create_block_question())

            file.write("")

            for p_id, page in pages_dict.items():
                if isinstance(page, Text):
                    file.write(page.create_block_submit())

            file.write(text_end)

        print("Writing: End")

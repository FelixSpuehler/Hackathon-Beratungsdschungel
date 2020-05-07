from datetime import datetime

from page import Page


class GoogleFormWriter:
    @staticmethod
    def write(pages_dict, project_title, file_name=""):
        print("Writing: Start")

        text_start = """function createForm() {{
        // create & name Form
        var item = "{project_title}";
        var form = FormApp.create(item).setTitle(item);""".format(project_title=project_title)

        text_end = """
        
}"""

        if file_name == "":
            dt_string = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = "../data/{}_{}.gs".format(dt_string, project_title)

        with open(file_name, "w") as file:
            file.write(text_start)
            for p_id, page in pages_dict.items():
                file.write(page.create_script_block())

            file.write(text_end)

        print("Writing: End")

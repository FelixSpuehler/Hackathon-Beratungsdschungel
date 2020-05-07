from page import Page

class GoogleFormWriter:
    @staticmethod
    def write(pages_dict, project_title):
        start_text = """function createForm() {
        
        // create & name Form
        var item = "{project_title}";
        var form = FormApp.create(item).setTitle(item);""".format(project_title=project_title)

        text_end = "}"

        print(start_text)
        print(text_end)


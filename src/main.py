from datetime import datetime

from csvReader import CsvReader
from googleFormWriter import GoogleFormWriter

from question import Question
from text import Text

if __name__ == '__main__':
    """ HIER INFOS ANGEBEN """
    # Speicherort der Baum-CSV-Datei
    csv_file = '../data/Baum_Beispiel.csv'
    # Projekt Titel
    project_title = "Version_{}".format(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    gs_file = "../data/{}.gs".format(project_title)

    print("Los!")
    pages_dict = CsvReader.read(csv_file)

    GoogleFormWriter.write(pages_dict=pages_dict,
                           project_title=project_title,
                           file_name=gs_file)

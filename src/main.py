from datetime import datetime

from csvReader import CsvReader
from googleFormWriter import GoogleFormWriter

from question import Question
from text import Text

if __name__ == '__main__':
    """ HIER INFOS ANGEBEN """
    # Speicherort der Baum-CSV-Datei
    csv_file = '../data/Baum_Incom.csv'
    # Projekt Titel
    #project_title = "Version_{}".format(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    project_title = "Baum_1800"
    # Speicherort der gs-Datei.
    gs_file = "../data/Baum_Incom.gs".format(project_title)

    # Lesen der CSV-Datei
    pages_dict = CsvReader.read(csv_file)

    # Schreiben in die gs-Datei
    GoogleFormWriter.write(pages_dict=pages_dict,
                           project_title=project_title,
                           file_name=gs_file)

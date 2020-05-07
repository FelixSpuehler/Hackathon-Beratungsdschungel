from csvReader import CsvReader
from googleFormWriter import GoogleFormWriter

from question import Question
from text import Text

if __name__ == '__main__':
    print("Los!")
    pages_dict = CsvReader.read('../data/Baum_Beispiel.csv')
    # print(len(pages))
    # for key, value in pages.items():
    #     print(value)
    #     print(value.create_script_block())

    GoogleFormWriter.write(pages_dict=pages_dict,
                           project_title="Digitale Studienberatung")

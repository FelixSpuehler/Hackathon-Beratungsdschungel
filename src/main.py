from csvReader import CsvReader

from question import Question
from text import Text

if __name__ == '__main__':
    print("Los!")
    pages = CsvReader.read('../data/Baum_Beispiel.csv')
    print(len(pages))
    for key, value in pages.items():
        print(value)
        print(value.create_script_block())

import os
import csv
from question import Question
from text import Text


class CsvReader:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    @staticmethod
    def read(file_name):
        print("Reading: Start")
        pages_dict = {}
        with open(file_name) as csv_file:
            csv_reader_object = csv.reader(csv_file, delimiter=';')
            next(csv_reader_object)
            for p_id, p_type, title, formulation, answer, goto  in csv_reader_object:
                if p_id in pages_dict.keys():
                    pages_dict[p_id].add_answer(answer, goto)
                elif p_type == 'Frage':
                    pages_dict[p_id] = Question(p_id, title, formulation, answer, goto)
                else:
                    pages_dict[p_id] = Text(p_id, title, formulation)

        print("Reading: End")
        return pages_dict

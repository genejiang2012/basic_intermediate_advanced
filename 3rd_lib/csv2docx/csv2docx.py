import argparse
import csv
import sys

from docx import *


class DataCSV:
    def __init__(self, file):
        if file.split('.')[-1] == "csv":
            self.file = file
        else:
            self.file = file + ".csv"

    def operate_file(self):
        steps_result_list = []
        with open(self.file, encoding='utf-8') as f:
            file_csv = csv.DictReader(f)

            for row in file_csv:
                steps_result_list.append(
                    {'steps': row['步骤'], 'expect': row['预期']})

        return steps_result_list


class MyDoc:
    def __init__(self):
        self.document = Document()  # use the Document class from docx
        style = self.document.styles['Normal']
        font = style.font
        font.name = "等线"
        font.size = shared.Pt(10)

    def add_paragraph(self, content):
        p = self.document.add_paragraph(content)
        p.add_run().bold = True

    def create_table(self, header, records):
        table = self.document.add_table(rows=2, cols=5)
        table.style = 'TableGrid'

        # merge the first row
        first_row = table.rows[0]
        first_row.cells[0].merge(first_row.cells[-1])
        first_row.cells[0].paragraphs[0].add_run('Objective1: ').bold = True

        # create the header
        hdr_cells = table.rows[1].cells
        hdr_cells[0].paragraphs[0].add_run(header[0]).bold = True
        hdr_cells[1].paragraphs[0].add_run(header[1]).bold = True
        hdr_cells[2].paragraphs[0].add_run(header[2]).bold = True
        hdr_cells[3].paragraphs[0].add_run(header[3]).bold = True
        hdr_cells[4].paragraphs[0].add_run(header[4]).bold = True

        # fill the data to table
        row_cells = table.add_row().cells
        row_cells[0].text = records[0]
        row_cells[1].text = records[1]
        row_cells[2].text = records[2]
        row_cells[3].text = records[3]
        row_cells[4].text = records[4]

    def create_header(self, header):
        table = self.document.add_table(rows=1, cols=5)

        # create the header
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = header[0]
        hdr_cells[1].text = header[1]
        hdr_cells[2].text = header[2]
        hdr_cells[3].text = header[3]
        hdr_cells[4].text = header[4]

    def create_records(self, records):
        table = self.document.add_table(rows=1, cols=5)

        for desc, con, expect_result, actual_result, comments in records:
            row_cells = table.add_row().cells
            row_cells[0].text = desc
            row_cells[1].text = con
            row_cells[2].text = expect_result
            row_cells[3].text = actual_result
            row_cells[4].text = comments

    def save_doc(self, doc_name):
        if doc_name.split('.')[-1] == 'docx':
            self.document.save(doc_name)
        else:
            self.document.save(doc_name + '.docx')


def parse_argument(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv file', type=str,
                        help='please specify file exported from Zentao')
    parser.add_argument('--docx file', type=str, help= ' please specify the docx name')
    return parser.parse_args(argv)


if __name__ == "__main__":
    csv_name = sys.argv[1]
    doc_name = sys.argv[2]
    my_csv = DataCSV(csv_name)
    steps_result = my_csv.operate_file()

    one_record = []

    for item in steps_result:
        one_record.append([item['steps'], ' ', item['expect'], 'Pass', ' '])

    #     print(one_record)
    my_doc = MyDoc()
    header = (
        'Description/Action', 'Specific Data/ Condition(s)', 'Expected Result',
        "Actual Result Pass/Fail", 'Comments')

    for item in one_record:
        #         print(item)
        my_doc.add_paragraph('Test Case')
        my_doc.create_table(header, item)

    my_doc.save_doc(doc_name)

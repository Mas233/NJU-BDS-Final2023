from send_request import *
from const import *
from file_operation import *
import re


def generate_tables():
    i = 1
    for line in read_file(chosen):
        print("Generating table {}...".format(i))
        response = generate_request(requirements+line, davinci_3)
        table1, table2 = resolve_response(response)
        output_files(table+"{}\\".format(i), line, response, table1, table2)
        i += 1


def demo_generate_table():
    for line in read_file(chosen):
        print("Generating table ...")
        response = generate_request(requirements+line, davinci_3)
        table1, table2 = resolve_response(response)
        output_files(table+"demo\\", line, response, table1, table2)
        break


def resolve_response(response):
    table1_content = re.search(r"OVERALL:?(.*?)PLAYERS", response, re.DOTALL)
    if table1_content:
        table1_content = table1_content.group(1).strip()
    table2_content = re.search(r"PLAYERS:?(.*?)$", response, re.DOTALL)
    if table2_content:
        table2_content = table2_content.group(1).strip()
    return table1_content, table2_content


def output_files(path, line, response, table1, table2):
    text_create(path, "src", txt, line)
    text_create(path, "res", txt, response)
    text_create(path, "OVERALL", csv, table1)
    text_create(path, "PLAYERS", csv, table2)


if __name__ == '__main__':
    generate_tables()
    print("Table generation completed!")


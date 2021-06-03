import os
import gzip
import shutil
import pandas as pd
import csv


def unzip_file():
    files_path = [os.path.abspath(x) for x in os.listdir()]
    for path in files_path:
        if(".py" in path):
            continue
        elif(".cm" in path):
            continue
        with os.scandir(path) as entries:
            for entry in entries:
                q = str(entry).split("'")[1]
                full_path = str(path) + "/" + q
                naming = '.'.join(q.split(".")[:-2])
                print("Unzipping "+naming)
                naming = str(path) + "/"+naming
                with gzip.open(full_path, 'rb') as f_in:
                    with open(naming+".txt", 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)


def convert_csv():
    files_path = [os.path.abspath(x) for x in os.listdir()]
    for path in files_path:
        if(".py" in path):
            continue
        elif(".cm" in path):
            continue
        with os.scandir(path) as entries:
            for entry in entries:
                if(".txt" in str(entry)):
                    q = str(entry).split("'")[1]
                    full_path_txt = str(path) + "/" + q
                    full_path_csv = '.'.join(
                        full_path_txt.split(".")[:-1]) + ".csv"
                    print("Converting "+q)
                    with open(full_path_txt, 'r', encoding="ISO-8859-1") as fin:
                        cr = csv.reader(fin, delimiter='\t')
                        filecontents = [line for line in cr]

                    # # write comma-delimited file (comma is the default delimiter)
                    with open(full_path_csv, 'w') as fou:
                        cw = csv.writer(fou, quotechar='', quoting=csv.QUOTE_NONE,
                                        lineterminator='\n', escapechar='\\')
                        cw.writerows(filecontents)


convert_csv()

#! /usr/bin/env python3
# python 2_csv_parsing_and_write.py data/supplier_comma_data.csv data/output/2_comma_output.csv
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        file_reader = csv.reader(csv_in_file, delimiter=',')
        file_writer = csv.writer(csv_out_file, delimiter=',')

        for row_list in file_reader:
            print(row_list)
            file_writer.writerow(row_list)

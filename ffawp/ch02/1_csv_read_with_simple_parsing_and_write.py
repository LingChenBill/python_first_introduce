#! /usr/bin/env python3
# python 1_csv_read_with_simple_parsing_and_write.py data/supplier_data.csv data/output/1_output.csv

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as file_reader:
    with open(output_file, 'w', newline='') as file_writer:
        header = file_reader.readline()
        header = header.strip()
        header_list = header.split(',')
        print(header_list)
        file_writer.write(','.join(map(str, header_list)) + '\n')

        for row in file_reader:
            row = row.strip()
            row_list = row.split(',')
            print(row_list)
            file_writer.write(','.join(map(str, row_list)) + '\n')


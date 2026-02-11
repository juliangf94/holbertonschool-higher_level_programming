#!/usr/bin/env python3
"""
Module for converting CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads a CSV file and converts its content into a JSON file.

    Args:
        csv_filename (str): The name of the source CSV file.

    Returns:
        bool: True if successful, False if an error occurred.
    """
    try:
        data_list = []

        #   Open and read the CSV file
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            #   DictReader transforms each line in a dict automatically
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data_list.append(row)

        #   Write the dict's list in data.json
        #   We can use either mode="w" or "w"
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            #   indent=4 is use for jumps in line and space
            json.dump(data_list, json_file, indent=4)
        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False

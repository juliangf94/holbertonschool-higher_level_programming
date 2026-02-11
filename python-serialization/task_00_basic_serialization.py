#!/usr/bin/env python3
"""
Module for basic serialization.
Provides functions to save a dictionary to a JSON file and load it back.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the output JSON file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file to a Python dictionary.

    Args:
        filename (str): The name of the input JSON file.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

#!/usr/bin/env python3
"""
Module for serializing and deserializing dictionaries using XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into an XML file.

    Args:
        dictionary (dict): The data to serialize.
        filename (str): The name of the output XML file.
    """
    # Create the element <data>
    root = ET.Element("data")

    # Iterates the dict and creates subelements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        #   Manage data type, XML only saves texts
        child.text = str(value)

    # Creates the tree and saves in file
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Reads an XML file and reconstructs the dictionary.

    Args:
        filename (str): The name of the source XML file.

    Returns:
        dict: The reconstructed dictionary.
    """
    try:
        #   Parse the XML file
        tree = ET.parse(filename)
        #   Gives use access to <data>
        root = tree.getroot()

        #   Rebuild the dict from child elements
        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text

        return deserialized_dict

    except FileNotFoundError:
        return None

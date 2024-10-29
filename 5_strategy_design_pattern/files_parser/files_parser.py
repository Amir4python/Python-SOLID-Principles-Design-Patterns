"""
Working with the Strategy Pattern Exercise #2
Exercise: Implement a simple file reader with different file parsers using the Strategy Design Pattern in Python.

Create an interface called FileParser with a single method parse_file that takes a string file_path as
an argument and returns a list of dictionaries.

Implement three different file parsers that inherit from FileParser:

a. CSVParser: This parser reads a CSV file and returns a list of dictionaries, where each dictionary represents a
 row with keys as column names and values as cell contents.

b. JSONParser: This parser reads a JSON file containing an array of objects and returns a list of dictionaries.

c. XMLParser: This parser reads an XML file and returns a list of dictionaries.
Assume that the XML file has a flat structure with a root element containing
multiple child elements of the same type, and each child element has only attributes (no nested elements).

Implement a FileReader class with the following methods:

a. __init__(self, file_parser: FileParser): Initializes a new file reader with a given file parser.

b. read_file(self, file_path: str) -> List[Dict[str, Any]]: Reads the file at the given file path
 and returns a list of dictionaries using the specified file parser.

Test your implementation with different file parsers and sample files in CSV, JSON, and XML formats.
For example, you can create a file reader with a CSVParser, read a sample CSV file, and print the list of dictionaries.

Note: You may need to install additional libraries for working with CSV, JSON, and XML files,
such as the xml.etree.ElementTree module from the Python standard library for XML parsing.

"""
import csv
import json
from abc import ABC, abstractmethod
from typing import List, Dict, Any

import xml.etree.ElementTree as ET


# Step 1: Create the FileParser interface
class FileParser(ABC):

    @abstractmethod
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        pass

    # Step 2: Implement the file parsers
    # TODO: Implement CSVParser, JSONParser, and XMLParser classes
    @abstractmethod
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        pass


# Step 2: Implement the file parsers
class CSVParser(FileParser):
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]


class JSONParser(FileParser):
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        with open(file_path) as jsonfile:
            return json.load(jsonfile)


class XMLParser(FileParser):
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        tree = ET.parse(file_path)
        root = tree.getroot()

        result = []
        for child in root:
            result.append(child.attrib)

        return result


# Step 3: Implement the FileReader class
class FileReader:

    def __init__(self, file_parser: FileParser):
        # TODO: Initialize the file reader with the given file_parser
        self._file_parser = file_parser

    def read_file(self, file_path: str) -> List[Dict[str, Any]]:
        # TODO: Read the file at the given file_path and return a list of dictionaries using the specified file parser
        return self._file_parser.parse_file(file_path)


# TODO: Read the file at the given file_path and return a list of dictionaries using the specified file parser

# Step 4: Test your implementation
if __name__ == "__main__":
    # TODO: Create a file reader with a CSVParser
    reader = FileReader(CSVParser())
    reader = FileReader(JSONParser())
    reader = FileReader(XMLParser())

    # TODO: Read a sample CSV file and print the list of dictionaries
    # data = reader.read_file("sample.csv")
    data = reader.read_file("sample.xml")
    print(data)

#create JSON for given csv

# create JSON for given csv

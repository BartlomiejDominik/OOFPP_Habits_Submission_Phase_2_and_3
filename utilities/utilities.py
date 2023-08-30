import os
import json
from datetime import date, datetime
from utilities.customJSONEncoder import CustomJSONEncoder
import sys


class Utilities:
    # Function for saving databank in json file based on an EncoderClass
    """A utility class for various helper functions related to JSON operations, console manipulation, and date handling.

    This class provides a set of static methods for saving data into JSON files, reading data from JSON files with
    dates, clearing the console screen, and handling logout operations.

    Attributes:
        N/A
    """
    @staticmethod
    def save_into_json_file(data, filename, indent_level=2):
        """Save data into a JSON file using a custom JSON encoder.

        Args:
            data (Any): The data to be saved.
            filename (str): The name of the JSON file.
            indent_level (int, optional): The level of indentation in the JSON file. Default is 2.
        """
        with open(filename, "w") as write_file:
            json.dump(data, write_file, indent=indent_level, cls=CustomJSONEncoder)

    # Function for reading from data with dates from json file
    def read_from_json_file(self, filename):
        """Read data with dates from a JSON file.

        Args:
            filename (str): The name of the JSON file to read from.

        Returns:
            Any: The data read from the JSON file.
        """
        # try:
        with open(filename, "r") as read_file:
            data = json.load(read_file, object_hook=self.date_hook)
            return data

    # Function for converting the data from a json file back to the dates format
    @staticmethod
    def date_hook(obj_dict):
        """Convert date strings in ISO format to date objects during JSON decoding.

        Args:
            obj_dict (dict): The dictionary representing the JSON object.

        Returns:
            dict: The dictionary with date strings converted to date objects.
        """
        for key, value in obj_dict.items():
            if isinstance(value, str):
                try:
                    # Check if the value is in ISO date format and convert it to a date object
                    obj_dict[key] = date.fromisoformat(value)
                except ValueError:
                    pass
        return obj_dict

    @staticmethod
    def clear_console():
        """Clear the console screen based on the operating system."""
        # Check the platform and execute the appropriate clear command
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For Linux and macOS
            os.system('clear')

    @staticmethod
    def log_out(log_out_file):
        """Log out the user and exit the program.

        Args:
            log_out_file (str): The name of the JSON file to store logout information.
        """
        model = Utilities()
        log_out_time = datetime.now().date().isoformat()  # .isoformat() converts date into a string (ISO
        # 8601:"YYYY-MM-DD")
        model.save_into_json_file(log_out_time, log_out_file,
                                  indent_level=4)  # indent specifies number of spaces for each
        # Level of indentation in *.json file. This makes the structure of the file more readable if open separately.
        sys.exit()  # exit the code

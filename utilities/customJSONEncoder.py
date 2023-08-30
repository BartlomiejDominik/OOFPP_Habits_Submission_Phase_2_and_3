# Class based on json bibliothek create to prepare the dates to be saved in json format.
import json
from datetime import date


class CustomJSONEncoder(json.JSONEncoder):
    """A custom JSON encoder that extends the default JSONEncoder to handle date objects.

    This class provides a custom way to encode date objects into JSON format by converting them into ISO 8601 format.

    Attributes:
        N/A
    """
    def default(self, obj):
        """Override the default method to provide custom JSON encoding for date objects.

        Args:
            obj (Any): The object to be encoded.

        Returns:
            str: The encoded JSON representation of the object,
                or the original representation if not applicable.
        """
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)

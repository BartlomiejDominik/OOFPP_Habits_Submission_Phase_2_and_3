# Class based on json bibliothek create to prepare the dates to be saved in json format.
import json
from datetime import date


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)

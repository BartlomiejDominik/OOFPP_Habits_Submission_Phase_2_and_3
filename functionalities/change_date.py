import datetime
import time

from utilities.utilities import Utilities


class ChangeDate:
    """This class is used to change the date of the last logout."""

    @staticmethod
    def change_date(log_out_file):
        """Allows the user to manually set the date of the last log_out for testing purposes.

        Args:
            log_out_file (str): The name of the JSON file to save the new date to.
        """
        model = Utilities()

        while True:
            model.clear_console()
            date_string = input('\nPlease insert the date in the format YYYY-MM-DD or type (b) to go back.\n')
            if date_string == 'b':
                model.clear_console()
                break
            else:

                format_string = "%Y-%m-%d"

                try:
                    current_date = datetime.datetime.now().date()
                    user_date = datetime.datetime.strptime(date_string, format_string).date()

                    if user_date >= current_date:
                        print("The provided date is not earlier than today.")
                        time.sleep(3)
                        pass
                    else:
                        # print("The provided date is earlier than today.")
                        model.save_into_json_file(user_date, log_out_file)
                        model.clear_console()
                        break
                except ValueError:
                    print("Date string does not have the correct format.")
                    time.sleep(1)

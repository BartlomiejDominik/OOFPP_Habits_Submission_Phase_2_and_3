from datetime import datetime


class StreakRunDaily:

    @staticmethod
    def calculate_longest_streak(habits):
        """Calculate the longest streak of completed habits.

        Args:
            habits (list): List of habit dictionaries.

        Returns:
            tuple: A tuple containing the longest streak length, start date, and end date of the streak.
        """

        print('\nPeriodicity: daily\n')
        for i, habit in enumerate(habits):
            list_of_dates = habit[6]  # Assuming the index of 'Check_offs' is 6 in the habit tuple

            # Convert strings to datetime objects (ignoring time)
            date_objects = [datetime.strptime(date_str[:10], "%Y-%m-%d") for date_str in list_of_dates]

            streaks = []
            current_streak = []
            for j in range(len(date_objects) - 1):
                if (date_objects[j + 1] - date_objects[j]).days <= 1:
                    if not current_streak:
                        current_streak.append(date_objects[j])
                    current_streak.append(date_objects[j + 1])
                else:
                    if len(current_streak) >= 2:
                        streaks.append(current_streak)
                    current_streak = []  # Reset current_streak regardless of length

            if current_streak:
                streaks.append(current_streak)  # Append any remaining streak

            # Find the longest streak for this habit
            longest_streak = max(streaks, key=len) if streaks else []

            # Calculate the length of the longest streak
            longest_streak_length = len(longest_streak)

            # Calculate minimum and maximum dates of the longest streak
            longest_streak_min_date = min(longest_streak).strftime("%Y-%m-%d") if longest_streak else None
            longest_streak_max_date = max(longest_streak).strftime("%Y-%m-%d") if longest_streak else None

            # Print results for this habit

            print(
                f"{i + 1}. {habits[i][1]}, Longest streak: {longest_streak_length} days (from {longest_streak_min_date}"
                f" to {longest_streak_max_date})")


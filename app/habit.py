from __future__ import annotations
import os
import datetime
from typing import List
import questionary

class Habit:
    """
    A class representing a habit to be tracked.

    Attributes:
        name (str): The name of the habit.
        description (str): A brief description of the habit.
        periodicity (int): The frequency at which the habit should be performed, in days.
        times_completed (int): The number of times the habit has been completed.
        last_completed (datetime.date): The date on which the habit was last completed.
        current_streak (int): The current streak of consecutive days on which the habit was completed.
        best_streak (int): The best streak of consecutive days on which the habit was completed.

    Constants:
        DAILY (int): periodicity = 1.
        WEEKLY (int): periodicity = 7.
        MONTHLY (int): periodicity = 30.


    Methods:
        track(): Tracks the completion of the habit for the current day.
        get_progress(): Calculates and returns the progress of the habit in percentage.
        get_streaks(): Returns the current and best streaks of the habit.
        __str__(): Returns a string representation of the habit object.
        doesExit(habit): Returns True if a habit name match is found in the database file
        save(): Saves the current instance of the `Habit` class to a text file specified by `file_name`.
        remove(): Removes the data of the habit from the file
        remove_duplicates(): Removes the duplicate data from the file
        update(newHabit, oldHabit): Updates the contents of the habit written to the file
        load_default_data(): loads the predefined data to the file
        clear_all_data(): clears all habits data
    """

    DAILY = 1
    WEEKLY = 7
    MONTHLY = 30

    def __init__(self, name: str, description: str, periodicity: int):
        """
        Initializes a new instance of the Habit class.

        Args:
            name (str): The name of the habit.
            description (str): A brief description of the habit.
            periodicity (int): The frequency at which the habit should be performed, in days.
        """
        self.name = name
        self.description = description
        self.periodicity = periodicity
        self.times_completed = 0
        self.last_completed = None
        self.current_streak = 0
        self.best_streak = 0

    def track(self):
        """
        Tracks the completion of the habit for the current day.
        """
        self.times_completed = int(self.times_completed)+1
        today = datetime.date.today()
        if self.last_completed is None or self.last_completed < today:
            self.current_streak = 1
        else:
            self.current_streak += 1
        self.last_completed = today
        if self.current_streak >= self.best_streak:
            self.best_streak = self.current_streak


    def get_progress(self) -> float:
        """
        Calculates and returns the progress of the habit in percentage.

        Returns:
            float: The percentage progress of the habit.
        """
        if self.times_completed == 0:
            return 0
        else:
            return self.times_completed / self.periodicity * 100

    def get_streaks(self) -> tuple:
        """
        Returns the current and best streaks of the habit.

        Returns:
            tuple: A tuple containing the current and best streaks of the habit.
        """
        return self.current_streak, self.best_streak

    def __str__(self) -> str:
        """
        Returns a string representation of the habit object.

        Returns:
            str: The string representation of the habit object.
        """
        if self.last_completed is not None:
            last_completed_str = self.last_completed.strftime('%Y-%m-%d')
        else:
            last_completed_str = ''
        return f"{self.name},{self.description},{self.periodicity},{self.times_completed},{last_completed_str},{self.current_streak},{self.best_streak}\n"

    @staticmethod
    def doesExist(habit: Habit, file_name: str = "habit_tracker_database.txt") -> bool:
        """
        Searches a text file and compares the first comma-separated value in each line of the file with
        the name attribute of a Habit object. If there is a match, returns True, else returns False.

        Args:
            habit (Habit): The Habit object to compare with the first value in each line of the file.
            file_name (str): The name of the text file to search.

        Returns:
            bool: True if there is a match between the first value in a line of the text file and the
            name attribute of the habit object, else False.
        """
        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                for line in f:
                    if line.strip().split(',')[0] == habit.name:
                        return True
        return False
    
    def save(self, file_name: str = "habit_tracker_database.txt") -> None:
        """
        Saves the current instance of the `Habit` class to a text file specified by `file_name`.
        If the habit already exists in the file, it will not be saved again.

        Args:
            file_name (str): The name of the file to save the instance to.

        Returns:
            None. The method only saves the instance to a file.
        """
        exists = os.path.exists(file_name)
        with open(file_name, "a" if exists else "w") as f:
            if Habit.doesExist(self, file_name):
                # If the habit already exists in the file, do not save it again
                return
            last_completed_str = self.last_completed.strftime('%Y-%m-%d') if self.last_completed else ""
            f.write(f"{self.name},{self.description},{self.periodicity},{self.times_completed},{last_completed_str},{self.current_streak},{self.best_streak}\n")

    def remove(self, file_name: str="habit_tracker_database.txt") -> None:
        """
        Removes all lines in the specified file that have the same habit name as the current instance of the `Habit` class.

        Args:
            file_name (str): The name of the file to remove the lines from.

        Returns:
            None. The method only removes the lines from the file.
        """
        # Open the file and read all the lines into a list
        with open(file_name, 'r') as f:
            lines = f.readlines()
        # Remove duplicates and keep the order of the lines
        unique_lines = []
        for line in lines:
            habit_name = line.strip().split(',')[0]
            if habit_name != self.name:
                unique_lines.append(line)
        # Write the unique lines back to the file
        with open(file_name, 'w') as f:
            f.writelines(unique_lines)

    @staticmethod
    def remove_duplicates(file_name: str="habit_tracker_database.txt") -> None:
        """
        Removes duplicate entries in a file that contains habits data.

        Args:
            file_name (str): The name of the file to remove duplicates from. Defaults to "habit_tracker_database.txt".

        Returns:
            None. The method only modifies the specified file by removing duplicate lines.
        """
        # Open the file and read all the lines into a list
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                lines = f.readlines()
            # Remove duplicates and keep the order of the lines
            unique_lines = []
            unique_habit_names = []
            for line in lines:
                habit1_name = line.strip().split(',')[0]
                if habit1_name not in unique_habit_names:
                    unique_lines.append(line)
                    unique_habit_names.append(habit1_name)
            # Write the unique lines back to the file
            with open(file_name, 'w') as f:
                f.writelines(unique_lines)

    @staticmethod
    def update(new_habit_data: Habit, old_habit_data: Habit, file_name: str = "habit_tracker_database.txt") -> bool:
        """
        Updates the data for a habit in the habit tracker database file.

        Args:
            new_habit_data (Habit): The updated data for the habit.
            old_habit_data (Habit): The original data for the habit to be updated.
            file_name (str, optional): The name of the file to update. Defaults to "habit_tracker_database.txt".

        Returns:
            bool: True if the habit was found and updated, False otherwise.
        """
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                lines = f.readlines()
            match_found = False
            for i, line in enumerate(lines):
                line_data = line.strip().split(",")
                if line_data[0] == old_habit_data.name:
                    lines[i] = str(new_habit_data)
                    match_found = True
            if not match_found:
                return False
            with open(file_name, 'w') as f:
                f.writelines(lines)
            Habit.remove_duplicates()
            return True
        else:
            return False
    
    @staticmethod
    def clear_all_data(file_name: str="habit_tracker_database.txt"):
        """
        Clears all application data
        """
        if os.path.exists(file_name):
            with open(file_name, "w") as file:
                file.truncate()
    
    @staticmethod
    def load_default_data(file_name: str = "habit_tracker_database.txt"):
        """
        Loads the application with a set of predefined habits
        """
        habits_data = [
            ["Get up early", "Get working when the world is asleep", Habit.DAILY, 0, None, 0, 0],
            ["Brush your teeth", "Health is wealth", Habit.DAILY, 2, datetime.date(2023, 5, 2), 2, 2],
            ["2 hours study", "Study helps grow", Habit.DAILY, 2, datetime.date(2023, 5, 2), 2, 2],
            ["Family Time", "Live the moments fully with family", Habit.WEEKLY, 1, datetime.date(2023, 5, 1), 1, 1],
            ["Next Month Planning", "Planning makes success more certain", Habit.MONTHLY, 0, None, 0, 0]
        ]
        available_data = []
        available_names = []
        i = 0
        for data in habits_data:
            if Habit.doesExist(Habit(data[0], "", 1)) == False:
                available_data.append(data)
                available_names.append(data[0])
            i = i+1
        available_names.append("Back")
        choice = questionary.select("Choose an option to load the data:", choices=available_names).ask()
        for data in available_data:
            if choice == data[0]:
                habit = Habit(data[0], data[1], data[2])
                habit.times_completed = data[3]
                habit.last_completed = data[4]
                habit.current_streak = data[5]
                habit.best_streak = data[6]
                habit.save()
                input("Predefined data loaded successfully!\nPress Enter to continue!")
                return
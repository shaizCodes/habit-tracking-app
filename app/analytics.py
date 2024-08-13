import os
from app.habit import Habit

class Analytics:
    """
    This class is used to print the data.

    Methods:
        show_all_habits(): it prints all the data in tabular form.
        show_best_streak_habit(): it prints the last habit that has the best steak in a tabular form.
        show_most_completed_habit(): it prints the last most completed habit in a tabular form.
    """
    @staticmethod
    def show_all_habits():
        """
        Prints all the data in tabular form.
        """
        habits = []
        habit_names = []
        if os.path.exists("habit_tracker_database.txt"):
            highest_name_length = 0
            highest_description_length = 0
            highest_periodicity_length = 11
            highest_times_completed_length = 15
            highest_last_completed_length = 14
            highest_current_streak_length = 14
            highest_best_streak_length = 11
            formatted_line = ""
            with open("habit_tracker_database.txt", "r") as f:
                for line in f:
                    line = line.replace("\n", "")
                    habits.append(line)
                    habit_names.append(line.strip().split(',')[0])
                    length = len(line.strip().split(',')[0])
                    highest_name_length = length if highest_name_length < length else highest_name_length
                    length = len(line.strip().split(',')[1])
                    highest_description_length = length if highest_description_length < length else highest_description_length
                    length = len(line.strip().split(',')[2])
                    highest_periodicity_length = length if highest_periodicity_length < length else highest_periodicity_length
                    length = len(line.strip().split(',')[3])
                    highest_times_completed_length = length if highest_times_completed_length < length else highest_times_completed_length
                    length = len(line.strip().split(',')[4])
                    highest_last_completed_length = length if highest_last_completed_length < length else highest_last_completed_length
                    length = len(line.strip().split(',')[5])
                    highest_current_streak_length = length if highest_current_streak_length < length else highest_current_streak_length
                    length = len(line.strip().split(',')[6])
                    highest_best_streak_length = length if highest_best_streak_length < length else highest_best_streak_length
                length = 2+highest_name_length+3+highest_description_length+3+highest_periodicity_length+3+highest_times_completed_length+3+highest_last_completed_length+3+highest_current_streak_length+3+highest_best_streak_length+3
                formatted_line = "-".center(length, "-")+"\n"
                formatted_line += "| "+("NAME".center(highest_name_length, " "))
                formatted_line += " | "+("DESCRIPTION".center(highest_description_length, " "))
                formatted_line += " | "+("PERIODICITY".center(highest_periodicity_length, " "))
                formatted_line += " | TIMES COMPLETED"
                formatted_line += " | "+("LAST COMPLETED".center(highest_last_completed_length, " "))
                formatted_line += " | CURRENT STREAK | BEST STREAK |\n"
                formatted_line += "-".center(length, "-")+"\n"
                for habit in habits:
                    habit_name = habit.strip().split(',')[0]
                    habit_description = habit.strip().split(',')[1]
                    habit_periodicity = habit.strip().split(',')[2]
                    habit_times_completed = habit.strip().split(',')[3]
                    habit_last_completed = habit.strip().split(',')[4]
                    habit_current_streak = habit.strip().split(',')[5]
                    habit_best_streak = habit.strip().split(',')[6]
                    if habit_periodicity == str(Habit.DAILY):
                        habit_periodicity = "DAILY"
                    elif habit_periodicity == str(Habit.WEEKLY):
                        habit_periodicity = "WEEKLY"
                    elif habit_periodicity == str(Habit.MONTHLY):
                        habit_periodicity = "MONTHLY"
                    else:
                        habit_periodicity = "Every "+str(habit_periodicity)+" day"
                    habit_last_completed = "None" if habit_last_completed == "" else habit_last_completed
                    line = "|"+(habit_name.center(highest_name_length+2, " "))+"| "+(habit_description.center(highest_description_length, " "))+" | "+(habit_periodicity.center(highest_periodicity_length, " "))+" | "+(habit_times_completed.center(highest_times_completed_length, " "))+" | "+(habit_last_completed.center(highest_last_completed_length, " "))+" | "+(habit_current_streak.center(highest_current_streak_length, " "))+" | "+(habit_best_streak.center(highest_best_streak_length, " "))+" |\n"
                    formatted_line += line
                    formatted_line += "-".center(length, "-")+"\n"
                print(formatted_line)
    
    @staticmethod
    def show_best_streak_habit():
        """
        Prints the last habit that has the best steak in a tabular form.
        """
        if os.path.exists("habit_tracker_database.txt"):
            habit_name = ""
            habit_description = ""
            habit_periodicity = ""
            habit_times_completed = ""
            habit_last_completed = ""
            habit_current_streak = ""
            habit_best_streak = ""
            highest_name_length = 0
            highest_description_length = 0
            highest_periodicity_length = 11
            highest_times_completed_length = 15
            highest_last_completed_length = 14
            highest_current_streak_length = 14
            highest_best_streak_length = 11
            formatted_line = ""
            best_streak = 0
            with open("habit_tracker_database.txt", "r") as f:
                for line in f:
                    if best_streak <= int(line.strip().split(',')[6]):
                        best_streak = int(line.strip().split(",")[6])
                        habit_name = line.strip().split(',')[0]
                        highest_name_length = len(habit_name)
                        habit_description = line.strip().split(',')[1]
                        highest_description_length = len(habit_description)
                        habit_periodicity = line.strip().split(',')[2]
                        if habit_periodicity == str(Habit.DAILY):
                            habit_periodicity = "DAILY"
                        elif habit_periodicity == str(Habit.WEEKLY):
                            habit_periodicity = "WEEKLY"
                        elif habit_periodicity == str(Habit.MONTHLY):
                            habit_periodicity = "MONTHLY"
                        else:
                            habit_periodicity = "Every "+str(habit_periodicity)+" day"
                        habit_times_completed = line.strip().split(',')[3]
                        habit_last_completed = line.strip().split(',')[4]
                        habit_last_completed = "None" if habit_last_completed == "" else habit_last_completed
                        habit_current_streak = line.strip().split(',')[5]
                        habit_best_streak = line.strip().split(',')[6]
                length = 2+highest_name_length+3+highest_description_length+3+highest_periodicity_length+3+highest_times_completed_length+3+highest_last_completed_length+3+highest_current_streak_length+3+highest_best_streak_length+3
                formatted_line = "-".center(length, "-")+"\n"
                formatted_line += "| "+("NAME".center(highest_name_length, " "))
                formatted_line += " | "+("DESCRIPTION".center(highest_description_length, " "))
                formatted_line += " | "+("PERIODICITY".center(highest_periodicity_length, " "))
                formatted_line += " | TIMES COMPLETED"
                formatted_line += " | "+("LAST COMPLETED".center(highest_last_completed_length, " "))
                formatted_line += " | CURRENT STREAK | BEST STREAK |\n"
                formatted_line += "-".center(length, "-")+"\n"
                formatted_line += "|"+(habit_name.center(highest_name_length+2, " "))+"| "+(habit_description.center(highest_description_length, " "))+" | "+(habit_periodicity.center(highest_periodicity_length, " "))+" | "+(habit_times_completed.center(highest_times_completed_length, " "))+" | "+(habit_last_completed.center(highest_last_completed_length, " "))+" | "+(habit_current_streak.center(highest_current_streak_length, " "))+" | "+(habit_best_streak.center(highest_best_streak_length, " "))+" |\n"
                formatted_line += "-".center(length, "-")+"\n"
                print(formatted_line)

    @staticmethod
    def show_most_completed_habit():
        """
        Prints the last most completed habit in a tabular form.
        """
        if os.path.exists("habit_tracker_database.txt"):
            habit_name = ""
            habit_description = ""
            habit_periodicity = ""
            habit_times_completed = ""
            habit_last_completed = ""
            habit_current_streak = ""
            habit_best_streak = ""
            highest_name_length = 0
            highest_description_length = 0
            highest_periodicity_length = 11
            highest_times_completed_length = 15
            highest_last_completed_length = 14
            highest_current_streak_length = 14
            highest_best_streak_length = 11
            formatted_line = ""
            best_streak = 0
            with open("habit_tracker_database.txt", "r") as f:
                for line in f:
                    if best_streak <= int(line.strip().split(',')[5]):
                        best_streak = int(line.strip().split(",")[6])
                        habit_name = line.strip().split(',')[0]
                        highest_name_length = len(habit_name)
                        habit_description = line.strip().split(',')[1]
                        highest_description_length = len(habit_description)
                        habit_periodicity = line.strip().split(',')[2]
                        if habit_periodicity == str(Habit.DAILY):
                            habit_periodicity = "DAILY"
                        elif habit_periodicity == str(Habit.WEEKLY):
                            habit_periodicity = "WEEKLY"
                        elif habit_periodicity == str(Habit.MONTHLY):
                            habit_periodicity = "MONTHLY"
                        else:
                            habit_periodicity = "Every "+str(habit_periodicity)+" day"
                        habit_times_completed = line.strip().split(',')[3]
                        habit_last_completed = line.strip().split(',')[4]
                        habit_last_completed = "None" if habit_last_completed == "" else habit_last_completed
                        habit_current_streak = line.strip().split(',')[5]
                        habit_best_streak = line.strip().split(',')[6]
                length = 2+highest_name_length+3+highest_description_length+3+highest_periodicity_length+3+highest_times_completed_length+3+highest_last_completed_length+3+highest_current_streak_length+3+highest_best_streak_length+3
                formatted_line = "-".center(length, "-")+"\n"
                formatted_line += "| "+("NAME".center(highest_name_length, " "))
                formatted_line += " | "+("DESCRIPTION".center(highest_description_length, " "))
                formatted_line += " | "+("PERIODICITY".center(highest_periodicity_length, " "))
                formatted_line += " | TIMES COMPLETED"
                formatted_line += " | "+("LAST COMPLETED".center(highest_last_completed_length, " "))
                formatted_line += " | CURRENT STREAK | BEST STREAK |\n"
                formatted_line += "-".center(length, "-")+"\n"
                formatted_line += "|"+(habit_name.center(highest_name_length+2, " "))+"| "+(habit_description.center(highest_description_length, " "))+" | "+(habit_periodicity.center(highest_periodicity_length, " "))+" | "+(habit_times_completed.center(highest_times_completed_length, " "))+" | "+(habit_last_completed.center(highest_last_completed_length, " "))+" | "+(habit_current_streak.center(highest_current_streak_length, " "))+" | "+(habit_best_streak.center(highest_best_streak_length, " "))+" |\n"
                formatted_line += "-".center(length, "-")+"\n"
                print(formatted_line)
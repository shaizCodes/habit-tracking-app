import questionary
from app.habit import Habit
import os
from app.analytics import Analytics
import datetime

def print_header():
    print("-".center(70, "-"))
    print(" Habit Tracker ".center(70, "="))
    print("-".center(70, "-"))

while True:
    os.system("cls")
    print_header()
    choices = (["Create a new Habit", "Search an existing Habit", "Update an existing Habit", "Delete a habit", "Analyze the habits", "Clear all the data", "Quit the application"])
    choice = questionary.select("Choose an option from the following:", choices=choices).ask()
    os.system("cls")
    print_header()
    if choice == choices[0]:
        # CREATE
        choices = (["Create a DAILY habit", "Create a WEEKLY habit", "Create a MONTHLY habit", "Load Predefined Data to the application", "Back to main menu"])
        choice = questionary.select("Choose an option from the following:", choices=choices).ask()
        os.system("cls")
        print_header()
        habit_periodicity = Habit.DAILY
        if choice == choices[0]:
            habit_periodicity = Habit.DAILY
        elif choice == choices[1]:
            habit_periodicity = Habit.WEEKLY
        elif choice == choices[2]:
            habit_periodicity = Habit.MONTHLY
        elif choice == choices[3]:
            Habit.load_default_data()
            continue
        else:
            continue
        habit_name = questionary.text(
            "Write the name of your habit*:",
            validate=lambda text: True if len(text) > 0
            else "Please insert a name for your habit.").ask()
        habit_description = ""
        if habit_name is not None:
            habit_description = questionary.text(
                    "Write the description [optional]:").ask()
        habit = Habit(habit_name, habit_description, habit_periodicity)
        habit.save()
        print("The data has been successfully written to the database.")
        input("Press Enter to continue!")
        continue
    elif choice == choices[1]:
        # SEARCH
        habit_name = questionary.text(
            "Write the name of the habit to search*:",
            validate=lambda text: True if len(text) > 0
            else "Please insert a name for your habit.").ask()
        if Habit.doesExist(Habit(habit_name, "", Habit.DAILY)):
            print("SEARCH FOUND!")
            if os.path.exists("habit_tracker_database.txt"):
                with open("habit_tracker_database.txt", "r") as f:
                    for line in f:
                        if line.strip().split(',')[0] == habit_name:
                            line = line.replace("\n", "")
                            habit_description = line.strip().split(',')[1]
                            habit_periodicity = line.strip().split(',')[2]
                            habit_times_completed = line.strip().split(',')[3]
                            habit_last_completed = line.strip().split(',')[4]
                            habit_current_streak = line.strip().split(',')[5]
                            habit_best_streak = line.strip().split(',')[6]
                            if habit_periodicity == str(Habit.DAILY):
                                habit_periodicity = "DAILY"
                            elif habit_periodicity == str(Habit.WEEKLY):
                                habit_periodicity = "WEEKLY"
                            elif habit_periodicity == str(Habit.MONTHLY):
                                habit_periodicity = "MONTHLY"
                            else:
                                habit_periodicity = "Every "+str(habit_periodicity)+" day"
                            name_length = 6
                            if name_length < len(habit_name):
                                name_length = len(habit_name)
                            description_length = 13
                            if description_length < len(habit_description):
                                description_length = len(habit_description)
                            periodicity_length = 11
                            times_completed_length = 15
                            current_streak_length = 14
                            best_streak_length = 11
                            last_completed_length = 14
                            if last_completed_length < len(habit_last_completed):
                                last_completed_length = len(habit_last_completed)
                            habit_last_completed = "None" if habit_last_completed == "" else habit_last_completed
                            line = "|"+(habit_name.center(name_length+2, " "))+"| "+(habit_description.center(description_length, " "))+" | "+(habit_periodicity.center(periodicity_length, " "))+" | "+(habit_times_completed.center(times_completed_length, " "))+" | "+(habit_last_completed.center(last_completed_length, " "))+" | "+(habit_current_streak.center(current_streak_length, " "))+" | "+(habit_best_streak.center(best_streak_length, " "))+" |\n"
                            line = line.replace(",", " | ")
                            length = len(line)
                            formatted_line = "-".center(length, "-")+"\n"
                            formatted_line += "| "+("NAME".center(len(habit_name), " "))
                            formatted_line += " | "+("DESCRIPTION".center(description_length, " "))
                            formatted_line += " | "+("PERIODICITY".center(periodicity_length))
                            formatted_line += " | TIMES COMPLETED"
                            formatted_line += " | "+("LAST COMPLETED".center(last_completed_length))
                            formatted_line += " | CURRENT STREAK | BEST STREAK |\n"
                            formatted_line += "-".center(length, "-")+"\n"
                            formatted_line += line
                            formatted_line += "-".center(length, "-")
                            print(formatted_line)
                            input("Press Enter to continue!")
                            continue
        else:
            print("No Search Found!")
            input("Press enter to continue!")
            continue
    elif choice == choices[2]:
        # UPDATE
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
                habit_names.append("Back")
                other_choices = ["Track/Complete", "Edit the contents", "Back"]
                choice = questionary.select("\nSelect the update operation: ", choices=other_choices).ask()
                if choice == other_choices[0]:
                    choice = questionary.select("\nSelect the habit you want to update: ", choices=habit_names).ask()
                    for habit in habits:
                        if choice == "Back":
                            break
                        elif choice == habit.strip().split(",")[0]:
                            oldHabit = Habit(habit.strip().split(",")[0], habit.strip().split(",")[1], int(habit.strip().split(",")[2]))
                            oldHabit.times_completed = int(habit.strip().split(",")[3])
                            if len(habit.strip().split(",")[4]) > 0:
                                year = int(habit.strip().split(",")[4].split("-")[0])
                                month = int(habit.strip().split(",")[4].split("-")[1])
                                day = int(habit.strip().split(",")[4].split("-")[2])
                                oldHabit.last_completed = datetime.date(year, month, day)
                            oldHabit.current_streak = int(habit.strip().split(",")[5])
                            oldHabit.best_streak = int(habit.strip().split(",")[6])
                            oldHabit.track()
                            Habit.update(oldHabit, oldHabit)
                            break
                    input("Habit tracked/completed successfully!\nPress Enter to continue...")
                    continue
                choice = questionary.select("\nSelect the habit you want to update: ", choices=habit_names).ask()
                os.system("cls")
                print_header()
                for habit in habits:
                    if choice == "Back":
                        continue
                    elif choice == habit.strip().split(",")[0]:
                        oldHabit = Habit(habit.strip().split(",")[0], habit.strip().split(",")[1], int(habit.strip().split(",")[2]))
                        oldHabit.times_completed = int(habit.strip().split(",")[3])
                        if len(habit.strip().split(",")[4]) > 0:
                                year = int(habit.strip().split(",")[4].split("-")[0])
                                month = int(habit.strip().split(",")[4].split("-")[1])
                                day = int(habit.strip().split(",")[4].split("-")[2])
                                oldHabit.last_completed = datetime.date(year, month, day)
                        oldHabit.current_streak = int(habit.strip().split(",")[5])
                        oldHabit.best_streak = int(habit.strip().split(",")[6])
                        newHabit_name = questionary.text(
                            "Write the name of your habit*:",
                            validate=lambda text: True if len(text) > 0
                            else "Please insert a name for your habit.").ask()
                        newHabit_description = questionary.text("Write the description of your habit[optional]: ").ask()
                        newHabit_periodicity = questionary.text(
                            "Write the periodicity of your habit*:",
                            validate=lambda text: True if text=="1" or text=="7" or text=="30"
                            else "Please insert 1 for daily, 7 for weekly and 30 for monthly.").ask()
                        newHabit = Habit(newHabit_name, newHabit_description, newHabit_periodicity)
                        newHabit.times_completed = oldHabit.times_completed
                        newHabit.last_completed = oldHabit.last_completed
                        newHabit.current_streak = oldHabit.current_streak
                        newHabit.best_streak = oldHabit.best_streak
                        Habit.update(newHabit, oldHabit)
                        print("The data has been updated.")
                        input("Press Enter to continue!")
                        continue
        else:
            questionary.print("No data found! Kindly create habits first!")
            input("Press Enter to continue!")
        continue
    elif choice == choices[3]:
        # DELETE
        os.system("cls")
        print_header()
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
                habit_names.append("Back")
                choice = questionary.select("\nSelect the habit you want to update: ", choices=habit_names).ask()
                for habit in habits:
                    if choice == "Back":
                        continue
                    elif choice == habit.strip().split(",")[0]:
                        oldHabit = Habit(habit.strip().split(",")[0], habit.strip().split(",")[1], habit.strip().split(",")[2])
                        oldHabit.remove()
                        print("The data has been successfully deleted.")
                        input("Press Enter to continue!")
                        continue
        else:
            questionary.print("No data found! Kindly create habits first!")
            input("Press Enter to continue!")
            continue
    elif choice == choices[4]:
        # ANALYZE
        choices = ["Show all habits", "Show the habit with best streak", "Show the most completed habit", "Back"]
        choice = questionary.select("\nSelect the habit you want to update: ", choices=choices).ask()
        if choice == choices[0]:
            Analytics.show_all_habits()
            input("Press Enter to continue!")
        elif choice == choices[1]:
            Analytics.show_best_streak_habit()
            input("Press Enter to continue!")
        elif choice == choices[2]:
            Analytics.show_most_completed_habit()
            input("Press Enter to continue!")
        elif choice == choices[3]:
            continue
    elif choice == choices[5]:
        Habit.clear_all_data()
        input("All data has been cleared!\nPress Enter to continue!")
    elif choice == choices[6]:
        # QUIT
        print("Thanks for using the application!")
        exit(1)

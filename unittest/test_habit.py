import os
_relative_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys
sys.path.append(_relative_path)
from app.habit import Habit
import unittest
import datetime
import tempfile

class TestHabit(unittest.TestCase):
    def setUp(self):
        self.habit = Habit('Exercise', '30 min workout', Habit.DAILY)
        self.habit.save("test_habit_tracker_database.txt")

    def test_track(self):
        self.habit.track()
        self.assertEqual(self.habit.times_completed, 1)
        self.assertEqual(self.habit.current_streak, 1)

    def test_get_progress(self):
        self.habit.times_completed = 5
        progress = self.habit.get_progress()
        self.assertEqual(progress, 500)

    def test_get_streaks(self):
        self.habit.current_streak = 3
        self.habit.best_streak = 5
        streaks = self.habit.get_streaks()
        self.assertEqual(streaks, (3, 5))

    def test_str(self):
        habit_str = str(self.habit)
        self.assertEqual(habit_str, 'Exercise,30 min workout,1,0,,0,0\n')

    def test_doesExist(self):
        if os.path.exists("test_habit_tracker_database.txt"):
            with open("test_habit_tracker_database.txt", "w") as f:
                f.write("Exercise,30 min workout,1,0,,0,0\n")
            self.assertTrue(Habit.doesExist(self.habit, "test_habit_tracker_database.txt"))
        else:
            self.assertFalse(Habit.doesExist(Habit('Meditation', '10 min meditation', Habit.DAILY)))
    

    def test_save_new_habit_to_file(self):
        # create a new habit instance
        habit = Habit("Drink Water", "Drink at least 8 glasses of water per day", Habit.DAILY)
        # save the habit to a file
        habit.save("test_habit_tracker_database.txt")
        # check if file exists and habit is saved correctly
        self.assertTrue(os.path.exists("test_habit_tracker_database.txt"))
        with open("test_habit_tracker_database.txt", "r") as f:
            lines = f.readlines()
            self.assertIn("Drink Water,Drink at least 8 glasses of water per day,1,0,,0,0\n", lines)
        # clean up the file
        os.remove("test_habit_tracker_database.txt")

    def test_save_existing_habit_to_file(self):
        with open("test_habit_tracker_database.txt", "r+") as f:
            f.truncate()
        # create a new habit instance and save it to a file
        habit1 = Habit("Drink Water", "Drink at least 8 glasses of water per day", Habit.DAILY)
        habit1.save("test_habit_tracker_database.txt")
        # create another habit instance with the same name
        habit2 = Habit("Drink Water", "Drink more water", Habit.DAILY)
        # try to save the new habit instance to the same file
        habit2.save("test_habit_tracker_database.txt")
        # check if file still has only one instance of the habit
        with open("test_habit_tracker_database.txt", "r") as f:
            lines = f.readlines()
            self.assertEqual(1, len(lines))
            self.assertIn("Drink Water,Drink at least 8 glasses of water per day,1,0,,0,0\n", lines)
        # clean up the file
        os.remove("test_habit_tracker_database.txt")

    def test_remove(self):
        # Create a temporary file with some sample data
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f:
            f.write("habit1,description1,7,2,2022-04-28,2,2\n")
            f.write("habit2,description2,1,3,2022-04-29,3,3\n")
            f.write("habit3,description3,30,4,,4,4\n")
            f.write("habit1,description4,7,5,2022-04-27,5,5\n")
        # Create a Habit object to remove
        habit = Habit("habit1", "description1", Habit.WEEKLY)
        habit.times_completed = 2
        habit.last_completed = datetime.date(2022, 4, 28)
        habit.current_streak = 2
        habit.best_streak = 2
        # Call the remove method
        habit.remove(f.name)
        # Verify that the lines corresponding to the habit have been removed
        with open(f.name, 'r') as f:
            lines = f.readlines()
        assert len(lines) == 2
        assert lines[0] == "habit2,description2,1,3,2022-04-29,3,3\n"
        assert lines[1] == "habit3,description3,30,4,,4,4\n"
        # Delete the temporary file
        os.unlink(f.name)

    def test_remove_duplicates(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmpfile:
            tmpfile.write("Test Habit 1,A test habit.,7,0,,0,0\n")
            tmpfile.write("Test Habit 2,Another test habit.,3,0,,0,0\n")
            tmpfile.write("Test Habit 1,A test habit.,7,0,,0,0\n")
            tmpfile.write("Test Habit 2,Another test habit.,3,0,,0,0\n")
        Habit.remove_duplicates(tmpfile.name)
        with open(tmpfile.name, 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 2)
            self.assertEqual(lines[0].strip(), "Test Habit 1,A test habit.,7,0,,0,0")
            self.assertEqual(lines[1].strip(), "Test Habit 2,Another test habit.,3,0,,0,0")
        os.remove(tmpfile.name)

    def test_update(self):
        with open("test_habit_tracker_database.txt", "r+") as f:
            f.truncate()
        # create a habit to update
        old_habit_data = Habit("Drink water", "Drink 8 glasses of water daily", Habit.WEEKLY)
        old_habit_data.times_completed = 0
        old_habit_data.last_completed = None
        old_habit_data.current_streak = 0
        old_habit_data.best_streak = 0
        # add the habit to the file
        old_habit_data.save("test_habit_tracker_database.txt")
        # create an updated habit
        new_habit_data = Habit("Drink water", "Drink 8 glasses of water daily", Habit.DAILY)
        new_habit_data.times_completed = 1
        new_habit_data.last_completed = datetime.date(2023, 4, 30)
        new_habit_data.current_streak = 1
        new_habit_data.best_streak = 1
        # update the habit in the file
        assert Habit.update(new_habit_data, old_habit_data, "test_habit_tracker_database.txt") == True
        # check that the habit was updated
        with open("test_habit_tracker_database.txt", "r") as f:
            # print(f.readlines())
            assert "Drink water,Drink 8 glasses of water daily,1,1,2023-04-30,1,1\n" in f.readlines()

    def tearDown(self):
        if os.path.exists("test_habit_tracker_database.txt"):
            os.remove("test_habit_tracker_database.txt")


if __name__ == "__main__":
    unittest.main()
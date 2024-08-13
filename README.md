# Habit Tracking Application

## Installation

### Prepare your environment for the use of the Application

For stable usage of the application, **python version 3.10.4** is recommended. Install python from the [official website](https://www.python.org/). Check your python version with entering your command promt and execute the following command:

```python
python --version 
```

It is recommended to use a customized environment to ensure full functionality, e.g. with the distribution anaconda, which can be downloaded [here](https://www.anaconda.com/products/distribution).

Install the required packages with the following command in your command line interface (For more information about pip, please check the [pip documentation](https://pip.pypa.io/en/latest/user_guide/)):

```python
pip install -r requirements.txt 
```

&nbsp;

## Use of the Application

First download the code by either downloading the .zip-File or clone it via the command promt. For more information about the later please check the [github docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

To run the application, either open the project with a python-IDE and run the file *main.py* or enter the following in the command prompt:

```python
python main.py 
```

Or simply install the VS Code along with Python extensions and open the main.py then click on the play button that is at the top right corner of the screen on the top ribbon.

&nbsp;

## Introduction to the Menu

After following the steps above, you should be greeted with the following screen, which is the main menu of the application:

![Main menu of the CLI based Habit Tracking Application](/pictures/start_menu.png)

From here on, you can create new habits, search, update and delete existing ones, and analyse the habits. To navigate through the application, please use your *up* and *down* keys as well as the *Enter button*.
If you want to close the application, either move the cursor to **Quit the application** and press *Enter*.

&nbsp;

### Create New Habits

If you want to create new habits, select **Create a new Habit** in the main menu. The following step through will show you what to consider.

![New habit creation options](/pictures/habit_creation_options.png)

Choosing the first three options will require you to enter habit name, description and periodicity as shown in the following screenshot;

![New Habit Creation Data Entry](/pictures/habit_creation_successful.png)

#### Load Predefined Data

Whereas the fourth option, *Load Predefined Data to the application*, prints a list of predefined habits to the screen from which you can select a habit to load;

![Load predefined data option in new habit creation menu](/pictures/predefined_habits_that_can_be_loaded.png)

&nbsp;

### Search habits by their name

From the application main menu, selecting *search an existing Habit* will yeild following output where you will be asked to enter the name of the habit that you want to search. If search is found, following is outputted;

![Search habits by their name](/pictures/search_found.png)

If in case the searched habit does not exist, following is the result;

![No search match found](/pictures/search_failed.png)

&nbsp;

### Update existing habits

To update habits, you need to choose *Update an existing Habit* option from the main menu. Then following update operations menu will be shown after the habits;

![Update existing habits](/pictures/update_operations_menu.png)

#### Track Habits

Among these options, *Track/Complete* will yield such a screen with the possible habits that can be updated and you are to select the one that you want to track;

![Track Habits](/pictures/update_track_operation_menu.png)

#### Edit the contents of the Habits

The second option, *Edit the contents* will be shown with such a screen. Select your desired habit whose contents that you want to change;

![Habit contents](/pictures/update_edit_the_contents_operation_menu.png)

And such an output will be generated when a habit is selected and the details to change are provided;

![Changing habit contents](/pictures/update_edit_the_contents_operation_result.png)

&nbsp;

### Delete Habits

Existing habits can be deleted as well by choosing *delete a habit* option that results in such a screen;

![Deleting habits](/pictures/delete_operation.png)

Choose the habit that you want to delete, then such an output will be produced;

![Habit deletion](/pictures/delete_operation_successful.png)

&nbsp;

### Analyze the Habits

When the option *Analyze the habits* is selected, following menu is presented;

![Habit analysis](/pictures/analyze_the_habits_menu.png)

#### Show All Habits

If you select *Show all habits* option, then all the habits along with their details are printed in a formatted tabular form as shown in the following screenshot;

![All habits](/pictures/analyze_show_all_data.png)

#### Show the habit with best streak

If you select *Show the habit with best streak* option, then a single habit (whose best streak is the highest among all habits) along with its details is printed as shown in the accompanying screenshot;

![Best streak habit](/pictures/show_the_habit_with_best_streak_output.png)

#### Show the most completed habit

If you select *Show the most completed habit* option, then a single habit (which has been completed most times) along with its details is printed as shown in the accompanying screenshot;

![most completed habit](/pictures/show_the_most_completed_habit_output.png)

&nbsp;

### Clear all Data

You can choose the option *Clear all the data* from the main menu to delete all the habits from the application. It produces the following output when selected;

![Clear all habits data](/pictures/clear_all_data_result.png)

&nbsp;

### Quit the application

You can quit the application by selecting the last option from the main menu, *Quit the application*. This results in following output;

![Terminating application](/pictures/quit_result.png)

&nbsp;

## Testing the Application

To test the application, change in the directory **unittest** and run **test_habit.py** for testing the Habit class methods as the whole application is based on that class defined in **habit.py** file.

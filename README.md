# This repository contains a beta version of the HabiBart application created to help users define and track their habits.
![1](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/f87d42c6-ff8b-4b9e-b8f6-3037193341c9)
## 1. Distribution:

The application will be delivered as a compressed zip file containing the executable file and all subfolders.

<img src="https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/15ff28bc-3f46-4b73-bb8d-f37a21039972" alt="Image" width="600" height="400">

Figure 1. Structure of the files in main folder

## 2. Data storage:
All the data is stored in JSON files. The database is a list of dictionaries, with each habit represented as one dictionary with attributes.

<img src="https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/ffab3168-74b2-47b8-a240-28d6b7f1651f" alt="Image" width="600" height="600"></b>

Figure 2. Data structure in the database.json file

## 3. Launch:
Due to the early stage of development of this application, users will be asked, after launching the executable file, whether they should run the test fixture or proceed directly to the main menu.

<img src="https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/ca4470ed-256d-41db-8c9c-45997dea6f72" alt="Image" width="400" height="100">

Figure 3. Starting sequence of the application

## 3.1 Launch.Test:
The user should type 't' and press Enter to initiate the test run. Subsequently, messages will be prompted, providing information about the current stage of this process, and the user will be presented with sample data. At certain points in this process, user interaction (pressing Enter to proceed) is required. This functionality is designed to enable progress tracking throughout the testing process.

<img src="https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/abbb4dbb-d788-4f40-ad8e-4cb1daba45ad" alt="Image" width="600" height="400">

Figure 4. Introduction to the first test

<img src="https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/9efc3b74-93e6-43f5-924b-409932290853" alt="Image" width="400" height="100">

Figure 5. Example window screen from test fixture

<img src="https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/6122431c-159b-4fe0-94ff-1d0d3bb1766f" alt="Image" width="600" height="400">

Figure 6. The last test results screen

### The 'assert' command is used to check parts of the code.

For example, a part of the code tests if the creation of a dataset, based on five default habits, with random check-offs for the last 28 days (four weeks) was successful.
<pre>
            print('\n########## Test 2. Creating the dataset with random check_offs for last 28 days(four weeks) ##########\n')
            time.sleep(3)
            dataset = Set()
            dataset.test_function(model.read_from_json_file(database), database)
            result_habits = model.read_from_json_file(database)
            # check if random check_off's were added to a database
            for habit in result_habits:
                assert len(habit['Check_offs']) is not None
            print('\n########## Test 2. Successfully completed! ##########\n')
</pre>

## 3.2 Launch.Menu:
During the first run and after completing the tests, or discarding them at the beginning, the application will check if the database and log_out file exist. If not, these will be created with five predefined habits. The last log_out_date is set to be two days earlier to demonstrate how user notifications about incomplete habits work. These two steps occur only if any of the files are missing

![8](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/20392cce-f6b2-47ed-9da7-16c682e6e44f)

Figure 7. Launch menu testing proceder screen1: database.json file not found

![9](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/89a98578-d049-4991-b151-2f60108291da)

Figure 8. Launch menu testing proceder screen2: log_out_time.json file not found

## 4 Menu:
This is the place where the user can choose from available functions by typing the predefined letter. Based on both files 'database.json' and 'log_out_time.json' (set by default two days earlier for presentation purposes), the user is prompted in the upper part of the menu with habits that have not been completed since the last log-out. If the last log_out was earlier on the same day, it will not be considered, and this part of the menu will be empty.

![10](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/62e9cb04-0e29-4def-a3ae-55c3c4213ba4)

Figure 9. Main menu layout

## 4.1 Menu.Help(h):
This is the place prepered for the user_manual.

![11](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/b3175145-020c-48b2-bcb1-ac83c7cece60)

Figure 10. User_help layout

## 4.2 Menu.Check_off_habit(c):
In this part, the user has the possibility to check off any active habits that have not yet been completed for the day or week. The logic here is based on two variables: 'Active' (boolean) and 'Periodicity' ('daily' or 'weekly'). For instance, if an active habit with weekly periodicity already has a check-off mark in the database for Monday, it will not appear in the list of habits to be completed until the following week.

<pre>
operation.list_of_weekly_habits_with_check_offs_this_week(database, not_completed_habits_week)
# search in a 'habits' database and print all the habits that have to be done weekly
print('------------------------------\nHabits on a weekly basis:\n')
for habit in not_completed_habits_week:
    # habits
    if habit['Periodicity'] == "weekly" and habit['Active'] == True:
        max_counter += 1
        daily_and_weekly_habits.append(habit)
        print(max_counter, habit['Task'], "-", habit['Specification']) # print each item from the list in a separate line
    else:
        pass
</pre>

![12](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/7a6dd0be-7a3f-41ca-8683-72cc290df44f)

Figure 11. Check off habit interface

## 4.3 Menu.Add_new_habit(n):
This is the place to add new habits to the existing default habits in the database.

![13](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/f01d3fa7-cf7a-4241-8ec3-a46e413f5a5b)

Figure 12. Adding new habit interface

## 4.4 Menu.Analytics(a):
User can choose betwenn two predefind options:

![14](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/137ca4ad-3735-4524-9c3c-44fc5663d1a7)

Figure 13. Analytics menu layout

![15](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/10bc1eff-7788-43ce-87aa-d27e71f91a3b)

Figure 14. Analytics/All active habits

![16](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/0045f95e-0b61-47c5-9af7-b82667963070)

Figure 15. Analytics/Longest run streaks for each habit

## 4.5 Menu.Settings(s):
Here, users can deactivate existing habits by selecting them from the list. Upon deactivation, the 'Active' parameter in the database will be changed from 'True' to 'False'. The second option in this menu is designed to modify the last log_out time. This option is intended solely for testing purposes, such as setting a date in the past to display incomplete habits in the main menu.  

![17](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/3d770bda-4219-4c6a-9f52-79f207df3b34)

Figure 16. Settings menu layout

![18](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/38d206fd-65b1-474f-af34-7466195fe693)

Figure 17. Interface to deactivate a habit

![19](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/be6e6f70-f6ca-43b8-a0ef-86123bb5e75e)

Figure 18. Example of the deactivated habit in database file 

## 4.6 Menu.Exit(x):
This part of the code is responsible for closing the app and saving the current date in the 'log_out_time.json' file. This saved date will be used by the next launch of the program, for example, to remind the user of incomplete habits since the last log_in.

<pre>
    def log_out(log_out_file):
        model = Utilities()
        log_out_time = datetime.now().date().isoformat()  # .isoformat() converts date into a string (ISO
        # 8601:"YYYY-MM-DD")
        model.save_into_json_file(log_out_time, log_out_file,
                                  indent_level=4)  # indent specifies number of spaces for each
        # Level of indentation in *.json file. This makes the structure of the file more readable if open separately.
        sys.exit()  # exit the code
</pre>

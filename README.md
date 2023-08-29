# This repository contains a beta version of the HabiBart application created to help users define and track their habits.

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/9557a60a-f39c-4a04-b03a-b659216b9b04)

## 1. Distribution:
The application will be delivered as a compressed zip file containing the executable file and all subfolders.

<img src="https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/7397c525-bbe9-48ba-88ee-c190b9befad9" alt="Image" width="600" height="400">

## 2. Data storage:
All the data is stored in JSON files. The database is a list of dictionaries, with each habit represented as one dictionary with attributes.

<img src="https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/4bc418f1-7f0d-4b5a-885e-d872e181dcf9" alt="Image" width="600" height="600">

## 3. Launch:
Due to the early stage of development of this application, users will be asked, after launching the executable file, whether they should run the test fixture or proceed directly to the main menu.

<img src="https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/bde2b7f3-c462-435a-8a64-b176b2ec926c" alt="Image" width="400" height="100">

## 3.1 Launch.test:
The user should type 't' and press Enter to initiate the test run. Subsequently, messages will be prompted, providing information about the current stage of this process, and the user will be presented with sample data. At certain points in this process, user interaction (pressing Enter to proceed) is required. This functionality is designed to enable progress tracking throughout the testing process.

<img src="https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/56f97edf-442e-46c1-9675-003909614ff9" alt="Image" width="600" height="400">

<img src="https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/33832cb1-8aeb-4c75-aa96-8b9be654be0c" alt="Image" width="400" height="100">

<img src="https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/b0294899-3a58-4e6f-a31e-e3207cc9e981" alt="Image" width="600" height="400">

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

## 3.2 Launch.menu:
During the first run and after completing the tests, or discarding them at the beginning, the application will check if the database and log_out file exist. If not, these will be created with five predefined habits. The last log_out_date is set to be two days earlier to demonstrate how user notifications about incomplete habits work. These two steps occur only if any of the files are missing

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/227a0ce5-a3a9-43ab-ae2f-95f568f480e0)

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/92bc2d52-061e-4698-8996-5a51f037c34c)

## 4 Menu:
This is the place where the user can choose from available functions by typing the predefined letter. Based on both files 'database.json' and 'log_out_time.json' (set by default two days earlier for presentation purposes), the user is prompted in the upper part of the menu with habits that have not been completed since the last log-out. If the last log_out was earlier on the same day, it will not be considered, and this part of the menu will be empty.

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/7f780910-a8b0-4f88-8f66-56dd5dafc8a3)

## 4.1 Menu.help(h):
This is the place prepered for the user_manual.

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/379798ca-11e4-42f9-80ce-8b1bdf3a5291)

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

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/95d00d33-fd34-4205-aeef-2f7e2539b239)

## 4.3 Menu.Add_new_habit(n):
This is the place to add new habits to already existing default habits in database

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/f875d8e4-0d04-4735-b829-9379139e86b9)

## 4.4 Menu.Analytics(a):
User can choose betwenn two predefind options:
![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/fc1f976a-8cb0-446d-a4e4-9df20a15ef38)

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/8b15a0e5-339d-4608-a211-a71c399f5517)

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/68de086f-fe01-4290-bfd5-aba0054bcee8)

## 4.5 Menu.Settings(s):
Hier user can delete(deactivate) existing habits by choosing them from the list. After deactivation the parameter 'Active' in database will be changed from True to false. The second optionin this menu is created to change last log_out_time. This option is only for testing purpose, f.e. to set date in the past and shown not completed habits in main menu.  

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/f89c36ff-1ae4-4a45-ab2e-53a063c40050)
![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/7ffd61f0-0d79-40ae-90b5-ac5eeeb8ea0b)
![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/32f9c44c-f2f9-4fc3-bb30-29815d919a90)

## 4.6 Menu.Exit(x):
This part of the code is responsible for closing the app and saving the current date in 'log_out_time.json' file which will be used be the next lauch of the program f.e. to prompt user not completed habits since last log_in.

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

































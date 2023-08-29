# OOFPP_Habits_Submission_Phase_2_and_3

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/9557a60a-f39c-4a04-b03a-b659216b9b04)

# This is a beta version of the HabiBart application created to help users define and track their habits.

## 1. Distribution:
The application will be delivered as a zip file containing the compressed executable file and all subfolders.
![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/7397c525-bbe9-48ba-88ee-c190b9befad9)

## 2. Data storage:
All the data are storred in to json files. The database is a list of dictionaries where each habit is one dictionary with atributes.
![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/4bc418f1-7f0d-4b5a-885e-d872e181dcf9)

  


## 3. Launch:
Because of the early stage of developing of this application user after launching the exe. file will be asked if it should run test fixture or go direct go to main menu:

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/bde2b7f3-c462-435a-8a64-b176b2ec926c)

## 3.1 Launch.test:
User shoul type 't' and press enter to launch test run. After this there will propmt a messages with the information according to stage of this proces and user will be shown the sample data.
In some points of this process there is a interaction(pressing enter, to go forward) from the user site needed. This functionality sholud allow to track the progges during the testing process.

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/56f97edf-442e-46c1-9675-003909614ff9)

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/33832cb1-8aeb-4c75-aa96-8b9be654be0c)

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/b0294899-3a58-4e6f-a31e-e3207cc9e981

With the 'assert' command the parts of the code are checked. 

#As example the part of the code which test if: creating, based on five default habits, the dataset with random check_offs for last 28 days(four weeks), was succesfull. 

            print('\n########## Test 2. Creating the dataset with random check_offs for last 28 days(four weeks) ##########\n')
            time.sleep(3)
            dataset = Set()
            dataset.test_function(model.read_from_json_file(database), database)
            result_habits = model.read_from_json_file(database)
            # check if random check_off's were added to a database
            for habit in result_habits:
                assert len(habit['Check_offs']) is not None
            print('\n########## Test 2. Successfully completed! ##########\n')

## 3.2 Launch.menu:
During the first run und after compleating the tests, or discard it at the begining, the application will cheeck if database and log_out file are existing. If not these will be created wit five predefined habits. Last log_out_date ist set to be to days earlier to present how user notifiactions about not completed habits are working. Those two steps are happening only if any of the file is missing.

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/227a0ce5-a3a9-43ab-ae2f-95f568f480e0)

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/92bc2d52-061e-4698-8996-5a51f037c34c)

## 4 Menu:
This is the palce where the user through typing the predefine letter can choose one from avaliable functions. Based of the both files 'databse.json' and 'log_out_time.json' (set as default two days earlier fot the presentation purpose) user get prompt in the upper part of menu those habits there are not completed since last log_out. If last log_out was earlier the same day that will not count and this part of menu will be empty. 

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/7f780910-a8b0-4f88-8f66-56dd5dafc8a3)

## 4.1 Menu.help(h):
This is the place prepered for the user_manual.

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/379798ca-11e4-42f9-80ce-8b1bdf3a5291)

## 4.2 Menu.Check_off_habit(c):
In this part user have the possibility to check of anyfrom the activ habits that hasn't been not yet completed for this day or this week. Logic hier is based on two variables: 'Active'(boolean) and 'Periodicity'('daily' or 'weekly'), f.e. if an activ habit with weekly periodicity have allredy check_off mark in the database at monday it will not appera in the list of habits to completed since next week.  

 operation.list_of_weekly_habits_with_check_offs_this_week(database, not_completed_habits_week)
                # search in a 'habits' database and print all the habits that have to be done weekly
                print('------------------------------\nHabits on a weekly basis:\n')
                for habit in not_completed_habits_week:  # habits
                    if habit['Periodicity'] == "weekly" and habit['Active'] == True:
                        max_counter += 1
                        daily_and_weekly_habits.append(habit)
                        print(max_counter, habit['Task'], "-", habit['Specification'])  # print each item from the list
                    # in a separate line
                    else:
                        pass
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

    def log_out(log_out_file):
        model = Utilities()
        log_out_time = datetime.now().date().isoformat()  # .isoformat() converts date into a string (ISO
        # 8601:"YYYY-MM-DD")
        model.save_into_json_file(log_out_time, log_out_file,
                                  indent_level=4)  # indent specifies number of spaces for each
        # Level of indentation in *.json file. This makes the structure of the file more readable if open separately.
        sys.exit()  # exit the code

































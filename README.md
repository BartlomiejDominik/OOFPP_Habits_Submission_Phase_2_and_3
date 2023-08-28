# OOFPP_Habits_Submission_Phase_2_and_3

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/9557a60a-f39c-4a04-b03a-b659216b9b04)

##This is a beta version of the HabiBart application created to help users defining and tracking theirs habits.

## 1. Distribution:
Application will be delivered as an zip.file with compresed exe.file and all subsolders.
![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/7397c525-bbe9-48ba-88ee-c190b9befad9)

## 2. Launch:
Because of the early stage of developing of this application user after launching the exe. file will be asked if it should run test fixture or go direct go to main menu:

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/bde2b7f3-c462-435a-8a64-b176b2ec926c)

## 2.1 Launch.test:
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

## 2.2 Launch.menu:
During the first run und after compleating the tests, or discard it at the begining, the application will cheeck if database and log_out file are existing. If not these will be created wit five predefined habits. Last log_out_date ist set to be to days earlier to present how user notifiactions about not completed habits are working. Those two steps are happening only if any of the file is missing.

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/227a0ce5-a3a9-43ab-ae2f-95f568f480e0)

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/92bc2d52-061e-4698-8996-5a51f037c34c)

## 3 Menu:
This is the palce where the user through typing the predefine letter can choose one from avaliable functions.

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/7f780910-a8b0-4f88-8f66-56dd5dafc8a3)

## 3 Menu.help(h):
This is the place prepered for the user_manual.

![image](https://github.com/BartlomiejDominik/OOFPP_Habits_Submission_Phase_2_and_3/assets/140627512/379798ca-11e4-42f9-80ce-8b1bdf3a5291)

## 3 Menu.Check_off_habit(c):















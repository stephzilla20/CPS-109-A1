# CPS 109 Assignment 1
# Name: Stephen Tao
# Student number: 501189625
# Problem: Finding a way to keep track of the foods you eat in order to be able to lose or gain weight
# This program is a calorie calculator and tracker, asks user for their info
# to find the daily calories they need and allows them to track their foods calories and macros
# Assumes all inputs from user are valid!


def main():
    '''
    main function runs all helper functions to allow user to track calories
    '''
    #brief desc for user
    print("\t Welcome To Stephen's Calorie Tracker :D")
    print("This program helps you with your weigh loss/gain goal\n"
          "Its main purpose is to track your daily calories.\n"
          "Start by finding out how many calories you need!\n ")

    #runs function to track calories and calculate calories
    trackInfo(calcCals())


def trackInfo(intakeCal):
    '''tracks calories, protien, carbs, and fats, takes in a total calorie arguement'''

    foodName = [] #list to store name of all inputted foods
    foodCal = [] #list to store all inputted calories
    foodProtien = [] #list to store total inputted protien
    foodCarbs = [] #list to store total inputted carbs
    foodFat = [] #list to store total inputted fat

    #brief desc for user
    print("\nHere you can track your food's calories, protien, carbs, and fat!")

    #initialize boolean variable to keep track of if user wants to keep adding food
    addFood = True

    #while loop to keep asking user for food info
    while addFood == True:

        #prompts user for foods info and adds all inputted info to appropriate list to store values
        foodName.append(input("Please enter the name of the food: "))
        foodCal.append(int(input("Please enter the number of calories the food has: ")))
        foodProtien.append(int(input("Please enter the amount of protien in grams: ")))
        foodCarbs.append(int(input("Please enter the amount of carbs in grams: ")))
        foodFat.append(int(input("Please enter the amount of fat in grams: ")))

        #prints out updated total calories left after user logs calories
        print(f"You have {intakeCal - sum(foodCal)} calories left for today!\n")

        #asks user if they want to keep adding foods
        keepAdd = input("Would you like to add more foods? Enter 'yes' or 'no': ")

        #if user enters 'no' loop ends
        if keepAdd == 'no':
            break


    #prints out final totals overview for user to see
    print("\nHere are your daily totals: ")
    print(f"Your total calories are: {sum(foodCal)}") #total calories
    print(f"Your total protien is: {sum(foodProtien)}g") #total protien in grams
    print(f"Your total carbs are: {sum(foodCarbs)}g") #total carbs in grams
    print(f"Your total fats are: {sum(foodFat)}g") #total fats in grams
    print("Today you ate: ", end = '') #all inputted foods

    #for loop to loop through list of names of food inputted and prints
    for foods in range(len(foodName)):
        print(f'{foodName[foods]} - ', end = '')

    #if-else to check if user exceeded or stayed under daily calorie goal
    if intakeCal >= sum(foodCal):
        print("\nGood job! You are below your daily calories today! :D")
    else:
        print(f"\nOh no! You are over your daily calories today. Try to stay under {intakeCal} calories!")



def calcCals():
    '''
    helper function that takes user info as input and does all caluclations to find daily calorie intake,
    returns final daily calorie intake
    '''

    #prompts user for age, height, weight, and gender
    print("Please enter your:")
    userAge = int(input("Age (years): ")) #users age
    userHeight = int(input("Height (cm): ")) #users height
    userWeight = int(input("Weight (kg): ")) #users weight
    userGender = str(input("Please enter your gender: ")) #users gender

    #prompts user for their activity level
    print("Please choose your active level (1,2,3,4 or 5): ")
    #users activity level
    userActive = int(input("1 - little to no exercise \n"
                           "2 - exercise 1 - 3 days per week\n"
                           "3 - exercise 3- 5 days per week\n"
                           "4 - exercise 6 -7 days per week\n"
                           "5 - intese exerise 6 -7 days per week\n"))

    userCalories = round(calcAMR(userActive, calcBMR(userAge, userHeight, userWeight, userGender))) #the users maintainence calories using helper function

    #prompts user to enter their preference for weight loss/gain
    gainOrLose = input("Do you want to gain weight or lose weight? Please enter 'gain' or 'lose: ") #if user wants to gain or lose
    gainLoseSpeed = input("Do you want to gain or lose weight faster or slower? PLease  enter 'fast' or 'slow': ") #how fast user wants to gain or lose

    totalCal = (finalCal(gainOrLose, gainLoseSpeed, userCalories)) #the users total daily calorie intake after preferences using helper function

    print("Your daily calorie intake should be: " + str(totalCal)) #prints out total daily calorie intake for user to see

    return totalCal


def finalCal(mode, speed, calories):
    '''
    helper function that determines calorie intake based on users
    weight loss/gain preferences and their calories as arguments,
    returns final daily calorie intake
    '''

    #nested if to check if user wants to gain, checks to see if fast or slow, adjusts calories accordingly
    if mode == 'gain':
        if speed == 'fast':
            calories = calories + 500
        else:
            calories = calories + 300

    #nested if to check if user wants to lose, checks to see if fast or slow, adjusts calories accordingly
    if mode == 'lose':
        if speed == 'fast':
            calories = calories - 500
        else:
            calories = calories - 300
    return calories


def calcAMR(activeLevel, BMR):
    '''helper function that calculates the Active Metabolic Rate based on activity levels(maintainence calories), takes in users activity level and BMR as arguments'''

    #if-elif to check user activity level and calucalte AMR accordingly using BMR
    if activeLevel == 1:
        AMR = BMR * 1.2
    elif activeLevel == 2:
        AMR = BMR * 1.375
    elif activeLevel == 3:
        AMR = BMR * 1.55
    elif activeLevel == 4:
        AMR = BMR * 1.725
    elif activeLevel == 5:
        AMR = BMR * 1.9
    else:
        pass
    return AMR


def calcBMR(age, height, weight, gender):
    '''helper function that calculates Basal Metabolic Rate (BMR), takes in users age, height, weight, and gender as arguments'''

    femaleBMR = 447.593 + (9.247 * weight) + (3.098 * height) - (4.33 * age) #formula for BMR for females
    maleBMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age) #formula for BMR for males

    #if statement to check users gender to return appropriate BMR
    if gender == "male": #if user is male return male bmr value
        return maleBMR
    if gender == 'female': #if user is female return female bmr value
        return femaleBMR

#runs the main function
main()
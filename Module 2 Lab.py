#Alexander Eyermann 11/3/2024
#Module 2 Lab
#This program asks for a set of student names & their GPAs to determine if-
#-They Qualify for the deans list or Honor Roll

#Bool Variable that controls the function of the main block of code on exit condition
exitCon = False
while exitCon == False:
    lastName = input("Enter the Students Last Name (Enter 'ZZZ' to Quit): ")
    if lastName == "ZZZ":
        exitCon = True
        break

    firstName = input("Enter the Students First Name: ")
    gpa = float(input("Enter the Students GPA: "))

    if gpa >= 3.5:
        print(f"{firstName} {lastName} has made the Deans List!")
    elif gpa >= 3.25:
        print(f"{firstName} {lastName} has made the Honor Roll!")
    else:
        print(f"{firstName} {lastName} did not qualify for the Deans list or the Honor Roll")

#Exit Confirmation
print("Goodbye!")
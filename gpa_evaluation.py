"""

Joe Douglas

gpa_evaluation.py

This purpose of this app is to evaluate a student's GPA to determine if they will make //
Honor Roll or Dean's List. 

"""

last_name = str(input("Please enter your last name or press 'ZZZ' to quit: "))
#student last name

while True:
    if last_name == "ZZZ":      
        break
        #quit

    first_name = str(input("Please enter your first name: "))        
    #student first name

    gpa = float(input("Please enter your GPA: "))       
    #student GPA

    full_name = first_name + " " + last_name

    if gpa >= 3.5:
        print(full_name, "has made the Dean's List")       
        #test for Dean's List

    elif gpa >= 3.25 and gpa < 3.5:
        print(full_name, "has made the Honor Roll")        
        #test for Honor Roll

    else:
        print(full_name, "has not made Honor Roll or Dean's List yet")      
        #test for gpa < 3.25

    break

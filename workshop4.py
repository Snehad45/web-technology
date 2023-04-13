def percent ():
    """It take percentage of students and displays the grade of the students"""
    marks= int(input("Enter the percentage of the student:" ))
    if marks>=70 and marks<=100:
        print("your grade is 'A'")
    elif marks>=60 and marks<70:
         print("your grade is 'B'")
    elif marks>=50 and marks<60:
        print("your grade is 'C'")
    elif marks>=40 and marks<50:
        print("your grade is 'D'")
    else:
        print("you are failed")
    print ()      

percent()  
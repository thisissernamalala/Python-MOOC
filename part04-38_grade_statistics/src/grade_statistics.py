import math

grade = 0
exam_points = 0
exercise_points = 0
total =0
count = 0
my_grades = []
ex_p = []
xam_p = []
while True:
    inpu = input("Exam points and exercises completed: ")
    if inpu != "":
        split_val = inpu.split()
        exam_points += int(split_val[0])
        exercise_points += int(split_val[1])
        ex_p.append(exercise_points)
        xam_p.append(exam_points)
        count+=1
    else:
        print("Statistics:")
        ex_points = math.floor(exercise_points/10)
        total = ex_points+exam_points
        for i in range(count):
            pp = math.floor(ex_p[i]/10)
            xam = xam_p[i]
            subb = pp + xam
            print(subb)
            
            if exam_points <10:
                grade = 0
                my_grades.append(grade)
            else:
                if subb>=0 and subb<=14:
                    grade = 0
                    my_grades.append(grade)
                elif subb>=15 and subb<=17:
                    grade = 1
                    my_grades.append(grade)
                elif subb>=18 and subb<=20:
                     grade = 2
                     my_grades.append(grade)
                elif subb>=21 and subb<=23:
                    grade = 3
                    my_grades.append(grade)
                elif subb>=24 and subb<=27:
                    grade = 4
                    my_grades.append(grade)
                elif subb>=28 and subb<=30:
                    grade = 5
                    my_grades.append(grade)
        av = total/count
        
        print(f"Points average: {av:.2f}")
        print(f"Pass percentage: {sum(my_grades)/count*100}")
        print("Grade distribution: ")
        print(my_grades)
        for i in range(5,-1,-1):
            occur = my_grades.count(i)    
            print(f"  {i}: {occur*'*'}")
        break
        


    
    

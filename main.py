gradepoint1 = input("Enter your course 1 letter grade: ")
credit1 = input("Enter your course 1 credit: ")
def grade(gradepoint,course):
  if f"{gradepoint}" == 'A' or f"{gradepoint}" == 'a':
    print(f"Grade point for {course} is: 4.0")
  elif f"{gradepoint}" == 'A-' or f"{gradepoint}" == 'a-':
    print(f"Grade point for {course} is: 3.67")
  elif f"{gradepoint}" == 'B+' or f"{gradepoint}" == 'b+':
    print(f"Grade point for {course} is: 3.33")
  elif f"{gradepoint}" == 'B' or f"{gradepoint}" == 'b':
    print(f"Grade point for {course} is: 3.0")
  elif f"{gradepoint}" == 'B-' or f"{gradepoint}" == 'b-':
    print(f"Grade point for {course} is: 2.67")
  elif f"{gradepoint}" == 'C+' or f"{gradepoint}" == 'c+':
    print(f"Grade point for {course} is: 2.33")
  elif f"{gradepoint}" == 'C' or f"{gradepoint}" == 'c':
    print(f"Grade point for {course} is: 2.0")
  elif f"{gradepoint}" == 'D' or f"{gradepoint}" == 'd':
    print(f"Grade point for {course} is: 1.0")
  elif f"{gradepoint}" == 'F' or f"{gradepoint}" == 'f':
    print(f"Grade point for {course} is: 0.00")
  else:
    print(f"Grade point for {course} is: 0.00")
  
grade("gradepoint1,course")

gradepoint2 = input("Enter your course 2 letter grade: ")
credit2 = input("Enter your course 2 credit: ")
grade("gradepoint2,course 2")

gradepoint3 = input("Enter your course 3 letter grade: ")
credit3 = input("Enter your course 3 credit: ")
grade("gradepoint3,course 3")

gradepoint1 = float(gradepoint1)
gradepoint2 = float(gradepoint2)
gradepoint3 = float(gradepoint3)

GPA = float(gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3) 
print("Your GPA is: "+ str(GPA))
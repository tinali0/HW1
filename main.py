gradepoint1 = input("Enter your course 1 letter grade: ")
credit1 = input("Enter your course 1 credit: ")

def grade(gradepoint):
  if gradepoint == 'A' or gradepoint == 'a':
    return 4.0
  elif gradepoint == 'A-' or gradepoint == 'a-':
    return 3.67
  elif gradepoint == 'B+' or gradepoint == 'b+':
    return 3.33
  elif gradepoint == 'B' or gradepoint == 'b':
    return 3.0
  elif gradepoint == 'B-' or gradepoint == 'b-':
    return 2.67
  elif gradepoint == 'C+' or gradepoint == 'c+':
    return 2.33
  elif gradepoint == 'C' or gradepoint == 'c':
    return 2.0
  elif gradepoint == 'D' or gradepoint == 'd':
    return 1.0
  elif gradepoint == 'F' or gradepoint == 'f':
    return 0.00
  else:
    return 0.00
  
  
grade1 = grade(gradepoint1)
print("Grade point for course 1 is: " + str(grade1))

gradepoint2 = input("Enter your course 2 letter grade: ")
credit2 = input("Enter your course 2 credit: ")
grade2=grade(gradepoint2)
print("Grade point for course 2 is: " + str(grade2))

gradepoint3 = input("Enter your course 3 letter grade: ")
credit3 = input("Enter your course 3 credit: ")
grade3=grade(gradepoint3)
print("Grade point for course 3 is: " + str(grade3))

credit1 = float(credit1)
credit2 = float(credit2)
credit3 = float(credit3)


GPA = float((grade1 * credit1 + grade2 * credit2 + grade3 * credit3) / (credit1+ credit2 + credit3))
print("Your GPA is: "+ str(GPA))
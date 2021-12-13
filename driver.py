from Person import person



n=input("Enter name: ")
a=eval(input("Enter address: "))

people=person(n,a)

p=input("Are you a student or a teacher?")

if p=="student" or "Student":
    from Person import student
elif p=="teacher" or "Teacher":
    from Person import teacher

q=input("What do you want to do?")
murid=student
guru=teacher

if q == "add courses":
    guru.addCourses()
elif q == "remove courses":
    guru.removeCourses()
elif q== "input grades":
    murid.addCourseGrade()
elif q== "print scores":
    murid.printGrades()
elif q== "get grade average":
    murid.getAvgGrades()






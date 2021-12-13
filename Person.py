class person():
    def __init__(self,name,address):
        self.name=name
        self.address=address
        
    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address
    
    def setAddress(self,address):
        self.address=eval(address)
    
    def __str__(self):
        return f"name: {self.getName()}\n address: {self.getAddress()}"

class teacher(person):
    def __init__(self,courses,numCourses=0):
        self.__courses=courses
        self.__numCourses=len(self.__courses)
    

    def addCourses(self):
        self.__courses=[]
        while True:
            course_name=input("What courses do you want to add: ")
            self.__courses.append(course_name)
            q=input("do you want to add more (y/n): ")
            if q=="y":
                continue
            else:
                break
        
        return self.__courses

    def getNumCourses(self):
        return self.__numCourses
    
    def removeCourses(self):
        self.__courses()
        keys = list(self.__courses.keys())
        print(self.__courses)
        input("do you want to remove a course?(y/n)")
        while "y":
            i=input("which course do you want to remove (select number):")
            self.__courses.pop(keys[i-1])
            print(self.__courses)
            q=input("remove another course(y/n)")
            if q=="y":
                continue
            else:
                break
        return self.__courses

    def __str__(self):
        return f"name: {self.getName()}\n address: {self.getAddress()}"

    
    
class student(teacher):
    def __init__(self,grades):
        self.__grades=grades

    def addCourseGrade(self):
        self.__courses()
        self.__grades=[self.__courses]
        keys = list(self.__grades.keys())
        print(self.__grades)
        c=input("which course's grade would you like to input?(input number)")
        g=input("Enter grade: ")
        self.__grades[keys[c-1]]==g
        q=input("Would you like to add another score?(y/n)")
        while q=="y":
            c=input("which course's grade would you like to input?(input number)")
            g=input("Enter grade: ")
            self.__grades[keys[c-1]]==g
            q=input("Would you like to add another score?(y/n)")
            if q=="y":
                continue
            else:
                break

        return self.__grades

    def printGrades(self):
        return self.__grades
    
    def getAvgGrades(self):
        for key,value in self.__grades.items():
            return sum(value)/ float(len(value))





    def __str__(self):
        return f"name: {self.getName()}\n address: {self.getAddress()}"

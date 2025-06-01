class Student :
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def Average(self):
        
        return sum(self.marks)/len(self.marks)
    def is_pass(self):
        return  all(marks>40 for marks in self.marks)           
    def __str__(self):
        return f"name :{self.name}\nrollno:{self.rollno}\nmarks:{self.marks}"
class student_mangement_class:
    def __init__(self):
        self.marks=[]
        self.students=[]
        self.rollno=[]
    def add_student(self):
        student=input('enter student name:')
        rollno=input('enter roll number')

        if rollno in self.rollno:
                print("already enrolled.")
        else:
                marks=[]
                for i in range(3):
                    mark=int(input(f"enter marks{i+1}: "))
                    marks.append(mark)
                new_student = Student(student, rollno, marks)
                
                print(f'average: "{new_student.Average()}')
                self.students.append(new_student)
                self.rollno.append(rollno)  
                print("student enrolled successfully.")
    def list_students(self):
        for student in self.students:
           print(student)
    def search_student(self):
        rollnos=input("enter roll number of student you want to search:")
        for student in self.students:   
          if student.rollno == rollnos:
             print(student)
             return
        print("student not found")
    def delete_student(self):
        rollnos=input("enter roll number of student you want to delete:")
        for student in self.students:   
          if student.rollno == rollnos:
             self.students.remove(student)
             print('student delete successfully.')
             return
        print("student not found")
    def class_average(self):
        total = 0
        for student in self.students:
           total += student.average()
        return total / len(self.students)
    def marks_update(self):
        update_rollno=input("enter rollno of student whose marks you want to update:")
        for student in self.students:
         if update_rollno in self.rollno:   
               new_marks=[]
               for i in range(3):
                upgrade_marks=int(input(f"enter upgraded marks:{i+1}"))
                new_marks.append(upgrade_marks)
               student.marks = new_marks  # ✅ Correct assignment (you had: student.marks = upgrade_marks ❌)

               print("marks update")
               return
        else:
            print("student not found.")
    def fail_pass_student(self):
        print("passed students: \n")
        for student in self.students:   
         if student.is_pass()==True:  
             print(student)
        print('Failed Students:\n')
        for student in self.students: 
          if student.is_pass()==False:  
            print(student)
system=student_mangement_class()
  
def menu(system):
    while True:
        print("welcome to student marks management system :\nChoose the options : ")
        
        print("1.add student\n2.list students\n3.search student\n4.delete student\n5.class average\n6.marks update\n7.show fail and pass student ")
        print('0 to Exist')
        enroll=int(input('enter the option: '))
        if enroll == 1:
            system.add_student()
        elif enroll == 2:
            system.list_students()
        elif enroll == 3:
            system.search_student()
        elif enroll == 4:
            system.delete_student()
        elif enroll == 5:
           avg= system.class_average()
           print(f'class average {avg}')
        elif enroll == 6:
            system.marks_update()
        elif enroll == 7:
            system.fail_pass_student ()
        elif enroll == 0:
            print('exiting system')
            break
        else:
            print ("invalid option..")
            
system=student_mangement_class()
menu(system)
       
            


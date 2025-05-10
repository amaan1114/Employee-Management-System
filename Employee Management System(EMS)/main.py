#Employee Dictionary to store Employee Data
employee={}

#adding employee
def add_employee(emp_id,name,age,department,salary):
   emp = {emp_id:{'name:':name,
                  'age:':age,
                  'department:':department,
                  'salary:':salary}}
   employee.update(emp)

#Showing all the employees
def view_employees():
    if(employee):
        print()
        print('id'.ljust(15),"name".ljust(13),"age".ljust(14),"department".ljust(14),"salary")
        for key in employee:
            print()
            print(str(key).ljust(15),end="")
            
            for value in employee[key].values():
                print(str(value).ljust(15),end="")
        print("\n")
    else:
        print("No employees available\n")

#Searching for the employee
def search_employee(id):
    if(id in employee):
        for keys,value in employee[id].items():
                print(keys,value)
        print('-------------------\n\n')
    else:
        print("Employee not found\n")




#Main Menu
def main_menu():
    select=0
    while(select!=4):
        print("1. Add Employee\n2. View All Employees\n3. Search for Employee\n4. Exit\n")
        select = int(input("Select (number) from the option what you want to do: "))
        if(select==1):
            id = int(input("Enter Employee's ID: "))

            #Checking for the employee id to be unique
            if(id in employee):
                print("This Employee Id already exist")            
            else:
                name = input("Enter Employee's name: ")
                age = int(input("Enter Employee's age: "))
                department = input("Enter Employee's department: ")
                salary = int(input("Enter imployee's salary: "))
                print()
                add_employee(id,name,age,department,salary)
                print("Employee successfully added!\n")
        if(select==2):
            view_employees()
        if(select==3):
            id = int(input("Enter the id of the employee to search: "))
            print()

            search_employee(id)
        
             
        

main_menu()




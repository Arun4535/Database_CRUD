#Tasks to be done
# 1.create connection in constructor
# 2. insert
# 3. display all
# 4. delete
# 5. update
# 6. Truncate
#create pythonTest database in mysql first

import mysql.connector as connector

class DBHelper:
    def __init__(self): #constructor will create table
        self.con = connector.connect(host='localhost',port='3306',user='root',password='root',database='pythonTest')
        query='create table if not exists Employee(empId int primary key,Name varchar(20),phone varchar(12))'
        cur=self.con.cursor()
        cur.execute(query)
        print("Table created")
    
    #insert
    def insert_employee(self,id,name,contact):
        query = "insert into employee(empId,Name,phone) values({},'{}','{}')".format(id,name,contact)
        #print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('employee details inserted')

    #display details
    def display(self):
        query = 'select * from employee'
        cur = self.con.cursor()
        cur.execute(query)
        print("Table entries are : ")
        for row in cur:
            print("EmployeeID : ",row[0],", EmployeeName : ",row[1],", Contact : ",row[2])
    
    #delete 
    def delete_employee(self,id):
        query = 'delete from employee where empId = {}'.format(id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('Employee deleted')
    
    #update method to update name corresponding given employee id
    def update_employee(self,id,newName):
        query = 'update employee set Name = "{}" where empId = {}'.format(newName,id)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('Employee details updated')

    def delete_all(self):
        query = 'truncate table employee'
        cur = self.con.cursor()
        cur.execute(query)
        print('all rows deleted')
        self.con.commit()


# helper = DBHelper() #object
# helper.insert_employee(1, "Arun", "1234567890")
# helper.insert_employee(2, "Ankit", "1234567890")
# helper.insert_employee(3, "Raj", "1234567890")
# helper.insert_employee(4, "Mohit", "1234567890")
# helper.display()
# helper.delete_employee(1)

# helper.display()
# print()
# helper.update_employee(3, 'Hemant')
# print()
# helper.display()

def main():
    db = DBHelper()
    while True:
        print("Press 1 to insert employee")
        print("Press 2 to display all employee")
        print("Press 3 to delete employee")
        print("Press 4 to update employee")
        print("Press 5 to delete all rows of employee")
        print("Press 6 to exit")
        print()
        try:
            choice = int(input())
            if choice == 1 :
                #insert
                id = int(input('Enter Employee id : '))
                name = input('Enter Employee name : ')
                contact = input('Enter Employee phone no. : ')
                print()
                db.insert_employee(id, name, contact)
                print()

            elif choice == 2 :
               #display
               db.display()
            elif choice == 3 :
                #delete
                id = int(input('Enter employee id to be deleted '))
                db.delete_employee(id)
            elif choice == 4 :
                id = int(input('Enter employee id whose name to be updated: '))
                name = input('Enter new name : ')
                db.update_employee(id, name)
                
            elif choice == 5:
                #truncate
                db.delete_all()
            elif choice == 6:
                break
            else:
                print('Invalid input! Try again')
        except Exception as e:
            print(e)
            print('Invalid input! Try again')
main()

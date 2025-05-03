import json
from All_path.path import Sign_up_path
from All_path.path import Staff_path
from Error_handal.logger import write_logs
from Authentication.auth_singup import  User
from Domain.menu.restaurant_menu import menu_details
from Domain.staff_manage.management_menu import item_manage
from Domain.order.order_items import order_item_bill_details

import datetime

         
class Login_Admin:
    def __init__(self,path):
        
        try:
            self.path=path
            
            # self.path=r"Src/Database/domain.json"
            # Load existing user data from JSON file
            
            with  open(self.path,'r') as file:
                self.load_data=json.load(file) 
        except Exception as e:
            data=datetime.datetime.now()            
            error_data={'error':str(e),"funcation_name":'__init__()','class':'Login_User','date':data}
            write_logs(str(error_data))
            print('Technical issue please wait')
                    
    def input_admin(self):
        
        
            
        try:
            while True:
            
                input_data=input('please enter your email address:  ')
                found=False
                for email in self.load_data:
                    for key,value in email.items():
                        if key == 'email' and value == input_data:
                            
                            
                        
                            found=True
                if not found:
                    print('No match invalid email please try again!') 
                else:
                    break
                
                                
            while True:
                input_data=input('please enter your password :  ')
                found=False
                for password in self.load_data:
                    for key,value in  password.items():
                        if key =='password' and value == input_data:
                            
                            print('Login successfully!')
                            
                
                            found=True
                
                if not found:
                    print('No match invalid password please try again!') 
                else:
                   break                
        except Exception as e:
            data=datetime.datetime.now()            
            error_data={'error':str(e),"funcation_name":' input_user()','class':'Login_User','date':data}
            write_logs(str(error_data))
            print('Technical issue please wait')

# child class (Admin_Login) is created when inherits the properties of the parent class

class Staff_Login(Login_Admin):
    """The child class is inheriting the properties of the parent class and using them"""
    try:
        
        def __init__(self,path):
            self.path=path
            # self.path=r"Src/Database/staff.json"
            with open(self.path,'r') as file:
                self.load_data=json.load(file)
    except Exception as e:
        data=datetime.datetime.now()  
        error_data={'error':str(e),'function_name':'__init__()','class':'Admin_Login','date':data} 
        write_logs(str(error_data)) 
        print('Technical issue please wait!')
        
        
        

      
# from Authentication import Staff_path         
def login_menu():
    """When the user press number 1, an object of the parent class (Login_User) is 
     Creat and its method is executed.
     When the  user preee number 2, an object of the child class (Admin_Login) is created 
     when inherits the properties of the parent class and its method is executed"""

    print('******Start login*****')
    print('='*10)
    print('1.  admin login....!')
    print('2.  staff login....!')
    press_number=int(input('Select  opation: '))
    if press_number == 1:
        data= Login_Admin(Sign_up_path)
        data.input_admin()
        print()
        # call menu Details
        # menu_details()
        # order_item_bill_details()
    elif press_number == 2:
        data= Staff_Login(Staff_path )
        data.input_admin()
        # call manage item
        # item_manage() 
        

        
def restaurant_menu():
    while True:
        
        print('='*30)
        print()
        print('Restaurant Manegment System')
        print()
        print('='*30)
        print()
        print('1. Sign up......') 
        print('2. Login........')
        print('3. Exit')
        print()
        press_number=input('Select any option: ')
        if press_number.isdigit():
            press_number=int(press_number)
            if press_number == 1:
                print()
                data=User(Sign_up_path)
                data.load_user_details()
                data.input_user_details()
                data.save_user_data()
            elif press_number == 2:
                print()
                login_menu()
            elif press_number ==3:
                break 
            else:
                print('invalid number please check option!')   
        else:
            print('invalid number please try again!')                   
           
           
        

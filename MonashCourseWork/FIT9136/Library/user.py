from abc import ABC, abstractmethod
import csv
import datetime
import re
from custom_errors import *



TODAY = "15/09/2025"

userdict = {}

# this is the hard coded user policy given by the assignment

borrow_policy_physical = {"student": 10, 'staff': 14, "other": 7}
borrow_quota_physical = {"student": 4, 'staff': 6, "other": 2}
grace_period = {"student": 0, 'staff': 2, "other": 0}
fine_rate = {"student": 0.5, 'staff': 0.5, "other": 1.0}

class User(ABC):
    # Your code goes here
    '''
    This is a class that stores the user information, each user should contain ID, password, name, role and department.
    It also contains a list that keeps track of every user in user.instance.
    '''
    instances = []

    def __init__(self,ID: str,password: str,name: str,role: str,department: str)->None:
        '''
        this is the constructor of the class, it takes in ID, password, name, role and department
        and creates a new user instance. it also append the user to the class list
        there should only exist three roles:
            -student (has s as prefix in user ID)
            -staff (has e as prefix in user ID)
            -other (has o as prefix in user ID)
        '''
        assert type(ID) == str, f"user id shoud be string instead of {type(ID)}"
        self.ID = ID
        assert type(password) == str, f"user password shoud be string instead of {type(password)}"
        assert len(password) > 0, "user password cannot be empty"
        self.password = password
        assert type(name) == str, f"user name shoud be string instead of {type(name)}"
        for i in name:
            assert i.isalpha() or i == " ", f"user name {name} should only contain alphabetical character or white space"
        self.name = name
        assert role in ['student','staff','other'], f"user role shoud only be 'student', 'staff' or 'other'"
        self.role = role
        self.department = department
        self.borrowed_book = []
        self.fine = 0
        if self.ID in userdict:
            raise CustomKeyError(f"Duplicated UserID {self.ID} detected in CSV file")
        userdict[self.ID] = self
        User.instances.append(self)

    def get_id(self)->str:
        '''
        this method returns userID
        '''
        return self.ID

    def get_password(self)->str:
        '''
        this method returns user password
        '''
        return self.password

    def get_name(self)->str:
        '''
        this method returns uer name
        '''
        return self.name

    def get_role(self)->str:
        '''
        this method returns user role
        '''
        return self.role

    def get_department(self)->str:
        '''
        this function returns user department
        '''
        return self.department

    def __str__(self)->str:
        '''
        to string method, used to output (some, but not all) important information when print the user instance.
        '''
        return(f"name: {self.name}\nID: {self.ID}\nrole: {self.role}\ndept: {self.department}\n")

    def is_admin(self)->bool:
        """
        this method returns true if the user is an admin, and false otherwise
        what count as an admin? if the user role is "staff" and user deparment is "Library"
        """
        return(self.get_role() == "staff" and self.get_department() == "Library")

    def time_allowed(self)->int:
        '''
        this method return the user's allowed book borrow time based on the policy
        '''
        return borrow_policy_physical[self.get_role()]

    def quota_allowed(self)->int:
        '''
        this method return the user's allowed book quota time based on the policy
        '''
        return borrow_quota_physical[self.get_role()]

    def get_grace(self)->int:
        '''
        this method return the user's allowed grace period based on the policy
        '''
        return grace_period[self.get_role()]

    def get_fine(self)->float:
        '''
        this method return the user's fine per overdue day based on the policy
        '''
        return fine_rate[self.get_role()]

    def get_loan_list(self,list_with_extension = False)->list:
        '''
        this method returns the User.borrowed_book list
        this list contains all user instance

        if list_with_extension is set to True (default false)
        it will return the full nested list instead
        '''
        return self.borrowed_book

    def get_loan_amount(self)->int:
        '''
        this method returns how many active quota the user have
        online book does not contribute to the quota
        '''
        length = 0
        for book_id in self.borrowed_book:
            if book.get_book(book_id).getType() == "physical":
                length += 1
        return length

    def add_loan(self,book_id:str)->None:
        '''
        this method takes in book_id, and add it to the loaned book list of the user
        '''
        self.borrowed_book.append(book_id)

    def remove_loan(self,book_id:str)->None:
        '''
        this method takes in book_id, and remove it from the loaned book list of the user
        '''
        self.borrowed_book.remove(book_id)

    def exceed_quota_check(self)->bool:
        '''
        this method determines if user has exceed the allowed quota
        '''
        if self.get_loan_amount() >= int(self.quota_allowed()):
            return True
        else:
            return False

    @abstractmethod
    def role_belong(self)->str:
        '''
        this abstractmethod returns user's role in UpperCase
        '''
        pass

class Student(User):
    def role_belong(self)->str:
        '''
        this method returns string "Student"
        '''
        return "Student"

class Staff(User):
    def role_belong(self)->str:
        '''
        this method returns string "Staff"
        '''
        return "Staff"

class Other(User):
    def role_belong(self)->str:
        '''
        this method returns string "Others"
        '''
        return "Others"

def setup_user(userfile: str)->int:
    '''
    a special setup function that takes in a compatable csv file path and 
    turn each entry into an user instance (this is considered as side effect).
    it will skip headers and empty lines, some value can be empty.
    it will return 0 if program finish successfully, or 1 if encounters error
    '''
    #this ensures the function will only be called once per execution
    if type(userfile) != str:
        raise CustomTypeError(f"Expected a string input, got {type(userfile)} instead.")

    if userfile[-4:] != '.csv':
        raise CustomValueError("User File need to be in .csv format")
    try:
        with open(userfile,'r') as test_file:
            pass
    except FileNotFoundError:
        raise CustomValueError("Cannnot open userfile")
    except IOError:
        raise CustomValueError("Cannot read userfile")

    if userdict != {}:
        return 0

    with open(userfile, "r") as user_file:
        #this takes in a csv formatted file and returns an iterable, each instance is a list
        try:
            users = csv.reader(user_file)
        except:
            raise CustomValueError(f"cannot read user file as csv file!")
        next(users, None) #this line skips the header
        for user_info in users:
            if user_info != []:
                if len(user_info) != 5:
                    raise CustomValueError(f"user_info should contain 5 columns, got {len(user_info)} instead")
                ID = user_info[0]
                password = user_info[1]
                name = user_info[2]
                role = user_info[3]
                department = user_info[4]
                if ID == "":
                    raise MissingRequiredFieldError("user must be non empty id") 
                if password == "":
                    raise MissingRequiredFieldError("user must be non empty password")
                if name == "":
                    raise MissingRequiredFieldError("user name must be non empty")
                for char in name:
                    if not char.isalpha() and char != ' ':
                        raise CustomValueError(f"user name {name} must contain only alphabetic characters.")
                for char in ID[1:]:
                    if not char.isdigit():
                        raise CustomValueError(f"user ID {ID} must be in following format: char+digits.")
                if role == "":
                    raise MissingRequiredFieldError("user role must not be empty")
                if role not in ['student','staff','other']:
                    raise CustomValueError(f"user role can only be 'student','staff' or 'other', got '{role}' instead")
                # this will create instance from different subclass based on their role
                match role:
                    case "student":
                        if ID[0] != 's':
                            raise CustomValueError("Student id must start with s")
                        if department not in ['IT','Business','Arts','Science','Engineering','Education','Medicine','Library']:
                            raise CustomValueError("Student does not have correct department")
                        Student(ID,password,name,role,department)
                    case "staff":
                        if ID[0] != 'e':
                            raise CustomValueError("Staff id must start with e")
                        if department not in ['IT','Business','Arts','Science','Engineering','Education','Medicine','Library']:
                            raise CustomValueError("Staff does not have correct department")
                        Staff(ID,password,name,role,department)
                    case "other":
                        if ID[0] != 'o':
                            raise CustomValueError("Other user id must start with o")
                        if department != '':
                            raise CustomValueError("Department for other user should be empty")
                        Other(ID,password,name,role,department)
                
    return 0

def get_user(user_id: str)-> Student | Staff | Other | int:
    '''
    if user_id is in database, this function will return the user instance that matches the input id
    it will return -1 if it cannot find a matching instance
    '''
    if type(user_id) != str:
        raise CustomTypeError(f"Expected a string input, got {type(user_id)} instead.")
    if user_id in userdict:
        return userdict[user_id]
    else:
        raise CustomKeyError(f"Cannot find userID {user_id} in database.")
        return 1



import csv
import datetime
import re
import user
import book
from custom_errors import *


TODAY = "15/09/2025"
loandict = {}
user_lookuptable = {}
book_lookuptable = {}

class Loan():
    # your code goes here
    '''
    This is a class that stores the loan information, and related functions.
    it contains following instance variable fields:
    -user_id,book_id,borrow_date,due_date,return_date,surrogate_key
    it also contain the following class variable fields:
    -instances, surrogate_key
    the surrogate_key is automatically created when creating a new instance.
    the class contains following methods:
    __init__(), get_user(), get_book(), get_due_date(), active_loan(), set_return_date(), overdue_by_date()
    for more details please lookup their respective docstrings
    '''
    instances = []
    surrogate_key = 0

    def __init__(self,user_id: str,book_id: str,borrow_date: str,due_date: str,return_date: str)-> None:
        '''
        this is the constructor, 
        it takes in user ID, book ID, borrow date, due date, return date and creates a class instance
        return_date date can be empty
        when an instance is created, a new unique surrogate_key is also created and assigned to this instance.
        it will also add itself to the Loan.instance list, the loandict[surrogate_key]
        it will also update the user_lookuptable from "user" module
                        and the book_lookuptable from "book" module respectively.
        
        as a rule of thumb, you should never construct a new loan entity manually using this constructor,
        as it will cause desync between User and Book class.
        you should use setup_loan_entry() instead.
        '''
        assert isinstance(user_id, str), "user_id {user_id} should be a string"
        assert isinstance(book_id, str), "book_id {book_id} should be a string"
        assert isinstance(borrow_date, str), "borrow_date {borrow_date} should be a string"
        assert isinstance(due_date, str), "due_date {due_date} should be a string"
        assert isinstance(return_date, str), "return_date {return_date} should be a string"
        self.surrogate_key = Loan.surrogate_key
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = return_date
        self.extension = False
        Loan.instances.append(self)
        loandict[self.surrogate_key] = self
        if self.user_id in user_lookuptable:
            user_lookuptable[self.user_id].append(self.surrogate_key)
        else:
            user_lookuptable[self.user_id] = [self.surrogate_key]

        if self.book_id in book_lookuptable:
            book_lookuptable[self.book_id].append(self.surrogate_key)
        else:
            book_lookuptable[self.book_id] = [self.surrogate_key]

        Loan.surrogate_key += 1

    def get_user(self)-> str:
        '''
        this method returns user_id in the instance
        '''
        return self.user_id

    def get_extension(self)->bool:
        '''
        this method checks if the particular lona entry has been extended, returns a boolean value 
        '''
        return self.extension

    def set_extension(self,extension:bool)->None:
        '''
        this method set the extension value (a boolean value) as extension input
        '''
        assert isinstance(extension, bool), "extension should be a boolean value?"
        self.extension = extension

    def get_book(self)-> str:
        '''
        this method returns book_id in the instance
        '''
        return self.book_id

    def get_due_date(self)-> str:
        '''
        this method returns due_date in the instance
        '''
        return self.due_date

    def active_loan(self)-> bool:
        '''
        this method checks if the instance can be considered as "active loan"
        an active loan is a loan where its return date is empty
        '''
        if self.return_date == "":
            return True
        else:
            return False

    def set_due_date(self,date:str)->None:
        '''
        this method modify the loan instance directly, and set the due date to input date
        '''
        assert isinstance(date, str), "date should be a str value?"
        self.due_date = date

    def set_return_date(self,date:str)->None:
        '''
        this method modify the loan instance directly, and set the return date to input date
        '''
        assert isinstance(date, str), "date should be a str value?"
        self.return_date = date

    def overdue_by_date(self)->int:
        '''
        this method calculate the amount of days the book is overdue.
        it calculate the datedifference between the due_date and today.
        the result cannot be negative, if it is negative it will return 0 instead.
        '''
        difference = datetime.datetime.strptime(TODAY,'%d/%m/%Y') - datetime.datetime.strptime(self.get_due_date(),'%d/%m/%Y')
        return max(0,difference.days)

    def can_renew(self)->bool:
        '''
        this method calculate the amount of days the book is overdue.
        it calculate the datedifference between the due_date and today.
        the result cannot be negative, if it is negative it will return 0 instead.
        '''
        difference = datetime.datetime.strptime(TODAY,'%d/%m/%Y') - datetime.datetime.strptime(self.get_due_date(),'%d/%m/%Y')
        return (difference.days < 0)

    def __str__(self)-> str:
        '''
        to string method, used to output (some, but not all) important information when print the user instance.
        '''
        return(f"user: {self.book_id} loaned {self.book_id} on {self.borrow_date}\n")

def lookup_by_Skey(key:str)->Loan | int:
    '''
    this function takes in an surrogate key and try to lookup the loan instance associate with it in the loandict.
    if it cannot find the corresponding instance, it will return 1 instead.
    '''
    assert isinstance(key, str), "key should be a str value?"
    if key in loandict:
        return loandict[key]
    else:
        print("warning! key not in database!")
        return 1

def lookup_by_user(userid:str,keep_old_record:bool = True)->list:
    '''
    this function takes in the user_id, and optionally a bool value keep_old_record
    it will return a list of matching loan instances that has the user_id.
    
    keep_old_record is set to true as default, and if keep_old_record is set to false,
    it will ignore loan instances that have already been returned
    '''
    assert isinstance(userid, str), "userid should be a str value?"
    assert isinstance(keep_old_record, bool), "keep_old_record should be a boolean value?"
    result = []
    if userid in user_lookuptable:
        keylist = user_lookuptable[userid]
        for key in keylist:
            if keep_old_record or lookup_by_Skey(key).active_loan():
                result.append(lookup_by_Skey(key))
    return result

def lookup_by_book(bookid:str,keep_old_record:bool = True)->list:
    '''
    this function takes in the book_id, and optionally a bool value keep_old_record
    it will return a list of matching loan instances that has the book_id.
    
    keep_old_record is set to true as default, and if keep_old_record is set to false,
    it will ignore loan instances that have already been returned
    '''
    assert isinstance(bookid, str), "bookid should be a str value?"
    assert isinstance(keep_old_record, bool), "keep_old_record should be a boolean value?"
    result = []
    if bookid in book_lookuptable:
        keylist = book_lookuptable[bookid]
        for key in keylist:
            if keep_old_record or lookup_by_Skey(key).active_loan():
                result.append(lookup_by_Skey(key))
    return result

def lookup_by_both(userid:str,bookid:str,keep_old_record:bool = True)->list:
    '''
    this function takes in the user_id, book_id, and optionally a bool value keep_old_record
    and try to find a list of matching loan instances that contains both user_id and book_id.
    
    keep_old_record is set to true as default, and if keep_old_record is set to false,
    it will ignore loan instances that have already been returned
    '''
    assert isinstance(userid, str), "userid should be a str value?"
    assert isinstance(bookid, str), "bookid should be a str value?"
    assert isinstance(keep_old_record, bool), "keep_old_record should be a boolean value?"
    user_borrowed_list = lookup_by_user(userid,keep_old_record)
    book_borrowed_list = lookup_by_book(bookid,keep_old_record)
    result = []
    for instance in user_borrowed_list:
        if instance in book_borrowed_list:
            result.append(instance)
    return result

def setup_loan(loanfile: str)-> None:
    '''
    a special setup function that takes in a compatable csv file path and turn each entry into an Loan instance.
    it will skip headers and empty lines, some value can be empty.
    '''
    #this ensures the function will only be called once per execution
    if type(loanfile) != str:
        raise CustomTypeError(f"loan file should be a str, got {type(loanfile)} instead.")
    
    try:
        with open(loanfile,'r') as test_file:
            pass
    except FileNotFoundError:
        raise CustomValueError("Cannnot open loanfile")
    except IOError:
        raise CustomValueError("Cannot read loanfile")

    if loandict != {}:
        return 0

    with open(loanfile, "r") as loan_file:
        #this takes in a csv formatted file and returns an iterable, each instance is a list
        loans = csv.reader(loan_file)
            
        next(loans,None) # this skips the header line
        for loan_info in loans:
            assert type(loan_info) == list, f"error: loan_info loan output from csv.reader() should be list"
            if len(loan_info) > 0: # this is to skip empty lines
                # this is setup to avoid crash if the input csv file coantains error
                if len(loan_info) != 5:
                    raise CustomValueError(f"loan_info should contain 5 columns, got {loanfile} instead.")
                user_id = loan_info[0]
                book_id = loan_info[1]
                borrow_date = loan_info[2]
                due_date = loan_info[3]
                return_date = loan_info[4]
                setup_loan_entry(user_id,book_id,borrow_date,due_date,return_date)
    return 0

def setup_loan_entry(user_id:str,book_id:str,borrow_date:str,due_date:str,return_date:str)->None:
    '''
    this function setsup individual loan entry, it also update user_instance and book_instance as well.
    as a rule of thumb, you should never construct a new loan entity manually without using this function
    '''
    assert type(user_id) == str, f"user_id should be string, got {type(user_id)} instead"
    assert type(book_id) == str, f"book_id should be string, got {type(book_id)} instead" 
    assert type(borrow_date) == str, f"borrow_date should be string, got {type(borrow_date)} instead" 
    assert type(due_date) == str, f"due_date should be string, got {type(due_date)} instead" 
    assert type(return_date) == str, f"return_date should be string, got {type(return_date)} instead" 
    if user_id not in user.userdict.keys():
        raise UserNotFoundError(f"user {user_id} is not in the library database!")
    if book_id not in book.bookdict.keys():
        raise BookNotFoundError(f"book {book_id} is not in the library database!")
    try:
        borrow_date_datetime = datetime.datetime.strptime(borrow_date,'%d/%m/%Y')
    except:
        raise CustomDateError("borrow_date should follow '%d/%m/%Y' format")
    try:
        due_date_datetime = datetime.datetime.strptime(due_date,'%d/%m/%Y')
    except:
        raise CustomDateError("due_date should follow '%d/%m/%Y' format")
    try:
        if return_date != "":
            return_date_datetime = datetime.datetime.strptime(return_date,'%d/%m/%Y')
    except:
        raise CustomDateError(f"return_date should follow '%d/%m/%Y' format, got {return_date}")
    difference = due_date_datetime - borrow_date_datetime
    if difference.days < 0:
        raise CustomDateError("return date is before due date")
    difference = borrow_date_datetime - datetime.datetime.strptime(TODAY,'%d/%m/%Y')
    if difference.days > 0:
        raise CustomDateError("borrow day is in the future")
    Loan(user_id,book_id,borrow_date,due_date,return_date)
    user_instance = user.get_user(user_id)
    user_instance.add_loan(book_id)
    book_instance = book.get_book(book_id)
    book_instance.add_owner(user_id)

def borrow_book(user_id:str,book_name:str)->None:
    '''
    this function takes in user_id and book_name, and:
    -if neither book name is in database, nor does book name being a book id in database, return early
    -otherwise, if the book name is not an id, output the book information (can be multiple book instance)
     and asks user to input the id of the book the user wants
    -user can only borrow book if:
        -Copies are still available. Online books are always available and not counted 
            toward the borrowing quota.
        -User havs not exceeded his borrowing quota.
        -User does not have any outstanding fines.
        -User can type quit to exit the borrow and return console and go back to main menu.
    -if user can borrow book, the function will update all the classes, dictionary and lists accordingly
    '''
    assert type(user_id) == str, f"user_id should be string, got {type(user_id)} instead"
    assert type(book_name) == str, f"book_name should be string, got {type(user_id)} instead"
    if book_name in book.bookdict:
        borrow_book_id = book_name
        book_id = borrow_book_id
        book_instance = book.get_book(book_id)
        book_type = book_instance.getType()
        name = book_instance.getTitle()
        book_author = book_instance.getAuthor()
        book_year = book_instance.getYear()
        active_loan_record = lookup_by_book(book_id, False)
        total_amount = total_amount = int(book_instance.getCopies())
        available_amount = max(0,total_amount - len(active_loan_record))
        print(f"Found 1 book(s).")
        print(f"- {book_id} ({book_type}) '{name}' by {book_author} ({book_year}). Available copies: {available_amount}/{total_amount}.")
        id_list = [borrow_book_id]
    else:
        result = book.find_book_by_name(book_name)
        if result == []:
            print(f"No book match '{book_name}'")
            return
        else:
            id_list = []
            print(f"Found {len(result)} book(s).")
            for book_instance in result:
                book_id = book_instance.getID()
                book_type = book_instance.getType()
                book_author = book_instance.getAuthor()
                name = book_instance.getTitle()
                book_year = book_instance.getYear()
                total_amount = int(book_instance.getCopies())
                active_loan_record = lookup_by_book(book_id, False)
                available_amount = max(0,total_amount - len(active_loan_record))
                id_list.append(book_id)
                if book_type == 'online': #if book is online book, available copy and total copy will always be 0
                    available_amount = 0
                    total_amount = 0
                print(f"- {book_id} ({book_type}) '{name}' by {book_author} ({book_year}). Available copies: {available_amount}/{total_amount}.")
    while True: #this program will run forever until user input correctly
        borrow_book_id = input("Confirm the Book ID you'd like to borrow: ")
        if borrow_book_id in id_list:
            break
    #back to This, we already know the borrow_book_id is valid, no need to check now, only need to check if it is allowed:
    if book.get_book(borrow_book_id).all_lent():
        print("No copies available.")
        return
    if user.get_user(user_id).exceed_quota_check():
        print("Borrowing unavailable: quota reached. Review your loan details for more info.")
        return
    if user_has_fine(user_id):
        print("Borrowing unavailable: unpaid fines. Review your loan details for more info.")
        return
    # okay, we have managed to borrow a book, time to update the database
    book_instance = book.get_book(borrow_book_id)
    book_name = book_instance.getTitle()
    book_author = book_instance.getAuthor()
    book_year = book_instance.getYear()
    due_date = (datetime.datetime.strptime(TODAY,'%d/%m/%Y') + datetime.timedelta(days=user.get_user(user_id).time_allowed())).strftime('%d/%m/%Y')
    print(f"You have borrowed '{book_name}' by {book_author} ({book_year}). Due: {due_date}.")
    setup_loan_entry(user_id,borrow_book_id,TODAY,due_date,'')

def user_has_fine(userID:str)->bool:
    '''
    this is a helper function that takes in userID, and return true if user has outstanding fine and false otherwise.
    
    If a user returns a physical book after its due date, or if the due date has already passed and the book 
    remains unreturned (e.g., as of today, 15/09/2025), a fine will be applied. Online books are exempt from fines, 
    as access to these resources is automatically revoked by the reading platform once the due date has passed.

    Fines accrue only from the day after the due date (including any applicable grace period) and continue until the item 
    is returned. For items that are still on loan, fines are calculated up to today’s date (15/09/2025). 
    All fines are expected to be paid in full upon the return of the book.
    '''
    fines = 0.0
    #we are using the same strategy from the loan_detail() function:
    #step 4. calculate the amount of physical and digital copy loaned respectively.
    loaned_list = lookup_by_user(userID)
    user_instance = user.get_user(userID)
    for loan_instance in loaned_list:
        if loan_instance.active_loan():
            bookID = loan_instance.get_book()
            book_instance = book.get_book(bookID)
            booktype = book_instance.getType()
            if booktype == "physical":
                fines += (loan_instance.overdue_by_date() - user_instance.get_grace()) * user_instance.get_fine()
    if fines>0:
        return True
    else:
        return False
    pass

def return_book(user_id:str,book_id:str)->None:
    '''
    this helper function takes in userID and bookID and attempt to update the database.
    
    if the book id is not in the record, this function will print out:
        "No loan record for {book_id}."

    When a book is returned, the system will automatically set the return date to the current day 
    (TODAY), calculate any applicable fines, and display the result:
        "Returned '{book_name}' by {book_author} ({book_year})."
        (possible) "Overdue by {loan_record.overdue_by_date()} day(s)."
        (possible) "Fine: $ {'{:.2f}'.format(max(0,fine))}"
    
    If the user has borrowed multiple copies of the same book, 
    the system will return the copy (or loan) with the earliest due date first.
    '''
    assert isinstance(user_id, str), "user_id should be a string?"
    assert isinstance(book_id, str), "book_id should be a string?"
    if book_id not in user.get_user(user_id).get_loan_list():
        print(f"No loan record for {book_id}.")
        return
    else:
        book_instance = book.get_book(book_id)
        user_instance = user.get_user(user_id)
        book_name = book_instance.getTitle()
        book_author = book_instance.getAuthor()
        book_year = book_instance.getYear()
        result = f"Returned '{book_name}' by {book_author} ({book_year})."
        #now we need to determine the entry, we need the first entry:
        loan_record = lookup_by_both(user_id,book_id,False)[0]
        if loan_record.overdue_by_date()>0:
            result += f" Overdue by {loan_record.overdue_by_date()} day(s)."
            fine = (loan_record.overdue_by_date() - user_instance.get_grace()) * user_instance.get_fine()
            result += f" Fine: $ {'{:.2f}'.format(max(0,fine))}"
        user_instance.remove_loan(book_id)
        book_instance.remove_owner(user_id)
        loan_record.set_return_date(TODAY)
        print(result)
    pass

def renew_book(user_id,book_id):
    """
    this function takes in user_id and book name and attempt the extend the due date of said book by 5 days.
    
    A book is not eligible for renewal if:
    -Its extended due date has already passed (making it overdue). An error message
        "Renewal denied: This book is already overdue." 
    will be printed out instead.
    -If it is already renewed once by the user, the system will display 
        "Renewal unavailable: Each book can only be renewed once."
    -Users with unpaid fines cannot renew any loans until their fines are settled. The system will display 
        "Renewal denied: You have unpaid fines."
    """
    assert isinstance(user_id, str), "user_id should be a string?"
    assert isinstance(book_id, str), "book_id should be a string?"
    if user_has_fine(user_id):
        print("Renewal denied: You have unpaid fines.")
        return
    user_loaned_books = lookup_by_both(user_id,book_id,False)
    if len(user_loaned_books) == 0:
        print(f"No loan record for {book_id}.")
        return
    all_overdue = True
    all_renewed = True
    for loan_instance in user_loaned_books:
        if loan_instance.can_renew():
            all_overdue = False
            if loan_instance.get_extension() == False:
                all_renewed = False
                loan_instance.set_extension(True)
                new_due_date = (datetime.datetime.strptime(loan_instance.get_due_date(),'%d/%m/%Y') + datetime.timedelta(days=5)).strftime('%d/%m/%Y')
                loan_instance.set_due_date(new_due_date)
                book_instance = book.get_book(book_id)
                book_name = book_instance.getTitle()
                book_author = book_instance.getAuthor()
                book_year = book_instance.getYear()
                print(f"Renew '{book_name}' by {book_author} ({book_year}) successfully. New due date: {new_due_date}")
                return
    if all_overdue:
        print("Renewal denied: This book is already overdue.")
        return
    if all_renewed:
        print("Each book can only be renewed once.")
        return

from custom_errors import *

import user
import book
import csv
import datetime
import loan

from user import TODAY

def main(user_file: str, book_file:str, loan_file:str) -> None:
    """
    This is the entry of your program. Please DO NOT modify this function signature, i.e. function name, parameters
    Parameteres:
    - user_file (str): path the `users.csv` which stores user information
    - book_file (str): path the `books.csv` which stores book information
    - loan_file (str): path the `loans.csv` which stores loan information
    """
    # Your implemetation goes here
    #set up all three dataset as classes
    try:
        user_setup_failure = user.setup_user(user_file)
    except CustomTypeError as E:
        print("CustomTypeError:",E)
        return
    except CustomValueError as E:
        print("CustomValueError:",E)
        return
    except MissingRequiredFieldError as E:
        print("MissingRequiredFieldError:",E)
        return
    except Exception as E:
        print("User Setup Failed:",E)
        return
    try:
        book_setup_failure = book.setup_book(book_file)
    except CustomTypeError as E:
        print("CustomTypeError:",E)
        return
    except CustomValueError as E:
        print("CustomValueError:",E)
        return
    except MissingRequiredFieldError as E:
        print("MissingRequiredFieldError:",E)
        return
    except Exception as E:
        print("Book Setup Failed:",E)
        return
    try:
        loan_setup_failure = loan.setup_loan(loan_file)
    except CustomTypeError as E:
        print("CustomTypeError:",E)
        return
    except CustomValueError as E:
        print("CustomValueError:",E)
        return
    except MissingRequiredFieldError as E:
        print("MissingRequiredFieldError:",E)
        return
    except Exception as E:
        print("Loan Setup Failed:",E)
        return
    # safety net to exit before crashing
    if(user_setup_failure or book_setup_failure or loan_setup_failure):
        print("setup failed..")
        return

    userID = loginMenu()
    #unlike mainMenu() function below, we need to manually stop this progam if user quit during login session
    assert type(userID) in (str,int), "login menu() should return a str or int"
    if userID == -1: 
        print("Goodbye!")
        return
    else:
        user_instance = user.get_user(userID)
        print(f"Logged in as {user_instance.get_name()} ({user_instance.role_belong()})")
        mainMenu(user_instance,user_file,book_file,loan_file)
    pass

def loginMenu()->int | str:
    """
    this is the first part of the program, it controls the login pageg

    user are required to input their user name and password here to access the main main menu
    If the user id does not exist or user id and password does not match, 
    the program will print "Invalid credentials. x attempt(s) remaining." and prompt user to login again.

    each user has three opportunities and afterwards
    the program prints a message "Sorry you're out of attempts. Please contact your librarian for assistance." 
    and back to welcome and login menu.
    
    user can also input "quit" as username to terminate the program.

    this function will return the (order) id of the user stored in userinstance class after successful login
    however it can also return -1, if the user want to quit the program directly
    """
    attemptleft = 3
    print("Welcome to Library")
    while True: #this part will loop forever until either user correct login, exceed maximum attempt or quit the program
        if attemptleft <= 0:
            print("Sorry you're out of attempts. Please contact your librarian for assistance.")
            return loginMenu() #it will terminate the current session and reopen a new loginMenu()
        userID = input("Login as: ")
        if userID == "quit":
            return -1
        userpwd = input("Password: ")
        if userID in user.userdict:
            correct_password = user.get_user(userID).get_password()
            if userpwd == correct_password:
                return userID
        attemptleft -= 1
        if attemptleft > 0:
            print("Invalid credentials.",attemptleft,"attempt(s) remaining.")

def mainMenu(userinstance:user.Student|user.Staff|user.Other, user_file: str, book_file:str, loan_file:str)->None:
    '''
    this is the second part of the program
    after user successfully log in, the user will be directed here.
    this program takes in
    -userinstance(the instance of the current user)
    -user_file: filepath to users.csv
    -book_file: filepath to books.csv
    -loan_file: filepath to loans.csv

    based on user's access level they will have 4 or 5 options to choose from:
    -quit the program:
    -log out:
    -view account policy
    -view my loans
    -(admin only)library report

    when user quit the program, the program will print "goodbye" then terminate.

    when viewing account policy, the program will display user current membership policies, 
    and their total loans.
    
    when viewing the user's loands, the program will display all active loans (sorted by due date). 
    Active loans are those without a returned date.
    
    when viewing library reports, the program provides key statistics, 
    including the total number of users (with a breakdown by role), 
    as well as details about the book collection and available books which 
    currently have one or more copies available.
    '''
    assert isinstance(userinstance, user.Student) or isinstance(userinstance, user.Staff) or isinstance(userinstance, user.Other), "user instance should be a user class instance"
    assert isinstance(user_file, str),f"user_file {user_file} should be a string?"
    assert isinstance(book_file, str),f"book_file {book_file} should be a string?"
    assert isinstance(loan_file, str),f"loan_file {loan_file} should be a string?"
    userRole = userinstance.role_belong()
    print("==================================")
    print("My Library Account")
    print("0. Quit")
    print("1. Log out")
    print("2. View account policies")
    print("3. View my loans")
    print("4. Borrow and Return")
    print("5. Search by Keywords")
    if userinstance.is_admin(): #admin has one more menu
        print("6. Manage Library")
    print("==================================")
    while True: #this will run forever until user has input valid command
        userAction = input("Enter your choice: ")
        #the range of command is different based on their access level
        if (userinstance.is_admin() and userAction in ['0','1','2','3','4','5','6']) or userAction in ['0','1','2','3','4','5']:
            break
    # The program will print the message: "Goodbye!", and terminates.
    if userAction == "0":
        print("Goodbye!")
        return
    # this will return to the main menu (then login page)
    if userAction == "1":
        main(user_file,book_file,loan_file)
    # this will print out the user policy with loancheck() helper function
    # then return to main menu page
    if userAction == "2":
        output = f"{userRole} {userinstance.get_name()}. Policies: maximum of {userinstance.time_allowed()} days, {userinstance.quota_allowed()} items."
        output += loancheck(userinstance.get_id())
        print(output)
        mainMenu(userinstance,user_file,book_file,loan_file)
    # this will output user loan detail with the helper function loan_detail()
    # then it will return to main menu 
    if userAction == '3':
        loan_detail(userinstance.get_id())
        mainMenu(userinstance,user_file,book_file,loan_file)
    # this will go to borrow/return page, which handles related fields
    # after exiting the borrow/return program, it will return to main menu
    if userAction == '4':
        borrow_return(userinstance.get_id())
        mainMenu(userinstance,user_file,book_file,loan_file)
    # 
    if userAction == '5':
        book.search_engine()
        mainMenu(userinstance,user_file,book_file,loan_file)
    # this will output library detail with library_detail() helper function
    if userAction == '6':
        library_manager()
        mainMenu(userinstance,user_file,book_file,loan_file)
    # then it will return to main menu
    
def loancheck(userID:str)->str:
    '''
    this function takes in user id and return a string that displays user's loan status
    the string has the following format:
     Current loans: {number} ({number} physical / {number} online).
    example:
     Current loans: 2 (1 physical / 1 online).
    '''
    assert isinstance(userID, str),f"userID {userID} should be a string?"
    physicalCopy = 0
    onlineCopy = 0
    fines = 0.0
    loaned_list = loan.lookup_by_user(userID)
    user_instance = user.get_user(userID)
    # we are looking through loaned list, which is a list of loan instance that contains user id
    # then we add each active loan to physical/online copy, as well as calculate fines for overdued physical books.
    for instance in loaned_list:
        if instance.active_loan():
            bookID = instance.get_book()
            bookinstance = book.get_book(bookID)
            booktype = bookinstance.getType()
            assert isinstance(booktype, str),f"booktype {booktype} should be a string?"
            if booktype == "physical":
                physicalCopy += 1
                fines += (instance.overdue_by_date() - user_instance.get_grace()) * user_instance.get_fine()
            elif booktype == "online":
                onlineCopy += 1
            else: # if this happens, that means some book have type other 
                  # than physical or online, should contact support.
                return("fatal error: book type not physical nor online")
    return(f" Current loans: {physicalCopy+onlineCopy} ({physicalCopy} physical / {onlineCopy} online). Fines: $ {'{:.2f}'.format(max(fines,0))}")

def loan_detail(userID: str)->None:
    """
    this function takes in userID and output the user's loan details based on the database created.
    this function does not return anything, but does have side effect (print string on screen).
    the format is follows:

    You are currently have {number} loan(s).
    {number}. {book id} {book title} by {author}, Due date: {due date}

    example:
    You are currently have 2 loan(s).
    1. P0006 'Hands-On ML' by Aurelien Geron (2019). Due date: 13/09/2025.
    2. P0001 'Introduction to Python Programming' by S Gowrishankar (2019). Due date: 15/09/2025.
    """
    assert isinstance(userID, str),f"userID {userID} should be a string?"
    activeLoanCount = 0
    activeloans = []
    # we are looking through loaned list, which is a list of loan instance that contains user id
    loaned_list = loan.lookup_by_user(userID)
    assert isinstance(loaned_list, list),f"loaned_list {loaned_list} should be a string?"
    for instance in loaned_list:
        assert isinstance(instance, loan.Loan),f"instance should be a Loan instance?"
        if instance.active_loan(): #if it is active loan, we need to construct a message
            #print("it is active")
            bookID = instance.get_book()
            dueDate = instance.get_due_date()
            book_instance = book.get_book(bookID)
            bookTitle = book_instance.getTitle()
            bookAuthor = book_instance.getAuthor()
            bookYear = book_instance.getYear()
            activeloans.append(f"{bookID} '{bookTitle}' by {bookAuthor} ({bookYear}). Due date: {dueDate}.")
            activeLoanCount += 1 #this will be used to calculate the total amount of book loaned
    print(f"You are currently have {activeLoanCount} loan(s).")
    for i,loanString in enumerate(activeloans):
        print(f"{i+1}. {loanString}") #this part add the first "1. " bit of the response

def borrow_return(user_id:str)->None:
    '''
    this function takes in user_id, asks user's input, deciper it, and determine what to do next:

    -The user can input borrow <X> where <X> is either a book title or book ID. 

    -If multiple books share the same title, the program will display a list of 
     all matching books along with their IDs (sorted by book IDs). You will then 
     be asked to confirm the book by entering its ID. The book ID must be one from 
     the displayed list. If you enter an invalid ID, the program will prompt you again 
     until a valid ID is provided or you type quit.
    
    -A book can only be borrowed if 
        -It exists in the library catalog.
        -Copies are still available. Online books are always available and not counted 
            toward the borrowing quota.
        -User havs not exceeded his borrowing quota.
        -User does not have any outstanding fines.
        -User can type quit to exit the borrow and return console and go back to main menu.

    -if user's input does not begin with a correct command name ("borrow", "return", or "quit"). 
     the program should prompt for input again.
    '''
    assert isinstance(user_id, str),f"user_id {user_id} should be a string?"
    while True:
        userinput = input("> ")
        usercommand = userinput.split(" ")[0] #this separate the command name from the input
        if usercommand == "quit":
            break
        if len(userinput.split(" ")) < 2: #this will never be a valid string, so prompt again
            continue
        if usercommand not in ['borrow','return','renew']:
            continue
        book_name = ' '.join(userinput.split(" ")[1:]) # this reconstructs the book name from the input
        if usercommand == 'borrow':
            loan.borrow_book(user_id,book_name)
        if usercommand == 'return':
            loan.return_book(user_id,book_name)
        if usercommand == 'renew':
            loan.renew_book(user_id,book_name)

def library_manager()->None:
    '''
    this is a helper function
    inside the function the program would prompt the user to input a command, and calls different function based on the command
    the functions getting called can be:
     - library_detail(), if user input "report"
     - book.add_physical_book(), if user input "add physical"
     - book.add_online_book(), if user input "add online"
     - nothing, if user input invalid command
    if the user type in "quit"
    the function will terminate
    otherwise the function will prompt the user again and again
    '''
    while True:
        userInput = input("> ")
        if userInput == "quit":
            return
        if userInput == "report":
            library_detail()
        if userInput == "add physical":
            book.add_physical_book()
        if userInput == "add online":
            book.add_online_book()
    pass

def library_detail()->None:
    '''
    this helper function prints out a summary of the library.
    This report provides key statistics, including the total number of users 
    (with a breakdown by role), as well as details about the book collection and available 
    books which currently have one or more copies available.

    example:
    Library Report
    - 9 users, including 4 student(s), 3 staff and 2 others.
    - 14 books, including 10 physical book(s) (7 currently available) and 4 online book(s).
    '''
    # the first part is to iterate the user list and calculate the user report
    studentCount = 0
    staffCount = 0
    otherCount = 0
    for instance in user.User.instances:
        assert isinstance(instance, user.Student) or isinstance(instance, user.Staff) or isinstance(instance, user.Other), "user instance should be a user class instance"
        if instance.get_role() == "student":
            studentCount += 1
        elif instance.get_role() == "staff":
            staffCount += 1
        elif instance.get_role() == "other":
            otherCount += 1
        else: #if this happens this means some user has invalid user roles, the program should terminate at this point
            print("error: unidentified role detected, please contact admin")
            return
    # the second part is to iterate over the book list and calculate the total book count, physical book and online book count
    physicalBookCount = 0
    onlineBookCount = 0
    physicalBookDict = {} # we also include a dictionary to keep track of the available physical books
    for instance in book.Book.instances:
        assert isinstance(instance, book.PhysicalBook) or isinstance(instance, book.OnlineBook), "book instance should be a physical book class or online book class"
        if instance.getType() == "physical":
            physicalBookCount += 1
            # this line will add one copy to the physical book dictionary under the bookid key
            physicalBookDict[instance.getID()] = int(instance.getCopies())
        elif instance.getType() == "online":
            onlineBookCount += 1
        else: #if this happens this would mean we have an invalid booktype, the program should terminate at this point
            print("error: unidentified book type detected, please contact admin")
            return
    # te last part is to calculate the available bookinstance
    # we achieve this by iterate over loan list and dictionary list, 
    # then substract physical loans from the dictionary one by one
    for instance in loan.Loan.instances:
        assert isinstance(instance, loan.Loan), "loan instance should be a Loan class instance"
        # first, we only want to look for the entries that are active
        if instance.active_loan():
            bookID = instance.get_book()
            # then we look up the book id on book list and check its type
            book_instance = book.get_book(bookID)
            # if it is physical and it matches our id, we will substract one from our dictionary accordingly
            if book_instance.getType() == "physical":
                physicalBookDict[book_instance.getID()]-=1
                # if the value drop to 0, we drop the key from the dictionary since there are no more available books
                if physicalBookDict[book_instance.getID()] == 0:
                    del physicalBookDict[book_instance.getID()]
    # after all the calculation, we will print out the summary
    print("Library report")
    print(f"- {studentCount+staffCount+otherCount} users, including {studentCount} student(s), {staffCount} staff, and {otherCount} others.")
    print(f"- {physicalBookCount+onlineBookCount} books, including {physicalBookCount} physical book(s) ({len(physicalBookDict)} currently available) and {onlineBookCount} online book(s).")
    pass



if __name__ == "__main__":
    main('data/users.csv', 'data/books.csv', 'data/loans.csv')
    #print(book.PhysicalBook.instances)
    #print(book.OnlineBook.instances)

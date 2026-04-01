import csv
import datetime
import re
from custom_errors import *


bookdict = {}

class Book():
    # your code goes here
    '''
    this is a class that stores book information, information stored include:
        -bookid
        -book type (physical or online, physical start with prefix P in id, online has E in id)
        -book copies amount (if book is ebook than it will always be 0)
    '''
    instances = []
    keyword_list = []
    def __init__(self,book_id: str,b_type: str,copies: str,title: str,author: str,year: str,keywords: str)->None:
        '''
        this is the constructor of the class, it takes in book_id,b_type,copies,title,author,year,keywords
        and creates a new book instance. it also append the book to the class list
        '''
        assert isinstance(book_id,str),"book_id should be a string?"
        assert isinstance(b_type,str),"b_type should be a string?"
        assert isinstance(copies,str),"copies should be a string?"
        assert isinstance(title,str),"title should be a string?"
        assert isinstance(author,str),"author should be a string?"
        assert isinstance(year,str),"year should be a string?"
        assert isinstance(keywords,str),"keywords should be a string?"
        self.book_id = book_id.strip()
        self.b_type = b_type.strip()
        self.copies = copies.strip()
        self.title = title.strip()
        self.author = author.strip()
        self.year = year.strip()
        self.keywords = keywords.split(":")
        self.borrowed_by = []
        Book.instances.append(self)
        bookdict[self.book_id] = self
        Book.keyword_list += self.keywords
        Book.keyword_list = list(set(Book.keyword_list))

    def getID(self)-> str:
        '''
        this method returns the book id
        '''
        return self.book_id

    def getCopies(self)-> str:
        '''
        this method returns the book copy amount
        '''
        return self.copies

    def getType(self)-> str:
        '''
        this method returns the book type (physical or online)
        '''
        return self.b_type

    def getAuthor(self)-> str:
        '''
        this method returns the book author
        '''
        return self.author

    def getYear(self)-> str:
        '''
        this method returns the book publish year
        '''
        return self.year

    def getKeywords(self)->list:
        '''
        this method returns the book keywords (a string)
        '''
        return self.keywords

    def getTitle(self)-> str:
        '''
        this method returns the book ttle
        '''
        return self.title
    
    def get_lent_amount(self)->int:
        '''
        this method returns the amount of copies currently being lent
        '''
        return len(self.borrowed_by)

    def add_owner(self,user_id:str)->None:
        '''
        this method should be called when a new user borrows a copy of said book
        it takes the user id and record it to the book borrowed list
        '''
        assert isinstance(user_id, str),"user_id should be a string?"
        self.borrowed_by.append(user_id)

    def remove_owner(self,user_id:str)->None:
        '''
        this method should be called when an user returns a copy of said book
        it takes the user id and remove the first instance of matching user from the book borrowed list
        '''
        assert isinstance(user_id, str),"user_id should be a string?"
        self.borrowed_by.remove(user_id)

    def all_lent(self)->bool:
        '''
        this method returns true if there is no available copy in the library for this book instance
        or false otherwise
        '''
        if self.getType() == "online":
            return False
        if int(self.getCopies()) <= self.get_lent_amount():
            return True
        else:
            return False
        pass

    def __str__(self)-> str:
        '''
        to string method, used to rturn (some, but not all) important information when print the book instance.
        '''
        return(f"id: {self.book_id}\ntitle: {self.title}\nauthor: {self.author}\n")


class PhysicalBook(Book):
    '''
    this is a subclass of Book
    '''
    pass

class OnlineBook(Book):
    '''
    this is a subclass of Book
    '''
    pass

def setup_book(bookfile: str)->int:
    '''
    a special setup function that takes in a compatable csv file path and turn each entry into a book instance.
    it will skip headers and empty lines, some value can be empty.
    '''
    #this ensures the function will only be called once per execution
    if type(bookfile) != str:
        raise CustomTypeError(f"Expected a string input, got {type(bookfile)} instead.")
    try:
        with open(bookfile,'r') as test_file:
            pass
    except FileNotFoundError:
        raise CustomValueError("Cannnot open bookfile")
    except IOError:
        raise CustomValueError("Cannot read bookfile")
    # this makes sure this code will only be run once
    if bookdict != {}:
        return 0

    with open(bookfile, "r") as book_file: 
        #this takes in a csv formatted file and returns an iterable, each instance is a list
        try:
            books = csv.reader(book_file)
        except:
            raise CustomValueError(f"cannot read book file as csv file!")
        next(books,None) #this line skips the header
        for book_info in books:
            if len(book_info)>0: # this removes/ignores empty lines
                if len(book_info) != 7: # this helps avoiding crashing when csv file is invalid
                    raise CustomValueError(f"book_info should contain 7 columns, got {len(user_info)} instead")
                book_id = book_info[0]
                b_type = book_info[1]
                copies = book_info[2]
                title = book_info[3]
                author = book_info[4]
                year = book_info[5]
                keywords = book_info[6]
                setup_book_instance(book_id,b_type,copies,title,author,year,keywords)
    return 0

def setup_book_instance(book_id,b_type,copies,title,author,year,keywords):
    if book_id == '':
        raise MissingRequiredFieldError(f"Book id cannot be empty")
    if book_id[0] not in['P','E']:
        raise CustomValueError(f"Book ID should start with P or E, got {book_id} instead")
    for char in book_id[1:]:
        if not char.isdigit():
            raise CustomValueError(f"starting from second character, book_id should be all numbers, got {book_id} instead")
    if b_type == '':
        raise MissingRequiredFieldError(f"Book type cannot be empty")
    if b_type not in ['physical','online']:
        raise CustomValueError(f"Book type should either be physical or online, got {b_type} instead")
    if copies == '':
        raise MissingRequiredFieldError(f"Copy field should not be empty")
    if not copies.isdigit():
        raise CustomValueError(f"Book copies should be a integer number, got {copies} instead")
    if b_type == 'physical' and int(copies) <= 0:
        raise CustomValueError(f"Physical books should have at least 1 copies, got {copies} instead")
    if b_type == 'online' and int(copies) != 0:
        raise CustomValueError(f"Online books should always have 0 copies, got {copies} instead")
    if title == '':
        raise MissingRequiredFieldError(f"book title cannot be empty")
    if author == '':
        raise MissingRequiredFieldError(f"Book author cannot be empty")
    if year == '':
        raise MissingRequiredFieldError(f"Book year cannot be empty")
    if not (year.isdigit() and len(year) == 4):
        raise CustomValueError(f"Book year should be 4 digit integer, got {year} instead.")
    for char in keywords:
        if not (char.isalpha() or char.isdigit() or char in [':','-',' ']):
            raise CustomValueError(f"keyword should consist of letters and numbers only. The only allowed special character is the hyphen (-), got {keywords} instead.")
    if len(keywords.split(":")) > 5:
        raise CustomValueError(f"each book may have at most 5 keywords")
    if b_type == "physical":
        PhysicalBook(book_id,b_type,copies,title,author,year,keywords)
    elif b_type == "online":
        OnlineBook(book_id,b_type,copies,title,author,year,keywords)
    else:
        print("warning! file contain book with invalid type!")
        print(f"invalid id: {book_id}\ninvalid role: {b_type}")
        return 1
    return 0

def get_book(book_id: str)-> PhysicalBook | OnlineBook | int:
    '''
    this function returns the book instance based on the book_id provided
    it will return 1 if it cannot find the instance
    '''
    if type(book_id) != str:
        raise CustomTypeError(f"Expected a string input, got {type(book_id)} instead.")
    if book_id in bookdict:
        return bookdict[book_id]
    else:
        print("warning! book not in database!")
        return 1

def find_book_by_name(bookname: str)-> list:
    '''
    this function returns a list of book instance based on the book name provided
    '''
    if type(bookname) != str:
        raise CustomTypeError(f"Expected a string input, got {type(bookname)} instead.")
    result = []
    for instances in Book.instances:
        if instances.getTitle() == bookname:
            result.append(instances)
    return result

def add_physical_book()->None:
    '''
    this function asks user for a series of input and create a new physical book instance
    '''
    title = input("Title: ")
    author = input("Authors: ")
    year = input("Year: ")
    copies = input("Copies: ")
    keywordlist = []
    title_to_list = title.lower().split(" ")
    for i in title_to_list:
        if i in Book.keyword_list:
            keywordlist.append(i)
    keywords = ':'.join(sorted(keywordlist))

    maxvalue = 0
    for i in bookdict.keys():
        if i[0] == 'P':
            current_value = int(i[1:])
            if maxvalue < current_value:
                maxvalue = current_value
    maxvalue += 1
    result = f"{maxvalue:04d}"
    book_id = 'P'+result
    setup_book_instance(book_id,'physical',copies,title,author,year,keywords)
    print(f"Detected keywords: {keywords}")
    print(f"Adding {book_id} '{title}' by {author} ({year}).")
    pass

def add_online_book()->None:
    '''
    this function asks user for a series of input and create a new online book instance
    '''
    title = input("Title: ")
    author = input("Authors: ")
    year = input("Year: ")

    keywordlist = []
    title_to_list = title.lower().split(" ")
    for i in title_to_list:
        if i in Book.keyword_list:
            keywordlist.append(i)
    keywords = ':'.join(sorted(keywordlist))

    maxvalue = 0
    for i in bookdict.keys():
        if i[0] == 'E':
            current_value = int(i[1:])
            if maxvalue < current_value:
                maxvalue = current_value
    #reformat book_id
    maxvalue += 1
    result = f"{maxvalue:04d}"
    book_id = 'P'+result
    setup_book_instance(book_id,'physical','0',title,author,year,keywords)
    print(f"Detected keywords: {keywords}")
    pass

def have_overlap(list1:list,list2:list)->int:
    '''
    this is a helper function that takes in two lists, it returns how many keyword matches
    '''
    if type(list1) != list:
        raise CustomTypeError(f"Expected a list input, got {type(list1)} instead.")
    if type(list2) != list:
        raise CustomTypeError(f"Expected a list input, got {type(list2)} instead.")
    overlap_count = 0
    for i in list1:
        if i in list2:
            overlap_count += 1
    return overlap_count

def search_engine()->None:
    '''
    this function asks user for input, look up the database and print out matching instances
    specifically it will try to lookup the value in instances.keywords (which will be transformed into a list, separated by ":")
    '''
    keyword_input = input("Enter search keywords (separated by comma): ")
    keyword_list = keyword_input.split(",")
    foundbook = 0
    result_string = []
    for book_instance in Book.instances:
        instance_keyword = book_instance.getKeywords()
        matched_keywords = have_overlap(instance_keyword,keyword_list)
        if matched_keywords > 0:
            result_order_helper = f"{matched_keywords:02d} {book_instance.getYear()} "
            actual_message = f"{book_instance.getID()} '{book_instance.getTitle()}' by {book_instance.getAuthor()} ({book_instance.getYear()})."
            result_string.append(result_order_helper+actual_message)
            foundbook+=1
    result_string=sorted(result_string,reverse=True)
    print(f"Found {foundbook} book(s).")
    for i, result in enumerate(result_string):
        print(f"{i+1}. {result[8:]}")


if __name__ == "__main__":
    book_info = "P0001,physical,3,Introduction to Python Programming,,2019,python:programming".split(',')
    if len(book_info)>0: # this removes/ignores empty lines
        if len(book_info) != 7: # this helps avoiding crashing when csv file is invalid
            raise CustomValueError(f"book_info should contain 7 columns, got {len(user_info)} instead")
    book_id = book_info[0]
    b_type = book_info[1]
    copies = book_info[2]
    title = book_info[3]
    author = book_info[4]
    year = book_info[5]
    keywords = book_info[6]
    setup_book_instance(book_id,b_type,copies,title,author,year,keywords)













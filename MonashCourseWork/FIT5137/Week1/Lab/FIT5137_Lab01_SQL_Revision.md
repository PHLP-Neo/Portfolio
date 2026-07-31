# FIT5137 Advanced Database Technology

## Lab 1: SQL Revision

## Notes

1. This lab contains two parts:
   - **Part A:** Managing Tables
   - **Part B:** Querying Exercises
2. Attempt every question. The expected average time is approximately four minutes per question.
3. The lecture notes posted on Moodle contain the material required for the exercises.
4. Complete all questions using SQL queries.
5. SQL code may be copied and pasted, but quotation marks copied from Microsoft Word may not be compatible with the SQL editor.
6. Any unfinished questions should be completed before the Week 2 lab.

---

# Part A: Managing Tables

## 1. Inspect Existing Tables

After successfully connecting to Oracle using DBeaver or SQL Developer, execute:

```sql
SELECT *
FROM TAB;
```

Write down your observations.

---

## 2. Create the `LECTURER` Table

```sql
CREATE TABLE LECTURER
(
    StaffNO        NUMBER(6) NOT NULL,
    Title          VARCHAR2(3),
    FName          VARCHAR2(30),
    LName          VARCHAR2(30),
    StreetAddress  VARCHAR2(70),
    Suburb         VARCHAR2(40),
    City           VARCHAR2(40),
    PostCode       VARCHAR2(4),
    Country        VARCHAR2(30),
    LecturerLevel  CHAR(2),
    BankNO         CHAR(20),
    BankName       VARCHAR2(40),
    Salary         NUMBER(8,2),
    WorkLoad       NUMBER(2,1) NOT NULL,
    ResearchArea   VARCHAR2(40),
    PRIMARY KEY (StaffNO)
);
```

---

## 3. Inspect the Table List Again

```sql
SELECT *
FROM TAB;
```

Write down your observations.

---

## 4. Insert Records into `LECTURER`

### 4a. Insert the First Lecturer

```sql
INSERT INTO LECTURER
(
    StaffNO,
    Title,
    FName,
    LName,
    StreetAddress,
    Suburb,
    City,
    PostCode,
    Country,
    LecturerLevel,
    BankNO,
    BankName,
    Salary,
    WorkLoad,
    ResearchArea
)
VALUES
(
    1000,
    'Dr',
    'David',
    'Taniar',
    '3 Robinson Av',
    'Kew',
    'Melbourne',
    '3080',
    'Australia',
    '5',
    '1000567237',
    'CommBank',
    89000.00,
    2.0,
    'O-R DB'
);
```

### 4b. Attempt to Insert a Duplicate Primary Key

```sql
INSERT INTO LECTURER
(
    StaffNO,
    Title,
    FName,
    LName,
    StreetAddress,
    Suburb,
    City,
    PostCode,
    Country,
    LecturerLevel,
    BankNO,
    BankName,
    Salary,
    WorkLoad,
    ResearchArea
)
VALUES
(
    1000,
    'Ms',
    'Julie',
    'Main',
    '6 Algorithm Av',
    'Montmorency',
    'Melbourne',
    '3089',
    'Australia',
    '5',
    '1000123456',
    'CommBank',
    89000.00,
    2.0,
    'CBR'
);
```

Answer the following:

- What happens?
- Why does it happen?

Correct the statement by changing `StaffNO` from `1000` to `2000`.

### 4c. Insert Values Without Listing Column Names

When values are supplied for every column in the table's defined order, the column names may be omitted:

```sql
INSERT INTO LECTURER
VALUES
(
    3000,
    'Mr',
    'Daniel',
    'Wright',
    '22 Crystal Cres',
    'Alphington',
    'Melbourne',
    '3790',
    'Australia',
    '5',
    '1000654321',
    'CommBank',
    89000.00,
    2.0,
    'DB'
);
```

### 4d. Insert Partial Information

When inserting only some columns:

- The column names must be specified.
- Every `NOT NULL` column must receive a value.

```sql
INSERT INTO LECTURER
(
    StaffNO,
    Title,
    FName,
    LName,
    StreetAddress,
    Suburb,
    PostCode,
    Country,
    ResearchArea,
    WorkLoad
)
VALUES
(
    4000,
    'Mr',
    'RaiHong',
    'Lam',
    '12 Oracle Dr',
    'Fitzroy',
    '3424',
    'Australia',
    'Data Mining',
    1
);
```

---

## 5. Display the `LECTURER` Table

```sql
SELECT *
FROM LECTURER;
```

Write down your observations.

---

## 6. Create and Populate the `STUDENT` Table

### 6a. Create the Table

The column `CiTTy` is deliberately written using mixed case in the statement.

```sql
CREATE TABLE STUDENT
(
    StudentNO   NUMBER(6) NOT NULL,
    DOB         DATE,
    FName       VARCHAR2(30),
    LName       VARCHAR2(30),
    -- City is written as CiTTy
    CiTTy       VARCHAR2(40),
    PostCode    VARCHAR2(4),
    Country     VARCHAR2(30),
    FeePaid     NUMBER(8,2),
    LastFeeDate DATE,
    PRIMARY KEY (StudentNO)
);
```

### 6b. Insert Five Students

Insert records with these student numbers:

- `30001`
- `30002`
- `30003`
- `30004`
- `30005`

Assign values to every column.

#### Inserting a Date

Example date literal:

```sql
'12-FEB-2002'
```

#### Inserting Date and Time

```sql
TO_DATE('12-MAR-2001 16:15', 'DD-MON-YYYY HH24:MI')
```

#### Displaying Date and Time

```sql
TO_CHAR(NameOfAttribute, 'DD-MON-YYYY HH24:MI')
```

Example:

```sql
SELECT TO_CHAR(SYSDATE, 'DD-MON-YYYY HH24:MI')
FROM DUAL;
```

---

## 7. Add Columns to `STUDENT`

```sql
ALTER TABLE STUDENT
ADD
(
    StreetAddress VARCHAR2(70),
    Suburb         VARCHAR2(40)
);
```

---

## 8. Inspect the `STUDENT` Table Structure

In Oracle SQL Developer or Visual Studio Code:

```sql
DESCRIBE STUDENT;
```

Or:

```sql
DESC STUDENT;
```

DBeaver does not support the `DESC` command in the same way. Use:

```sql
SELECT COLUMN_NAME, DATA_TYPE
FROM USER_TAB_COLUMNS
WHERE TABLE_NAME = 'STUDENT';
```

Write down your observations.

---

## 9. Drop the `CiTTy` Column

```sql
ALTER TABLE STUDENT
DROP (CiTTy);
```

---

## 10. Add `City` as a `CHAR` Column

```sql
ALTER TABLE STUDENT
ADD (City CHAR(40));
```

---

## 11. Change `City` to `VARCHAR2`

```sql
ALTER TABLE STUDENT
MODIFY (City VARCHAR2(40));
```

Explain the difference between `CHAR` and `VARCHAR2`.

---

## 12. Update a Student Record

```sql
UPDATE STUDENT
SET StreetAddress = '12 New St'
WHERE StudentNO = 30001;
```

Display the contents of the `STUDENT` table and write down your observations.

---

## 13. Combine `ADD` and `DROP`

Can you add a new field and drop another field in one SQL statement?

Explain your answer.

---

## 14. Commit the Transaction

```sql
COMMIT;
```

Explain what happens.

---

# Part B: Querying Exercises

## 15. Import the Provided Tables

The required tables exist in the `dtaniar` account and contain sample records.

Example:

```sql
CREATE TABLE SUBJECT
AS
SELECT *
FROM dtaniar.SUBJECT;
```

Import all required tables into your account.

The original lab document includes an E/R diagram on page 5 showing the relationships among the following tables:

- `LAB`
- `LAB_SIGNUP`
- `LECTURE`
- `LECTURER`
- `STUDENT`
- `STUDENT_ENROLMENT`
- `SUBJECT`
- `TUTOR`

---

## 16. Lecturer Schedules

Write an SQL statement that lists all lecturers and their lecture schedules.

---

## 17. Lecturers Who Are Not Teaching

Determine whether any lecturers are not teaching.

---

## 18. First-Semester Subjects

List all subjects offered in the first semester.

---

## 19. Students Born Between 1990 and 1995

List the following details for students born after 1990 and before 1995:

- First name
- Last name
- Date of birth
- Fee-paid details

---

## 20. Students Enrolled in Database Subjects

List all students enrolled in a database subject.

Database subject codes:

- `CSE21DB`
- `CSE31DB`
- `CSE41FDB`

---

## 21. Students Who Are Tutors

List all students who are tutors.

---

## 22. Network Management Lecturers

Select lecturers whose research area is:

```text
Network Management
```

---

## 23. Average Lecturer Salary

Calculate the average salary of the lecturers.

---

## 24. Minimum and Maximum Lecturer Salary

Calculate the minimum and maximum lecturer salaries.

---

## 25. Tutors by Subject and Semester

List the number of tutors for each subject and semester.

---

## 26. Students in Each Lab

For each subject and lab, list:

- The total number of students
- The tutor's name

---

## 27. Weekly Database Lab Cost

Calculate the cost of running all database labs per week.

Use:

```text
Lab duration × tutor salary per hour
```

---

**End of Lab**

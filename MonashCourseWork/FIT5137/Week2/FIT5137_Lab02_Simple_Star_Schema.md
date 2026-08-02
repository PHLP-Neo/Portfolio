# FIT5137 Advanced Database Technology

## Lab 2: Star Schemas

## Part I: The International College Case Study

### Description

The admission office handles enrolment, payment, and marketing campaigns for international students, often through educational agents located overseas. Its operational system maintains the details of international students enrolled in the college and their payments.

The system has the following features:

- Each student's details and enrolled courses are stored.
- The college is multi-campus, and some courses are offered at different campuses. The admission office handles international students across all campuses.
- Some students are handled by an educational agent, particularly for their first course. For later courses, students normally deal directly with the college.
- Students pay tuition fees several times, normally once per semester, for each course.

> **E/R diagram description:** `STUDENT` connects to `ENROLMENT` and `PAYMENT`. `ENROLMENT` also connects to `AGENT` and `COURSE`; `COURSE` connects to `CAMPUS`. `PAYMENT` references both the student and enrolment. All displayed relationships are non-associative because the related entities do not share a primary key.

### Operational database tables

- `Student` (**StudentID**, LastName, FirstName, Address, Phone, DOB, Country, VisaExpDate, Sponsor)
- `Campus` (**CampusID**, CampusName, CampusAddress)
- `Course` (**CourseCode**, CourseName, Duration, CourseLevel, *CampusID*)
- `Agent` (**AgentNo**, AgentName, AgentAddress, AgentPhone, ContactPerson)
- `Enrolment` (**EnrolmentNo**, EnrolmentYear, EnrolmentStatus, *StudentID*, *AgentNo*, *CourseCode*)
- `Payment` (**PaymentNo**, PaymentDate, Amount, *StudentID*, *EnrolmentNo*)

Operational tables can be queried with:

```sql
select * from opdb.<table_name>;
```

### Analysis requirements

The data warehouse must answer at least these questions:

- What is the total income coming from particular countries?
- What is the total income for particular postgraduate courses in a particular year?
- What is the total income attributable to each agent?
- How many payments are generated each year?

> **Important:** The star schema design, fact measures, and dimensions must follow the specific analytical questions in each lab exercise and assignment. The design should align precisely with the data and analysis required by the problem.

### Star schema

> **Diagram description:** `CollegeFact` is linked to `CountryDim`, `CourseDim`, `AgentDim`, and `YearDim`. Its dimension keys are `Country`, `AgentNo`, `CourseCode`, and `EnrolmentYear`; its measures are `Number_of_Payments` and `Total_Income`.

### SQL implementation

```sql
/*
drop table AgentDim;
drop table CountryDim;
drop table CourseDim;
drop table YearDim;
drop table CollegeFact;
*/

-- Agent Dimension
create table AgentDim as
select * from opdb.Agent;

select * from AgentDim;

-- Country Dimension
create table CountryDim as
select distinct Country
from opdb.Student;

select * from CountryDim;

-- Course Dimension
create table CourseDim as
select CourseCode, CourseName, Duration, CourseLevel
from opdb.Course;

select * from CourseDim;

-- Year Dimension
create table YearDim as
select distinct EnrolmentYear
from opdb.Enrolment;

select * from YearDim;

-- Fact Table
create table CollegeFact as
select
    S.Country,
    E.AgentNo,
    E.CourseCode,
    E.EnrolmentYear,
    count(P.PaymentNo) as Number_of_Payments,
    sum(P.Amount) as Total_Income
from opdb.Student S, opdb.Enrolment E, opdb.Payment P
where E.EnrolmentNo = P.EnrolmentNo
  and E.StudentID = S.StudentID
group by
    S.Country,
    E.AgentNo,
    E.CourseCode,
    E.EnrolmentYear;

select * from CollegeFact;
```

### Tasks

Using the star schema, write SQL statements for these reports:

1. What is the total income coming from Australia?
2. What is the total income for each course?
3. What is the total income for the Master of Data Science course (`C6003`) in 2019?
4. What is the total income from New Star Agent?

## Part II: The Sales Case Study - Quarter

### Description

The sales operational system has four entities: product, sales, branch, and category.

- Product-Sales is one-to-many.
- Sales-Branch is many-to-one.
- Product-Branch can be viewed as many-to-many, but because Sales has its own primary key (`SalesNo`), the relationships from Sales to Branch and Product are non-associative.
- Product-Category is many-to-one.

> **E/R diagram description:** `SALES` references one `PRODUCT` and one `BRANCH`; `PRODUCT` references one `CATEGORY`. A branch and product can participate in many sales.

Operational tables can be queried with:

```sql
select * from opdb.<table_name>;
```

The manager wants to analyse total sales by quarter, branch, and product category.

### Star schema

> **Diagram description:** `SalesFact` is linked to `TimeDim`, `BranchDim`, and `ProdCategoryDim`. The fact contains `Quarter`, `BranchID`, `CategoryID`, and `Total_Sales`.

### SQL implementation

```sql
/*
drop table ProdCategoryDim;
drop table BranchDim;
drop table TimeDim;
drop table TempFact;
drop table SalesFact;
*/

-- Product Category Dimension
create table ProdCategoryDim as
select * from opdb.Category;

select * from ProdCategoryDim;

-- Branch Dimension
create table BranchDim as
select * from opdb.Branch;

select * from BranchDim;

-- Time Dimension
create table TimeDim (
    Quarter number(1),
    Description varchar2(20)
);

insert into TimeDim values (1, 'Jan-Mar');
insert into TimeDim values (2, 'Apr-Jun');
insert into TimeDim values (3, 'Jul-Sep');
insert into TimeDim values (4, 'Oct-Dec');

select * from TimeDim;

-- Temporary Fact Table
create table TempFact as
select
    S.SalesDate,
    B.BranchID,
    C.CategoryID,
    S.TotalPrice
from opdb.Branch B, opdb.Sales S, opdb.Product P, opdb.Category C
where B.BranchID = S.BranchID
  and S.ProductNo = P.ProductNo
  and P.CategoryID = C.CategoryID;

alter table TempFact
add (Quarter number(1));

update TempFact
set Quarter = 1
where to_char(SalesDate, 'MM') >= '01'
  and to_char(SalesDate, 'MM') <= '03';

update TempFact
set Quarter = 2
where to_char(SalesDate, 'MM') >= '04'
  and to_char(SalesDate, 'MM') <= '06';

update TempFact
set Quarter = 3
where to_char(SalesDate, 'MM') >= '07'
  and to_char(SalesDate, 'MM') <= '09';

update TempFact
set Quarter = 4
where Quarter is null;

select * from TempFact;

-- Sales Fact Table
create table SalesFact as
select
    Quarter,
    BranchID,
    CategoryID,
    sum(TotalPrice) as Total_Sales
from TempFact
group by Quarter, BranchID, CategoryID;

select * from SalesFact;
```

### Tasks

Using the star schema, write SQL statements for these reports:

1. Show the total sales in different quarters.
2. Show the total sales for different branches and product categories.
3. Show the total sales of kitchen supplies in Quarter 1.

## Part III: The Sales Case Study - Month

### Description

This part uses the same operational sales model as Part II. The manager now wants to analyse total sales by month, branch, and product category.

> **E/R diagram description:** `SALES` references `PRODUCT` and `BRANCH`, while `PRODUCT` references `CATEGORY`. The intended warehouse changes the time grain from quarter to month.

### Tasks

1. Create a star schema for the sales data.
2. Define the dimensions and attributes for the sales star schema.
3. Write the SQL statements that implement the star schema.
4. Write SQL statements for these reports:
   1. Show total sales by month.
   2. Show total sales by branch and product category.

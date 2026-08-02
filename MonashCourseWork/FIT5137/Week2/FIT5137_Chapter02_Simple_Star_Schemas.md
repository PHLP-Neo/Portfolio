# Chapter 2: Simple Star Schemas

## Overview

1. Notations and processes
2. First case study: a college star schema
3. Another simple case study: a sales star schema
4. Two-column table methodology

## 1. Notations and Process

### 1.1 Star Schema Notation

- A data warehouse provides a multidimensional view of a database.
- A star schema represents this multidimensional view.
- A star schema consists of a central **fact** and surrounding **dimensions**.
- Connecting lines may be straight or bent without changing their meaning.
- Fact and dimension tables contain attributes.
- Each dimension has a dimension ID as its primary key.
- Dimension IDs in the fact table are both foreign keys and part of the fact table's key.
- Fact measures are numerical values.

> **Diagram description:** A central fact table connects outward to multiple dimension tables. In the sales example, `SalesFACT` contains dimension identifiers and `Total_Sales`; it is linked to time, product, location, and customer dimensions. When a dimension is under discussion, that table is highlighted.

### 1.2 E/R Diagram Notation

- Entity names are capitalised.
- Primary key: **PK**.
- Foreign key: **FK**.
- Relationships use crow's-foot notation with participation.
- An associative relationship is many-to-many; a non-associative relationship is one-to-many.

> **Diagram description:** The example operational model contains `BRANCH`, `PRODUCT`, `CATEGORY`, and `SALES`. Crow's-foot symbols show the relationship cardinalities and optional or mandatory participation.

### 1.3 Transformation Process

The operational database is represented by an E/R model and supports day-to-day processing. Through an ETL transformation, selected and aggregated operational data becomes a data warehouse represented by a star schema.

> **Diagram description:** An arrow labelled *Transformation (ETL)* points from an operational E/R diagram to a star schema with one fact table surrounded by dimensions.

## 2. First Case Study: A College Star Schema

### Operational system and analytical purpose

The college's E/R database supports operational procedures. The college is multi-campus, some courses are offered at different campuses, and the admission office handles international students across all campuses.

The data warehouse is intended to answer questions such as:

- What is the total income from particular countries?
- What is the total income for particular postgraduate courses in a particular year?
- What is the total income attributable to each agent?
- How many payments are generated each year?

### Facts and dimensions

Fact measures derived from the questions:

- `Number_of_Payments`
- `Total_Income`

Dimensions derived from the questions:

- Country
- Course
- Agent
- Enrolment year

> **Diagram description:** The operational model contains student, enrolment, payment, agent, course, and campus entities. It is transformed into `CollegeFACT`, linked to `CountryDIM`, `CourseDIM`, `AgentDIM`, and `YearDIM`. The fact table stores the four dimension identifiers plus `Number_of_Payments` and `Total_Income`.

### Create the dimension tables

```sql
create table AgentDim as
select * from Agent;

create table CountryDim as
select distinct Country
from Student;

create table CourseDim as
select CourseCode, CourseName, Duration, CourseLevel
from Course;

create table YearDim as
select distinct EnrolmentYear
from Enrolment;
```

### Create the fact table

The fact is aggregated from operational tables because the dimension tables do not contain the payment-level data needed to calculate the measures.

```sql
create table CollegeFact as
select
    S.Country,
    E.AgentNo,
    E.CourseCode,
    E.EnrolmentYear,
    count(P.PaymentNo) as Number_of_Payments,
    sum(P.Amount) as Total_Income
from Student S, Enrolment E, Payment P
where E.EnrolmentNo = P.EnrolmentNo
  and E.StudentID = S.StudentID
group by
    S.Country,
    E.AgentNo,
    E.CourseCode,
    E.EnrolmentYear;
```

### Question time

**Why is the fact table created from operational tables rather than dimension tables?**

The fact measures must be calculated from detailed operational transactions. Dimensions provide descriptive viewpoints and identifiers, but usually do not contain the transaction rows required for aggregation.

## 3. Another Simple Case Study: A Sales Star Schema

The goal is to analyse total sales by:

- Quarter
- Branch
- Product category

> **Diagram description:** The operational model includes `SALES`, `PRODUCT`, `CATEGORY`, and `BRANCH`. It is transformed into `SalesFACT`, which stores `Quarter`, `BranchID`, `CategoryID`, and `Total_Sales`, and connects to `TimeDIM`, `BranchDIM`, and `ProdCategoryDIM`.

### Create the dimension tables

```sql
create table ProdCategoryDim as
select * from Category;

create table BranchDim as
select * from Branch;

create table TimeDim (
    Quarter number(1),
    Description varchar2(20)
);

insert into TimeDim values (1, 'Jan-Mar');
insert into TimeDim values (2, 'Apr-Jun');
insert into TimeDim values (3, 'Jul-Sep');
insert into TimeDim values (4, 'Oct-Dec');
```

### Identify the quarter through a temporary fact table

Quarter is not directly available in the operational tables, so it is derived in `TempFact`.

```sql
create table TempFact as
select
    S.SalesDate,
    B.BranchID,
    C.CategoryID,
    S.TotalPrice
from Branch B, Sales S, Product P, Category C
where B.BranchID = S.BranchID
  and S.ProductNo = P.ProductNo
  and P.CategoryID = C.CategoryID
  and to_char(S.SalesDate, 'YYYY') = '2020';

alter table TempFact
add (Quarter number(1));

update TempFact
set Quarter = 1
where to_char(SalesDate, 'MM') >= '01'
  and to_char(SalesDate, 'MM') <= '03';
```

The remaining months are assigned to quarters 2, 3, and 4 using the same pattern.

### Create the sales fact

```sql
create table SalesFact as
select
    Quarter,
    BranchID,
    CategoryID,
    sum(TotalPrice) as Total_Sales
from TempFact
group by Quarter, BranchID, CategoryID;
```

### Case study summary

There are three ways to create a dimension table:

1. Copy an operational table directly with `create table ... as select *`.
2. Select only relevant attributes from an operational table.
3. Create the dimension manually and populate it with `insert into`.

## 4. Two-Column Table Methodology

The two-column table method checks whether a proposed star schema is valid. It imagines the fact measure as viewed from one dimension at a time:

- The first column represents a category or dimension.
- The second column represents the fact measure or measures.

### 4.1 One Fact Measure

The first column contains a category and the second contains one statistical numerical value. If the same fact `F` makes sense when viewed from every proposed category `A`, `B`, `C`, and `D`, the schema can contain those four dimensions around fact `F`.

> **Diagram description:** Four two-column tables (`A-F`, `B-F`, `C-F`, and `D-F`) map to a star schema in which dimensions A-D surround a single fact measure F.

#### Example

An immigration fact can be viewed by year, country, visa type, and settling state.

> **Diagram description:** `ImmigrationFACT` contains `Year`, `Country`, `VisaType`, `SettlingState`, and `Num_of_Immigrants`. It connects to `YearDIM`, `CountryDIM`, `VisaTypeDIM`, and `SettlingStateDIM`.

### 4.2 Multiple Fact Measures

The second column may contain multiple facts, `F = {F1, F2, F3, ...}`. Every proposed fact measure must be meaningful for every proposed dimension.

> **Diagram description:** Four category tables each contain `F1`, `F2`, and `F3`, producing a star schema with dimensions A-D around a fact table containing all three measures.

#### Example

> **Diagram description:** `FitnessCentreFACT` contains job title, month, employment type, gender, `Num_of_Employees`, and `Total_Salary`. It connects to job-title, month, employment-type, and gender dimensions.

If a dimension such as `B` supports only `F1` and `F2`, a single star schema containing `F1`, `F2`, and `F3` across all four dimensions is not valid at that grain.

### Question time: why not store average salary?

An average is not additive and an average of averages can be incorrect. Store additive components such as total salary and employee count, then calculate the average when querying. Chapter 3 develops this issue further.

## Summary

- A fact is a numerical, aggregated value.
- A dimension is a point of view for analysis.
- Dimension tables may be copied directly, created from selected attributes, or created manually.
- Fact tables may be created directly from operational data or through a temporary fact table.
- The two-column method can validate whether facts and dimensions belong in the same star schema.

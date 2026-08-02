# Chapter 3: Creating Facts and Dimensions

## More Complex Processes

## Overview

1. Use of the `count` function
2. Average in the fact
3. Outer join
4. Creating temporary dimension tables
5. Creating temporary tables in the operational database

## 1. Use of the `count` Function

```sql
count(*)
```

Counts records.

```sql
count(attribute)
```

Counts non-null values of the attribute.

```sql
count(distinct attribute)
```

Counts distinct non-null values, removing duplication.

### Example: Mobile Apps Repository

The Monalisa App Store allows students from universities around the world to publish applications and receive feedback. A star schema is required to analyse ratings and feedback by different authors and applications.

> **Diagram description:** The operational model contains application, category, download, review, app-user, and university entities. The star schema places an application-download fact at the centre, connected to category, university, location, and time dimensions.

### Create the dimensions

```sql
create table CategoryDim as
select * from Category;

create table UniversityDim as
select UniversityID, UniversityName
from University;

create table LocationDim as
select distinct
    Country || City as LocationID,
    City,
    Country
from University;

create table TimeDim as
select distinct
    to_char(DownloadDate, 'YYYYMM') as TimeID,
    to_char(DownloadDate, 'MM') as Month,
    to_char(DownloadDate, 'YYYY') as Year
from Download;
```

### Create a temporary fact

```sql
create table TempFact as
select
    to_char(D.DownloadDate, 'YYYYMM') as DownloadMonth,
    to_char(A.CreationDate, 'YYYYMM') as CreationMonth,
    U.Country || U.City as LocationID,
    A.CategoryID,
    A.ApplicationID,
    U.UniversityID
from University U, App_User R, Download D, Application A
where U.UniversityID = R.UniversityID
  and R.UserID = D.DownloaderID
  and D.ApplicationID = A.ApplicationID;
```

### Fact measure: total downloads

```sql
create table AppsDownloadFact as
select
    DownloadMonth as TimeID,
    LocationID,
    CategoryID,
    UniversityID,
    count(*) as TotalDownloads
from TempFact
group by
    DownloadMonth,
    LocationID,
    CategoryID,
    UniversityID;
```

### Alternative fact measure: total applications

```sql
create table AppsFact as
select
    CreationMonth as TimeID,
    LocationID,
    CategoryID,
    UniversityID,
    count(distinct ApplicationID) as TotalApps
from TempFact
group by
    CreationMonth,
    LocationID,
    CategoryID,
    UniversityID;
```

## 2. Average in the Fact

Many aggregate functions can be used in a fact table, but highly aggregated measures create pitfalls. In particular, storing an average as a fact measure can produce an incorrect *average of averages*.

### Average-of-an-average example

The initial schema stores `Average_Score` by subject and semester. For the Database unit:

- Average calculated from fact rows: `(73.833 + 48) / 2 = 60.9165`
- Correct average calculated from the operational rows: `539 / 8 = 67.375`

The first result is wrong because the two semester averages represent different numbers of students.

> **Diagram description:** `EnrolmentFACT` initially stores `Average_Score` and connects to `SubjectDIM` and `SemesterDIM`. The corrected fact replaces the average with `Total_Score` and `Number_of_Students` at the same subject-semester grain.

### Corrected calculation

```sql
select
    sum(Total_Score) / sum(Number_of_Students) as Average_Score
from EnrolmentFact2
where UnitCode = 'IT001';
```

### Minimum and maximum

- Minimum and maximum can be stored in a fact table because they retain a meaningful global minimum or maximum.
- Do not mix a minimum measure with `max()` or a maximum measure with `min()`; the result is not meaningful.
- `count` and `sum` are commonly used fact measures.

```sql
select max(Max_Score)
from EnrolmentFact3
where UnitCode = 'IT001';

select min(Min_Score)
from EnrolmentFact3
where UnitCode = 'IT001';
```

## 3. Outer Join

### Example: Employment Agency

An employment agency places temporary workers in companies during peak periods. The required star schema analyses:

Fact measures:

- Total openings
- Total placements

Dimensions:

- Duration
- Qualification
- Month

> **Diagram description:** The operational model contains company, opening, qualification, placement, candidate, and candidate-qualification entities. It is transformed into `PlacementFACT`, connected to qualification, duration, and month dimensions. The fact stores `TotalOpening` and `TotalPlacement`.

### Create dimension tables

```sql
create table QualificationDim as
select * from Qualification;

create table MonthDim as
select distinct
    to_char(ActualStartDate, 'Month') as MonthName
from Placement;

create table DurationDim (
    DurationID number,
    DurationDesc varchar2(20)
);

insert into DurationDim values (1, 'Short-Term');
insert into DurationDim values (2, 'Medium-Term');
insert into DurationDim values (3, 'Long-Term');
```

### Create `TempFact` with a left outer join

The left outer join retains openings even when no placement exists, allowing `TotalOpening` and `TotalPlacement` to be counted separately.

```sql
create table TempFact as
select
    O.QCode,
    O.StartDate,
    O.EndDate,
    to_char(P.ActualStartDate, 'Month') as MonthName,
    O.OpenNo,
    P.CandNo
from Opening O left outer join Placement P
    on O.OpenNo = P.OpenNo;

alter table TempFact
add (DurationID number);

update TempFact
set DurationID = 1
where EndDate - StartDate < 10;

update TempFact
set DurationID = 2
where EndDate - StartDate >= 10
  and EndDate - StartDate <= 30;

update TempFact
set DurationID = 3
where EndDate - StartDate > 30;
```

### Create the fact

```sql
create table AgencyFact as
select
    QCode,
    DurationID,
    MonthName,
    count(OpenNo) as TotalOpening,
    count(CandNo) as TotalPlacement
from TempFact
group by QCode, DurationID, MonthName;
```

## 4. Creating Temporary Dimension Tables

### Sales example

The required time dimension contains `QuarterID`, `Quarter`, and `Year`. It cannot be copied directly because the operational sales table contains a date rather than those attributes. Creating rows manually is inefficient because the number of years is unknown, so a temporary time dimension is used.

> **Diagram description:** Operational sales data is transformed into `SalesFACT`, connected to `TimeDIM`, `BranchDIM`, and `ProdCategoryDIM`. `QuarterID` combines the year and quarter number in `YYYYQ` form.

### Create direct dimensions

```sql
create table BranchDim as
select * from Branch;

create table ProdCategoryDim as
select * from Category;
```

### Create a temporary time dimension

```sql
create table TimeDimTemp as
select distinct
    to_char(SalesDate, 'MM') as Month,
    to_char(SalesDate, 'YYYY') as Year
from Sales;

alter table TimeDimTemp add (
    QuarterID char(5),
    Quarter char(1)
);

update TimeDimTemp
set Quarter = '1'
where Month >= '01' and Month <= '03';

update TimeDimTemp
set Quarter = '2'
where Month >= '04' and Month <= '06';

update TimeDimTemp
set Quarter = '3'
where Month >= '07' and Month <= '09';

update TimeDimTemp
set Quarter = '4'
where Month >= '10' and Month <= '12';

update TimeDimTemp
set QuarterID = Year || Quarter;

create table TimeDim as
select distinct QuarterID, Quarter, Year
from TimeDimTemp;
```

### Create the sales fact

```sql
create table TempFact as
select
    to_char(S.SalesDate, 'YYYY') as Year,
    to_char(S.SalesDate, 'MM') as Month,
    B.BranchID,
    P.CategoryID,
    S.TotalPrice
from Branch B, Sales S, Product P
where B.BranchID = S.BranchID
  and S.ProductNo = P.ProductNo;

alter table TempFact add (Quarter char(1));

update TempFact
set Quarter = '1'
where Month >= '01' and Month <= '03';

update TempFact
set Quarter = '2'
where Month >= '04' and Month <= '06';

update TempFact
set Quarter = '3'
where Month >= '07' and Month <= '09';

update TempFact
set Quarter = '4'
where Quarter is null;

alter table TempFact add (QuarterID char(5));

update TempFact
set QuarterID = Year || Quarter;

create table SalesFact as
select
    QuarterID,
    BranchID,
    CategoryID,
    sum(TotalPrice) as Total_Sales
from TempFact
group by QuarterID, BranchID, CategoryID;
```

## 5. Creating Temporary Tables in the Operational Database

Operational data may require preprocessing before it can create fact and dimension tables. The sessional-employment case study demonstrates this: a university hires students for tutoring, programming, administration, and other temporary jobs.

Required analysis:

- Fact: number of contracts
- Dimensions: department, year, country, and degree

Each employee may have multiple degrees, but the data warehouse needs only the latest degree.

> **Diagram description:** The operational model connects contracts to employees and departments, while employees connect to degrees through `EMP_DEGREE`. The resulting `ContractFACT` connects to department, year, country, and degree dimensions and stores `Num_of_Contracts`.

### Create direct dimensions

```sql
create table DepartmentDim as
select * from Department;

create table DegreeDim as
select * from Degree;

create table YearDim as
select distinct to_char(StartDate, 'YYYY') as Year
from Contract;
```

### Keep each employee's latest degree

```sql
create table EmployeeTemp as
select
    T.EmpNo,
    T.EmpName,
    T.DOB,
    T.Phone,
    T.TaxFileNumber,
    T.DegreeID
from (
    select
        E.EmpNo,
        E.EmpName,
        E.DOB,
        E.Phone,
        E.TaxFileNumber,
        D.DegreeID,
        rank() over (
            partition by E.EmpNo
            order by D.GraduationDate desc
        ) as Rank
    from Employee E, Emp_Degree D
    where E.EmpNo = D.EmpNo
) T
where T.Rank = 1;
```

### Create the contract fact

```sql
create table ContractFact as
select
    E.DegreeID,
    to_char(C.StartDate, 'YYYY') as Year,
    C.DeptNo,
    count(*) as Num_of_Contracts
from EmployeeTemp E, Contract C
where E.EmpNo = C.EmpNo
group by
    E.DegreeID,
    to_char(C.StartDate, 'YYYY'),
    C.DeptNo;
```

## Summary

- Creating fact tables may require aggregate functions and outer joins.
- Creating dimensions may require temporary dimension tables.
- Operational data may need preprocessing in temporary operational tables before warehouse loading.

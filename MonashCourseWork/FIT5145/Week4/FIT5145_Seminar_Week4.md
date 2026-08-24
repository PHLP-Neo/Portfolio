# FIT5145 — Foundations of Data Science

## Seminar Week 4: Data Sources and Standards

**Monash University**

- **Clayton cohort:** Dr. Guanliang Chen and Dr. Chris Yun
- **Malaysia cohort:** Dr. Chern Hong Lim

> These notes are a Markdown conversion of the Week 4 seminar slides. Repeated navigation slides and decorative elements have been simplified, while the instructional text, examples, activities, and key data tables have been retained.

---

## Pre-Surveys

Please notice that …
- Please spend a few minutes filling out the following two
ANONYMOUS pre-surveys to help us improve:
- Unit & Lecture survey
- Applied classes survey

_Source slide: 2_

---

## Clarification About Assignments 1 & 3

Clarification about Assignment 1 & 3
- It should be about HAVING FUN!
- How to measure “novelty”?

_Source slide: 3_

---

## Unit Schedule

| Week | Content | Lecturer (Clayton) |
|---:|---|---|
| 1 | Overview of data science | Chris Yun |
| 2 | History and impact of data science | Chris Yun |
| 3 | Data business models | Chris Yun |
| **4** | **Data sources and standards** | **Chris Yun** |
| 5 | Characterising data and "big" data | Chris Yun |
| 6 | Big Data and data science | Chris Yun |
| 7 | Supervised data analysis (1) | Chris Yun |
| 8 | Supervised data analysis (2) | Chris Yun |
| 9 | Unsupervised data analysis | Chris Yun |
| 10 | Data management | Chris Yun |
| 11 | Issues in data science | Chris Yun |
| 12 | Future of data science | Guest Lecturer |

_Source slide: 4_

---

## Learning Outcomes — Week 4

Learning Outcomes (Week 4)
By the end of this week, you should be able to:
- Identify where to find data and explain how to access it
- Explain why data needs to be standardised
- Apply data sourcing and standards concepts to real-
world datasets
- Use shell commands to read and manipulate large data
files

_Source slide: 5_

---

## Topics for Lecture 4

1. Data sourcing
a. Open data
b. What, where & how to get data
2. Data standards (making data usable)
3. Sourcing + standards in action
4. Shell commands

_Source slide: 6_

---

## Standard Data Science Value Chain

- Collection: getting the data
- Wrangling: data preprocessing, cleaning
- Analysis: discovery (learning, visualisation, etc.)
- Presentation: arguing that results are significant and useful
- Engineering: storage and computational resources
- Governance: overall management of data
- Operationalisation: putting the results to work
Our Standard Value Chain

_Source slide: 7_

---

## Data Sources — Open Data

- Data sourcing
- Open data
- Examples: What, where & how
to get data
- Data standards
- Sourcing + standards in action
- Shell commands

_Source slide: 8_

---

## Data Sourcing

- Where can we get data from?
- Is it relevant to my project?
- Can we trust it?
- Can we use it legally?
- Without data sources, there is no data science.
Data sourcing

_Source slide: 9_

---

## Open Data

- Data that is “freely available to everyone to use and
republish as they wish, without restrictions from
copyright, patents or other mechanisms of control” –
Wikipedia
- Free – accessible, costs nothing
- Free – unrestricted usage
- Free – simple, non-proprietary format
- Commonly associated with open government data
Open data

_Source slide: 10_

---

## Open Data Examples

Open data examples
Transport & maps
Roads, routes & geographic data -
open and community-built
openstreetmap.org
Financial & market data
Stock prices, indices & company
filings
finance.yahoo.com
Open government data
Census, crime stats & economic
indicators
data.gov.au
Data sharing platform
Download & build on datasets
shared by others
<https://www.kaggle.com/work/>
datasets

_Source slide: 11_

---

## Benefits of Open Data

- New opportunities for business, new products and
services, and can raise productivity (e.g.: real-time
traffic data)
- Open data supports public understanding and citizen
engagement (e.g.: Covid-19 dashboard)
- Government, industry, universities and other
organisations should work together to share and use
data responsibly (e.g.: bushfire, education)
Open Data Benefits
Source: “Open data” by MGI, and “Science as an open enterprise” by the Royal Society (UK)

_Source slide: 12_

---

## Open Data and Disaster Response

## Open Data Benefits

Disaster Response (e.g. bushfire)
Government + Weather agency + Emergency services + Private companies
→ Shared data → Faster response

What open data lets us do
- Identify high-risk areas
- Decide safe evacuation routes
- Prioritise support and firefighting resources

*Result: better situational awareness, efficient resources, saved lives.*


_Source slide: 13_

---

## Open Data and Education

2Education: IT students in Victoria are better than
those in NSW.
Open
education data
Socioeconomic
data
Identify
disadvantaged
schools
Targeted
funding &
support
+ → →
What open data lets us do
Reveal learning gaps across regions
Identify schools or communities needing
extra help
Support better policy and resource allocation
Result: evidence-based decisions, reduced regional gaps, stronger outcomes for all.
Open Data Benefits

_Source slide: 14_

---

## Global Impact of Open Data

See “the global impact of open data” for a large catalogue of examples
Open Data Benefits

_Source slide: 15_

---

## The Year Open Data Went Worldwide

The video “The year open data went worldwide” a
TED talk by Prof. Tim Berners-Lee
Case 1: Bicycle Accident Data
Case 2: Water Supply and Racial Patterns
Case 3: Major earthquake hit Haiti

_Source slide: 16_

---

## Class Activity — Current Location

<https://miro.com/welcomeonboard/ZEZtdCtQN2xMU2hlV3h>
RK284M1ZvdkpVQ21YcWVOWVVuY3pYakVITFEyaGNGN2tUU
GRlbG9FaE5BbDU5aGdzK0FGVTRmck5LcGt2Mm42VDIyVzJE
RjNBcldSSEJuS1pKanUwcDVQUUFPR1ZQd0Q0REhPeTkyZ0Nz
cWtRNnJtRFRhWWluRVAxeXRuUUgwWDl3Mk1qRGVRPT0hdj
E=?share_link_id=686910333092
- Mark your current location on Clayton campus map
- How is your internet quality?
- Where are you joining from today?
- Are you hungry?
Activity: Where are you right now?

_Source slide: 17_

---

## Democratisation of Data

- Information that once was available to only a select
few ... available to everyone
- Finally puts crucial business information in the hands
of those who need it
- Open data needs supporting infrastructure to allow
sharing, e.g. USA Open Gov Initiative
- Analytic tools, (desktop and web-based), available to
analyse it.
Democratization of Data
Source: “the New Data Republic: Not Quite a Democracy” in MIT Sloan Review 2015

_Source slide: 18_

---

## Difficulties of Using Open Data

- Different data formats (e.g.: PDF, Excel, CSV, JPG)
- Poor organisation – datasets may contain many tables,
files, or external links.
Source: “What’s Wrong with Open-Data Sites–and How We Can Fix Them”

_Source slide: 19_

---

## More Difficulties of Using Open Data

- Programming skills may be required (e.g.: API, web
scrapping, Excel, PDF)
- Data can be fragmented – information may be spread
across multiple websites, tables, or sources.
- Large volume of data – the huge number of available
datasets can make it difficult to find the right one.
→ Data USA integrates data from multiple sources and presents it
through interactive visualisations and reports.
Difficulties of Using Open Data
Source: “What’s Wrong with Open-Data Sites–and How We Can Fix Them”

_Source slide: 20_

---

## Benefits of Data Sharing and Open Data

- Solve problems more efficiently through collaboration
and shared resources
- New products, services & business opportunities
- Better research & knowledge
- Public understanding & citizen engagement

_Source slide: 21_

---

## Data Sources — What, Where and How

- Data sourcing
- Open data
- Examples: What, Where & How
to Get Data
- Data standards
- Sourcing + standards in action
- Shell commands

_Source slide: 22_

---

## Public Data Examples

We’ll now look at three examples of public data and using
data?
1. Traffic Forecasting
2. NYC data
3. Predictive analytics for banks
Examples: What and Where to Get
Data

_Source slide: 23_

---

## Example 1 — Traffic Forecasting: Problem

Example 1: Traffic Forecasting
If we want to forecast traffic:
when blockages will occur,
when they will clear,
unexpected situations,
alternate routes
image: math.tu-berlin.de
What data do we
need?

_Source slide: 24_

---

## Example 1 — Traffic Forecasting: Required Data

Example 1: Traffic Forecasting
If we want to forecast traffic:
blockages, clearing, surprising
situations, alternate routes
- Critical data:
- Historical traffic data
- GPS data on traffic flow
- Maps
- incidents and events
- weather
image: math.tu-berlin.de
Where can we get the data from?

_Source slide: 25_

---

## Example 1 — Traffic Forecasting: Data Sources

Example 1: Traffic Forecasting
If we want to forecast traffic: blockages, clearing, surprising
situations, alternate routes
- Critical data:
- Historical traffic data (e.g.: Transport Victoria and VicRoads)
- GPS data on traffic flow (e.g.: smartphones, connected vehicles)
- Maps (e.g.: mapping providers)
- Incidents and events (e.g.: police, emergency services)
- Weather (e.g.: weather agencies)
Where can we get the data from?

_Source slide: 26_

---

## Example 1 — Traffic Forecasting: Challenge

Example 1: Traffic Forecasting
If we want to forecast traffic:
blockages, clearing, surprising
situations, alternate routes
- Critical data:
- Historical traffic data
- GPS data on traffic flow
- Maps
- incidents and events
- weather
- Challenge:
- collect different sources of data
image: math.tu-berlin.de

_Source slide: 27_

---

## Traffic Forecasting — Google Maps and Microsoft Clearflow

Today, Google Mapsuses real-time and historical traffic data to:
- Predict traffic and travel times
- Detect congestion and incidents
- Suggest alternative routes
Microsoft Introduced a Tool, Clearflow for Avoiding Traffic Jams(2008)
- Forecast traffic conditions
- Predict blockages and clearing
- Recommend alternate routes
- Historical example
Traffic Forecasting: Google Maps and
Microsoft
Source: Eric Horvitz’s discussion of Clearflowsystem: “Data, Predictions, and Decisions in Support of People and Society” (skip to 7:40-11:06 )

_Source slide: 28_

---

## Example 2 — New York City Open Data

- NYC introduced a program to make the city’s data accessible to
the public.
- New York City Mayor Mike Bloomberg: “In God We Trust, Everyone
else, bring data.”
- NYC shared many types of government-held public data:
Transportation, Buildings & housing, Public safety, Health,
Environment, City services, Business, and Schools and community
services
Example 2: New York City Data
Source: Bloomberg signs NYC 'Open Data Policy' into law
People started doing…

_Source slide: 29_

---

## NYC Example — Real-Time Bus Tracking

Real-time bus tracking, built on the cheap
DATA SOURCE
Bus GPS signals
Vehicles
broadcast their
live location
across the city
HOW
Low-cost live feed
Cheap sensors + an
open data stream -
no costly
infrastructure
RESULT
Real-time app
Riders see exactly
where their bus
is, right now, on
their phone
Takeaway Open location data + cheap tech = a genuinely useful public service.
Example 2: New York City Data

_Source slide: 30_

---

## NYC Example — Predicting Building Fire Risk

Predicting where fires might start in buildings
DATA SOURCE
Violations +
housing data
Building-code
violations joined
with housing records
HOW
Predictive
analytics
Model learns risk
signals: no smoke
alarms, exposed
wires, cracked walls
RESULT
High-risk
buildings
flagged
Inspectors prioritise
the properties most
likely to burn
Takeaway Two open datasets, combined, become a life-saving risk model.
Example 2: New York City Data

_Source slide: 31_

---

## Complexities of Using NYC Open Data

The complexities of using in NYC:
- Map of road speed by day+time: GPS data for NYC cabs gives; data
obtained via FOIL request, then made public by recipient
- Danger spots for cycles: NYPD crash data obtained by daily download
of PDF files followed by (non-trivial) extraction.
- Dirty waterways (e.g: river, harbor): fecal coliform measurements on
waterways from Department of Environmental Protection’s website;
extracted from Excel sheets per site; each in a different format
- Location from NYC Open Data portal need to normalize the addresses
supplied. (e.g.: 123 Main St vs 123 Main Street)
Example 2: New York City Data
Source: “How we found the worst place to park in New York City”

_Source slide: 32_

---

## NYC and Melbourne Open Data Portals

- NYC Open Data portal
- Melbourne has a similar portal: City of Melbourne’s open data
platform
Example 2: New York City Data

_Source slide: 33_

---

## Example 3 — Predictive Analytics for Banks

- Bigger data is “always” better?
(by Foster Provost, Professor at NYU)
- Describes customer prediction problem for banking
products
- His answer is that it’s not always (much) better.
- But that big data can certainly be better if the data is
richer and more fine-grained.
Example 3: Predictive Analytics for Banks
Source: See this video of a seminar on “Predictive Analytics with Fine-grained
Behavior Data” and author of this book

_Source slide: 34_

---

## Fine-Grained vs Coarse Data

It's not how big the data is - it's how fine-grained
The banking example — same customers, two very different kinds of data
Coarse / traditional data
A few attributes per person
Age, income, postcode — a handful
of columns everyone shares. Two
customers look almost the same, so
adding more people soon stops
helping.
One customer's record:
Age Income Postcode
Just 3 wide features
Fine-grained
behavioural data
Thousands of tiny signals per person
Every transaction, every merchant,
every timestamp. Each customer has
a distinctive fingerprint, so more
data keeps sharpening the
prediction.
One customer's record:
Thousands of narrow, mostly-empty
signals (sparse)
Example 3: Predictive Analytics for Banks

_Source slide: 35_

---

## Is Bigger Data Always Better?

Is bigger data always better?
Predicting who will buy a banking product - the answer is “it depends”
1K 10K 100K 1M 10M 100M
Predictive performance →
Amount of data →
Fine-grained behavioural data Coarse / traditional data
Fine-grained data
keeps climbing
Every extra record adds
new signal - the curve
doesn't flatten out.
Coarse data
plateaus fast
After a point, more rows
of the same few
attributes barely help.
Example 3: Predictive Analytics for Banks

_Source slide: 36_

---

## Lessons Learned from the Examples

What lessons have we learnt from these “data” examples?
- Traffic prediction
combine many sources
you might have to generate some of your own
- NYC data
data requires work to clean up
be creative about sources
Lessons Learnt from the examples
- Predictive analytics for banks
fine-grained data really helps, but is harder to use

_Source slide: 37_

---

## How to Get Data

- Download datasets from the web
- Web APIs: Sends a structured request and receives structured
data, usually in JSON format.
- Web scraping: Extracts content from an HTML webpage.
- Databases and cloud data platforms: Connects to structured
data stored in databases, data warehouses, or cloud storage
(e.g.: Google, Amazon, or Microsoft).

_Source slide: 38_

---

## Twitter / X as a Data Source

Twitter is the most famous microblogging platform
- with big corporate use
- contains lots of metadata: information about users, their follower
network, locations, hashtags, emojis+emoticons, …
Twitter (Now X)

_Source slide: 39_

---

## Twitter Developer API — Example Uses

API: Application Programming Interface
Example:
- App providing “What’s trending right now?”
Get top hashtags
Track viral tweets
Monitor breaking news
- Survey app: What do people think about this movie?
Twitter Developer API

_Source slide: 40_

---

## Twitter Developer API

API: Application Programming Interface
See Twitter’s developer platform
- library interfaces for Java, C++, Javascript, Python, Perl, PHP, Ruby,
...
- allows other applications to manage Twitter data for users
- extensive developer policy
- see search API doc
- lots of tutorials
Try to play with this: https://rapidapi.com/hub

_Source slide: 41_

---

## Example Data and Information APIs

Many companies are exposing their data and their website
functionality as APIs for others to make use of:
- Facebook API
- Twitter API
- Google Maps API
- Youtube API
- Amazon Advertising API
- New York Times API
- Chatgpt API
Example Data/Information APIs

_Source slide: 42_

---

## Data Standards

- Data sourcing
- Open data
- Examples: What, Where & How
to Get Data
- Data standards
- Sourcing + standards in action
- Shell commands

_Source slide: 43_

---

## Setting the Standards

- If you standardise things, you can be more efficient
- Efficiency lowers costs
- So how can you standardise data?
- What role do data scientists and data science play in
standarising things related to data?
Setting the standards

_Source slide: 44_

---

## Transactional Data


_Source slide: 45_

---

## Geospatial Data


_Source slide: 46_

---

## Linked Open Data — DBpedia

Linked Open Data: DBpedia

_Source slide: 47_

---

## Linked Open Data — XML

Linked Open Data: XML (eXtensible Markup
Language)

_Source slide: 48_

---

## Twitter Data


_Source slide: 49_

---

## Sample Twitter JSON Data

```json
{
  "data": [
    {
      "id": "1789012345678901234",
      "text": "Learning data science is fun! #AI #Python",
      "author_id": "2244994945",
      "created_at": "2026-03-23T10:15:30.000Z",
      "public_metrics": {
        "retweet_count": 12,
        "reply_count": 3,
        "like_count": 45,
        "quote_count": 2
      }
    }
  ],
  "includes": {
    "users": [
      {
        "id": "2244994945",
        "name": "Chris Yun",
        "username": "chrisyun_ai"
      }
    ]
  }
}
```

_Source slide: 50_

---

## Internet of Things Data


_Source slide: 51_

---

## Data Types and Formats

- Data is about a variety of things
- transactional data
- (geo)spatial data
- linked (open) data
- social media data
- Internet of Things (IoT)
- Data comes in a variety of formats
- Ascii/text format (+ Unicode!)
- Word or Excel or Pdf format
- Comma separated values (CSV)
- JSON format
- HTML or XML format
Data types and formats

_Source slide: 52_

---

## Making Data Usable Across Systems

How we make data usable across
systems?

_Source slide: 53_

---

## Five Types of Data Standards

Agreed rules so different systems understand each other. A standard can pin
down five things:
1 Representation
How data is stored & structured
CSV · JSON · XML · EXCEL
2 Meaning
What the values actually mean
ICD-10 · SNoMed-CT
3 Description
Data about the data (metadata)
Dublin Core
4 Exchange
How data & models move between tools
PMML · APIs
5 Process
How the team works, end to end
CRISP-DM
Data Standards

_Source slide: 54_

---

## Standard 1 — Representation

1 Representation
Agree on how data is encoded and structured, so any tool can read and
write it.
Data formats CSV · JSON · XML · EXCEL
Schema
Which columns, data types, keys are required.
Text encoding
How characters are stored.
UTF-8 · Unicode

_Source slide: 55_

---

## Standard 2 — Meaning

2 Meaning: what values mean
Agree on the values themselves, so the same thing reads the same
everywhere.
Vocabularies & codes
A fixed list of allowed values.
Example:
heart attack, myocardial
infarction
Identifiers
One agreed name for the same thing.
Units, dates & currency
Written the same way every time.
Example:
Australia, AU, AUS
Example: 5 kg vs 5000 g,
08/09/2026
- Standard vocabularies for use in Medicine, e.g.,
- health codes: disease and health problem codings ICD-10
- systematized nomenclature of medicine, clinical terms, SNoMed-CT

_Source slide: 56_

---

## Standard 3 — Metadata

Metadata: structured information that describes, explains,
locates, or otherwise makes it easier to retrieve, use or
manage an informationresource.
Metadata is:
- data aboutdata
- let other people find it, understand it, and use it
correctly.
- structured so that a computer can process & interpret it
3 Description: MetaData

_Source slide: 57_

---

## Metadata Example — Media File

MetaData
Source: Apple

_Source slide: 58_

---

## EXIF Metadata


_Source slide: 59_

---

## Book Metadata


_Source slide: 60_

---

## Types of Metadata

MetaData can be:
- Descriptive: describes content for identification and
retrieval, e.g. title, author of a book
- Structural: documents relationships and links, e.g.
chapters in a book, elements inXML, containers in MPEG
- Administrative: helps to manage information, e.g. version
number, archiving date, Digital Rights Management (DRM)
MetaData (cont.)

_Source slide: 61_

---

## Why Use Metadata?

Why use metadata?
MetaData
PollEv.com/fit5145chris

_Source slide: 62_

---

## Benefits of Metadata

- Facilitate data discovery
- Help users determine the applicability of the data
- Enable interpretation and reuse
- Clarify ownership and restrictions on reuse
Why Use Metadata
- Standard example:
- Metadata standards, such as Dublin Core, examples at
A Gentle Introduction to Metadata
But it has to be standardised; otherwise, others can’t
find, interpret, or reuse it.

_Source slide: 63_

---

## Metadata Activity

Name a type of descriptive, structural, and administrative
metadata that might be associated with FIT5145.
Question
PollEv.com/fit5145chris

_Source slide: 64_

---

## Standard 4 — Exchange: Data

How data moves between tools:
- Tool A (Python) needs to hand data to Tool B (R, a web app,
another team).
- JSON (JavaScript Object Notation): An open, text-based format
for exchanging data.
- Shared standard, ready-made libraries for reading/writing it
already exist in Python, Perl, Java, and nearly every language
4 Exchange
Python data table R data tableJSON data

_Source slide: 65_

---

## Standard 4 — Exchange: Models

How models move between tools:
4 Exchange
PMML: Predictive Model Markup Language
PMML provides a standard language for describing a (predictive)
model that can be passed between analytic software (e.g. from
R to SAS).
- PMML: An Open Standard for Sharing Models
- A list of products working with PMML is the PMML Powered page
on DMG site.

_Source slide: 66_

---

## Standard 5 — Process

We’ve seen many data
science processes and
lifecycles:
- e.g. our own “standard
Data Science value chain”
- CRISP-DM discussed
previously, is a
standardised data science
process
- statisticians sometimes
use the term exploratory
data analysis for part of
the process
5 Process

_Source slide: 67_

---

## Sourcing and Standards in Action

- Data sourcing
- Open data
- Examples: What, Where & How
to Get Data
- Data standards
- Sourcing + standards in action
- Shell commands

_Source slide: 68_

---

## Issues When Sourcing from Multiple Sources

What issues can we have when sourcing
data from multiple sources?

_Source slide: 69_

---

## Parsing Messy Files

Before you have a table at all, the raw file often isn't shaped like one.
Monthly Sales Report
generated 2026-02-01
suburb 2024 2025
Clayton 410 455
Caulfield 380 399
The real header is row 4, not row 1.
Junk rows on top
title / notes / blank lines above
the header
Fix on read: skip metadata rows, set the true header, drop blank rows/cols, fill
merged cells.
Parse: get a rectangular table out of the file

_Source slide: 70_

---

## Encoding Problems

You saved / expected What opened (wrong encoding)
café → cafÃ©
naïve → naÃ¯ve
한글 → ГЗ°ГЁЂ
→ ЂўЂџ
The fix: read & write everything as UTF-8. The mess happens when a file
saved in one encoding (e.g. Latin-1) is opened as another. Accents, 한글,
emoji break first.
Encoding: why your CSV shows garbage

_Source slide: 71_

---

## Reshaping — Wide and Long Data

WIDE
id jan feb mar
A 5 8 6
B 3 4 9
→
Gather()
LONG
id month value
A jan 5
A feb 8
A mar 6
B jan 3
B feb 4
B mar 9
Rule of thumb: long for analysis & plotting (ggplot loves it), wide for
human reading & reports & summarised table.
Reshape: pivot between wide and long

_Source slide: 72_

---

## Converting Data Types

"1,200" → 1200 string →
number
can't sum or sort
until it's numeric
"2026-02-01" → a Date string → date
can't compute
durations or sort
by time
"yes" / "Y" → TRUE string →
boolean
can't
filter/aggregate
reliably
Classic trap: postcode "0431" read as a number becomes 431 — the
leading zero is gone, and the join to another table fails.
Convert types: text that only looks like data

_Source slide: 73_

---

## Normalising Strings

"··VIC···"
"vic"
"Vic"
→ "vic"
"Ann·Lee··"
"ann··lee"
"ANN·LEE"
→ "ann lee"
Normalise
trim + collapse
whitespace
case-fold (VIC = vic)
strip invisible /
control chars
unify punctuation &
separators
Why first: "VIC" and "vic " are the same key to a human but different
strings to a computer — dedup and join both fail until you normalise.
Normalise strings first, so matching works

_Source slide: 74_

---

## Joining Data Sets

- For data sets to be joined, they must have something
in common.
Joining data sets

_Source slide: 75_

---

## Inner Join

**Inner join:** Keep only records that link between both datasets.

Example source data:

| Product | User |
|---|---|
| Pen | Alec |
| Book | Huang |
| Table | Indira |
| Pen | Indira |
| Chair | Blythe |
| Pen | Huang |

| User | Contact |
|---|---|
| Stef | 733 486 |
| Indira | 989 6732 |
| Boris | 939 3872 |
| Frances | 345 7239 |
| Miguel | 125 8369 |
| Huang | 934 3482 |

_Source slide: 76_

---

## Left Outer Join

**Left outer join:** Keep all records from Set A and linked records from Set B.

Example source data:

| Product | User |
|---|---|
| Pen | Alec |
| Book | Huang |
| Table | Indira |
| Pen | Indira |
| Chair | Blythe |
| Pen | Huang |

| User | Contact |
|---|---|
| Stef | 733 486 |
| Indira | 989 6732 |
| Boris | 939 3872 |
| Frances | 345 7239 |
| Miguel | 125 8369 |
| Huang | 934 3482 |

_Source slide: 77_

---

## Right Outer Join

**Right outer join:** Keep all records from Set B and linked records from Set A.

Example source data:

| Product | User |
|---|---|
| Pen | Alec |
| Book | Huang |
| Table | Indira |
| Pen | Indira |
| Chair | Blythe |
| Pen | Huang |

| User | Contact |
|---|---|
| Stef | 733 486 |
| Indira | 989 6732 |
| Boris | 939 3872 |
| Frances | 345 7239 |
| Miguel | 125 8369 |
| Huang | 934 3482 |

_Source slide: 78_

---

## Full Outer Join

**Full outer join:** Keep all records from both datasets.

Example source data:

| Product | User |
|---|---|
| Pen | Alec |
| Book | Huang |
| Table | Indira |
| Pen | Indira |
| Chair | Blythe |
| Pen | Huang |

| User | Contact |
|---|---|
| Stef | 733 486 |
| Indira | 989 6732 |
| Boris | 939 3872 |
| Frances | 345 7239 |
| Miguel | 125 8369 |
| Huang | 934 3482 |

_Source slide: 79_

---

## Wrangling Quiz

The slide asks you to identify every reason the following merged table is not yet ready for analysis:

| state | suburb | sales_2024 | sales_2025 | rep |
|---|---|---:|---:|---|
| VIC | Clayton | `"1,200"` | 1500 | Ann Lee |
| Victoria | Caulfield | `"980"` | 1010 | `ann lee  ` |
| VIC | Clayton | `"1,200"` | 1500 | Ann Lee |
| NSW | Kingsford | `"cafÃ©"` | 760 | B. Ng |

Potential issues implied by the preceding slides include inconsistent labels, duplicate rows, numeric values stored as strings, whitespace/case inconsistencies, and encoding problems.

_Source slide: 80_

---

## Activity — Scrape, Fix and Join

① SCRAPE · Wikipedia
ICC Men's T20I Team Rankings — last
week's rvest code
read_html() → columns:
Team Matches Points Rating
top 20 teams · reasonably clean (one row
per team)
② CSV · team_runs.csv (wide +
messy)
team runs_2023 runs_2024
IND "4,210" "4,880"
W. Indies "3,700" "3,910"
new zealand "3,560" "3,740"
wide form + key mismatches, comma-
strings, dup rows, encoding
GOAL: join both on Team so each team's yearly runs sit beside its current Rating.
Activity: Scrape it, fix it, join it
Your mission: two messy sources → one tidy table

_Source slide: 81_

---

## Activity Result

Activity: Scrape it, fix it, join it
Resulting table
Can you enter 6 values for
runs and Rating in Poll?

_Source slide: 82_

---

## Bridge to Week 5

The table now has the right shape - but a tidy shape doesn't
mean the values are correct.
Next week we ask whether the data is reliable: missing values,
errors, inconsistencies.

_Source slide: 83_

---

## Shell Commands

- Data sourcing
- Open data
- Examples: What, Where & How
to Get Data
- Data standards
- Sourcing + standards in action
- Shell commands

_Source slide: 84_

---

## Introduction to Scripting Languages

- A script is a series of commands to be performed
- A script is executable on demand
- not compiled to an executable form
- interpreted command-by-command as it is executed, like
on a command line
- Examples:
- R
- Python
- Unix shell
Introduction to scripting languages

_Source slide: 85_

---

## Unix Shell Scripts

- Command-line code for Unix (+ Linux & Mac OS)
- Scales up well for big files!
- Reduces the memory overload
Unix Shell script

_Source slide: 86_

---

## Wrap-Up


_Source slide: 87_

---

## Benefits of Data Sharing and Open Data — Recap

- Solve problems more efficiently through collaboration
and shared resources
- New products, services & business opportunities
- Better research & knowledge
- Public understanding & citizen engagement
Benefits of Data Sharing and Open Data

_Source slide: 88_

---

## Data Standards — Recap

Agreed rules so different systems understand each other. A standard can pin
down five things:
1 Representation
How data is stored & structured
CSV · JSON · XML
2 Meaning
What the values actually mean
ICD-10 · SNoMed-CT
3 Description
Data about the data (metadata)
Dublin Core
4 Exchange
How data & models move between tools
PMML · APIs
5 Process
How the team works, end to end
CRISP-DM
Data Standards

_Source slide: 89_

---

## Role of Data Scientists in Standardisation

- What role do data scientists and data science play in
standardising things related to data?
- Establishing the standards
- Enacting the standards
Setting the standards

_Source slide: 90_

---

## End


_Source slide: 91_

---

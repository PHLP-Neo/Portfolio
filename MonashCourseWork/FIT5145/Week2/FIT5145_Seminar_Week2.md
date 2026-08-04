

## FIT5145
Foundations of data science
Clayton cohort:
Dr. GuanliangChen and Dr. Chris Yun
Faculty of Information Technology, Monash University (Australia)
## Malaysia Cohort:
## Dr. Chern Hong Lim
School of Information Technology, Monash University (Malaysia)

Please notice that ...
•Week 2 Applied Class starts from this week.

## Unit Schedule
WeekContentLecturer
1Overview of data scienceChris Yun
2History and impact of data scienceChris Yun
3Data business modelsChris Yun
4Data sources and standardsChris Yun
5Characterising data and "big" dataChris Yun
6Big Data and data scienceChris Yun
7Supervised data analysis (1)Chris Yun
8Supervised data analysis (2)Chris Yun
9Unsupervised data analysisChris Yun
10Data managementChris Yun
11Issues in data scienceChris Yun
12Future of data scienceGuest Lecturer

Learning Outcomes (Week 2)
By the end of this week, you should be able to:
•Understand the historyof data science and its
impact on our life, science, society, social good
and the future.
•Comprehend the essentials for coding in R for data
science.
•Present R scripting in R Markdown.
•Explain and do data reading, data wrangling and
visualisation in R coding.

Topics for Lecture 2
1.History of Data Science.
2.Impact of Data Science.
3.Introduction to R and R Markdown.
4.Data reading.
5.Data wrangling
6.Visualisation.

History of Data
## Science
## 01
How did Data Science Evolve
(Textbook Section 1.4)

Data science is about
What is data science? (Revisiting)

Data science is about
•technology for working with data
•processes for working with data
•getting value from data
in a way that is effective and consistent.
What is data science? (Revisiting)
So why is it regarded as something “new”?

Evolution of Data Science as a Discipline
Data Science has developed in fits and starts, from many
precursors:
•Data Analysis (John Tukey) in 1962
•Expert Systems in the 1980’s
•Machine Learning in the 1980’s
•Data Mining in the 1990’s

Source: https://www.slideshare.net/slideshow/embed_code/36866068
Timeline of Data Science

If these fields existed for decades, why did data
science suddenly become popular after 2000?
Evolution of Data Science ...

Data Science emerges around 2000
•Dot.Comboom
•“data” as a valuable asset and business pressure on decision
making
•William Cleveland published in 2001 “Data Science: An
Action Plan for ... the field of Statistics”
•Data managementand the data/information society
•Dot.Com companies show the way
See also David Donoho’s “50 years of Data Science” (PDF paper)
Evolution of Data Science ...

## The Internet
## + Big Data
+ Increased computing power
+ Business demand for data-driven decisions
## ↓
The emergence of Data Science
Evolution of Data Science ...

## The Hype Cycle
Gartner’s Hype Cycle attempts to quantify the level of maturity of various technologies:

Hype Cycle in 2014
Can you
spot Data
## Science?

Hype Cycle for Analytics and Business Intelligence in 2019

Hype Cycle for Data Science and Machine Learning 2021

Hype Cycle for Data Science and Machine Learning 2022

Hype Cycle for AI 2023

How Early Rule-Based Chatbots Worked
One of the earliest Rule-based chatbot:
-ELIZA (1966) –Talk to ELIZA
https://www.masswerk.at/elizabot/?utm_source=chatgpt.com
IF the user message contains: "book" and ("hotel" OR "room")
THEN respond: "Sure, could you tell me the location and date?"
I need a place to stay???
•Example: A rule-based hotel chatbot
Sorry, I don’t understand.

How Machine Learning-Based Chatbots Worked
Provide question list to chatbot:
-I want to reserve a room
-Book a hotel for me
-I need a place to stay
## -...
ML understands intent →
## Hotel Booking
Sure, could you tell me the
location and date?
-Can I check in early and also get a
room with a city view?
Sorry, I don’t understand.
•Example: A machine learning-based hotel chatbot

Why Generative AI exploded after 2022?
-Massive data from
the Internet:
websites, books,
Wikipedia, social
media
-Huge computing
power (GPUs): Massive
parallel computation
-AI architecture:
## Transformer
Generative AI boom

Hype Cycle for AI 2024
What can we observe?

Hype Cycle for AI 2025
What can we observe?

Relationship of Data Science to Other Disciplines
See Battle of the Data Science Venn Diagrams for more.

## Data Science Research
•Data Science is seeing major growth at universities
internationally.
•Many research programs exist, including here at Monash:
•AiLECS Lab - an initiativebetween Monash University and the
Australian Federal Police (AFP)designed to help officers scan
through thousands of confronting images and files faster with
lower levels of emotional distress
•Google grant to establish world-first suicide monitoring
system
•Australia's first high-resolution vegetation map
•Centre for Learning Analytics Monash

Source: https://www.monash.edu/ai-data-science

## 02
Impact of Data
## Science
Some examples of how data science is
impacting others:
•Your life on the cloud:
... datafication of you
•Science and social good
... scientific method holds true, but broadens
technology
•Futurology
... healthcare and automobiles
(Textbook Section 1.6)

## 02
Impact of Data
## Science
Some examples of how data science is
impacting others:
•Your life on the cloud:
... datafication of you
•Science and social good
... scientific method holds true, but broadens
technology
•Futurology
... healthcare and automobiles
(Textbook Section 1.6)

Our personal information is increasingly stored in the cloud:
•GenAI (Chatgpt, Claud)
•social life (Instagram, Facebook),
•Entertainment/shopping (Neflix, Amazon),
•career (LinkedIn),
•search history (Google, etc.),
•health and medical (Fitbit, TBD),
•music (Apple), ...
Your Life on the Cloud

Our personal information is increasingly stored in the cloud:
•GenAI (Chatgpt, Claud)
•social life (Instagram, Facebook),
•Entertainment/shopping (Neflix, Amazon),
•career (LinkedIn),
•search history (Google, etc.),
•health and medical (Fitbit, TBD),
•music (Apple), ...
This provides many, many, many advantages:
•personalisation, convenience and personal agents
Your Life on the Cloud

Your Life on the Cloud (cont.)
But alsosome disadvantages:
•Privacy risks
•Security breaches
•Loss of control: What if you don’t have rights to
access/delete data?
•Surveillance and profiling
•Unexpected data sharing
•Biased automated decisions

## 02
Impact of Data
## Science
Some examples of how data science is
impacting others:
•Your life on the cloud:
... datafication of you
•Science and social good
... scientific method holds true, but broadens
technology
•Futurology
... healthcare and automobiles
(Textbook Section 1.6)

Scientific Method and Data Science
What is the relationship?
How does Data Science affect the
## Scientific Method?

What is a Scientific Method?
Smokers seem to have higher rates of lung
cancer.
Smoking increases the risk of lung cancer?
Smokers are more likely to develop
lung cancer than non-smokers.
Observing Group A (1000 smokers), Group B
(1000 non-smokers) for 20 years
Collect data on lung cancer diagnoses
Statistical testing, modelling

Chris Anderson’s blog in Wired 23/05/2008
The End of Theory

## Example:
Google search
→Why is this page ranked at the top of the search results?
YouTube recommendations
→Why are these videos recommended to me?
Lung cancer detection
→Can we predict whether a patient has lung cancer from medical data?
## Big Data: Do We Still Need Science?

•Predicting
population
growth
•A complex model of
obesity:
## Obesity Systems Map
To Understand the Issues ...
## Source: Integrating Urban Growth Models, Pearlstine,
Mazzotti, Pearlstine and Mann,2004

•Philosopher Massimo Pigliucci says:
Science is not about finding patterns–...–it is about finding
explanations for those patterns.
Not The End of Theory
•Example
-Population growth: Without causal understanding, we cannot
plan cities, manage resources, and forecast sustainability
-Obesity: We may predict correctly, but we cannot design
solutions.

Data Science for Science
Rather than replacing science, data science enhances it.
•Data science can identify hidden patterns in large datasets (e.g.:
Genomics, Physics, bioinformatics, and earth science)
→Hypothesis generation
•Analysing much larger datasets
•Improving predictions
•Providing new sources of scientific data (e.g.: social media,
wearable devices, satellites)
•Programming tools: Making research faster and more reproducible

## Examples:
•Data Science for Social Good movement training data scientists to
support community and charity.
-Public health, poverty analysis, disaster response, urban planning
Data Science for Social Good

A hospital builds a machine learning model that predicts
which patients are likely to develop breast cancer, but
the model does not explain why.
This is an example of:
## Question
PollEv.com /fit5145chris

Which example shows data science helping
scientific research?
## Question
PollEv.com /fit5145chris

## 02
Impact of Data
## Science
Some examples of how data science is
impacting others:
•Your life in the cloud:
... datafication of you
•Science and social good
... scientific method holds true, but broadens
technology
•Futurology
... healthcare, agentic AI and automobiles
(Textbook Section 1.6)

## Health Care
See “Big data – 2020 vision” talk by SAP manager John Schitka
Source: AI generated image

Agentic AI -Marketing
A real task: “Online sales dropped 18% last month — find out why and
suggest what to do.”
YOU set the goal
“Sales are down 18% —
find the cause and
recommend actions.”
Your only job:
Set the goal, then
approve the plan.
The agent then works autonomously:
Gathers the data
Queries the sales database & web analytics
Finds the pattern
Drop is concentrated in repeat buyers in VIC
Diagnoses the cause
Matches a 10% price rise + a competitor promo
Takes action
Drafts a win-back email + targeted discount
Result:  a diagnosed cause + a ready-to-run campaign - in minutes, not days.

Self autonomous driving
Data science turns raw sensor data into real-time driving decisions.
SENSE  ·  inputs
## Camera
LiDAR / Radar
GPS / Maps
Traffic data
ACT  ·  decisions
Detect lanes & cars
Predict pedestrians
Plan safest route
Brake / steer
## Data Science
## + AI
Without data science, a car cannot turn raw sensor data into safe driving decisions.

Self-driving cars:
•how does the city replace traffic fine revenue?
•can you drink and drive if the car is automatic?
•what happens to the taxi industry?
•what happens to the auto insurance industry?
•what happens to people still “self” driving, and their insurance?
Self autonomous driving
See “Big data – 2020 vision” talk by SAP manager John Schitka

## Introduction
to R
## 03
## R, R Markdown, Data Reading,
## Data Wranglingand
## Visualisation
Materials adapted from the
## Microcredential

1.History of Data Science.
2.Impact of Data Science.
3.Introduction to R and R Markdown.
4.Data reading.
5.Data wrangling.
6.Visualisation.
Topics for Lecture 2

R is a programming language.
•Reproducible
•Adaptable
R was originally created for statisticians.
•Functional
•Specialised
R is great in terms of ...
•Large community
•Commonly used for business intelligence
R is powerful in drawing graphs.
•Practical
•Communicative
## R: A Powerful Data Science Tool

RStudio is a programming environment for R.
•Helps manage the workflow
•Projects – a filing cabinet for your work!
•Libraries of packages
•Works with R scripts from files and the command-
line
RStudio, a tool for R

To maintain a reproducible workflow, you need to record
what steps you take in a process.
•This is vital when dealing with data
R Markdown is an authoring format (.Rmd files) that enables
us to combine embedded R code with formatted text, so we
can:
•Explain our thoughts and process
•Discuss the coding required
•Present the output of the processing
•Interpret the output
•Allow others to reproduce it all!
## R Markdown

R Markdown format
Please also refer to the material in Week 1
•Introduction to R Markdown
## # Top Heading
## ## Sub-heading
-List item 1
-List item 2
[Link to Monash](https://my.monash.edu)
##### This is my first coding practice.
## ```{r}
# this code adds up numbers.
## 1+1
## ```

Once you finish writing the content, you can knit the R
Markdown and create the output file.
Using RStudio to knit ... this
## Knitting R Markdown

Installing and Importing the Tidyverse
Tidyverseis a collection of R packages designed for data
science and data analysis. It works well for tasks such as data
manipulation, data reshaping, and data visualization.
•Core packages included:
ggplot2–data visualisation
dplyr–data manipulation (filter, select, mutate, summarise)
tidyr–data reshaping (pivot_longer, pivot_wider)
readr–reading data files
tibble–modern data frames
•Installing and loading the tidyverse
install.packages("tidyverse")              # install the tidyversepackage
library(tidyverse)                                  # load tidyverseinto the R session

Reading data in R
•Local datasets (e.g.: csv, excel) from your computer
data <-read_csv(" student.csv ")
•Web scraping: Extracts content from an HTML webpage.
•Web APIs: Sends a structured request and receives structured
data, usually in JSON format.
•Databases and cloud data platforms: Connects to structured
data stored in databases, data warehouses, or cloud storage
(e.g.: Google, Amazon, or Microsoft).

Reading data in R
•Local datasets (e.g.: csv, excel) from your computer
data <-read_csv("student.csv")
student_idagegenderscoreexam_date
## 3232424420M851/05/2025
## 3232424521F901/05/2025
32324246NAMale881/05/2025
3232424719F500May 1 2025
## 3232424822female761/05/2025
## 3232424920M-101/05/2025
Example of student dataset

Reading data in R
•Web APIs:Send a request to server and you receive data (one
request at a time)
request
return the
data in JSON
Your code
## R / Python
API server
extracts the data
## Data
usually JSON
•Databases & cloud platforms: Connect to structured data that is
already stored, then query it
connect
Your code
## R / Python
Cloud storage
## Google · Amazon ·
## Microsoft
## Data
warehouses
## Database
or
or

What does Exploratory Data Analysis
(EDA) mean?

•Get to know your data before advanced analysis and modelling.
## 1. Understand
structure
E.g.: How many
rows and
columns? What
type is each
variable?
- Check data
quality
(Data wrangling)
E.g.: Find missing
values,
duplicates, and
impossible
entries.
## 3. Summarise
## E.g.: Central
tendency and
spread of each
variable.
## 4. Visualise
## E.g.: See
distributions and
relationships
between
variables.
Exploratory Data Analysis (EDA)
Advanced analysis such as Machine learning model, Statistical testing, or Any
advanced analysis to reveal patterns and insights
After that...

What does Data Wrangling mean?

•Not all data can be used straight away
•Not all data is clean and tidy
•We need to wrangle the data into shape!
## Data Wrangling
is the process of transforming “raw” data
into data that can be analysed
to generate valid actionable results
and insights.
Wrangling the data

•Mistakes in Data?
When is wrangling needed?
student_idagegenderscoreexam_date
## 3232424420M851/05/2025
## 3232424521F901/05/2025
32324246NAMale881/05/2025
3232424819F500May 1 2025
## 3232424822femaleabsent1/05/2025
## 3232424920M-101/05/2025

•Missing Values: NA
•Inconsistency: M, F, Male, and female in Gender
•Incorrect Formats: 1/05/2025 and May 1 2025 in
exam_date
•Outliers: 500 and -10 in score
•Incorrect data type: absent in score
•Duplicates: 32324248 in student id
•What else?
When is wrangling needed?

•Too much data
✓Filter out stuff you don’t need
✓Identify what you do need
•Combinations of data
✓Link associated elements in different data sets
✓Merge data sets
When is wrangling needed?

•Discretisationof data
✓Transforming continuous data
When is wrangling needed?
personage
## A7
## B15
## C24
## D38
## E70
personageage_group
A7Child
B15Teen
C24Adult
D38Adult
E70Senior
-A range for each group
## 0 --------12 --------18 ----------------65 --------100
## Child       Teen              Adult          Senior

One example of data wrangling is to
extract dates from text and convert
them to a digitized date format.
Which of the following text can be a challenge in
converting them to a digitized date format?
## A.next Tuesday
B.January 3 next year
C.3rd Friday in the month
## D.03/12/18
## Question
PollEv.com /fit5145

Tidy data is a standard structure that data
wrangling often aims to produce:
•Each variable is a column.
•Each observation is a row.
•Each value is a cell.
Tidy data

Tidy or Messy?
studentmath_scoreenglish_score
## Alice8590
## Bob7882
## Chris9288
•Suppose we record students' exam scores.
There are 2 variables in this column!

Tidy or Messy?
student
math_
score
english_
score
## Alice8590
## Bob7882
## Chris9288
•Suppose we record students' exam scores.
studentsubjectscore
AliceMath85
AliceEnglish90
BobMath78
BobEnglish82
ChrisMath92
ChrisEnglish88

Data is often in a wide format, with lots of columns; or
a long format, with lots of rows.
•Depending on your needs, reshape the data from wide
to long format or vice versa.
•In R, use the following functions in tidyverse package:
## •gather
## •spread
## •separate
Reshaping Data in R

Reshaping Data in R
car
measurementvalue
Mazda RX4
mpg
## 21
Mazda RX4
## Cyl
## 6
Mazda RX4disp
## 160
Mazda RX4 Wagmpg
## 23
Mazda RX4 Wagcyl
## 4
Mazda RX4 Wagdisp
## 120
carmpgcyldisp
Mazda RX4216160
Mazda RX4 Wag23
## 4
## 120
•Wide form
•Long form

Mtcarsdata: A built-in dataset in R that contains
information about 32 cars and their performance
characteristics.
Gather (pivot_longer) transforms messy data to a tidy
‘long’ form. You will need
•key (identifier) – new variable for the gathered columns
•values (measures) – new variable for the gathered values
•names – names of columns to be gathered
mtcars%>% gather(key = "measurement", value = "value")
Tidy data: Gather

Reshaping Data: Wide to Long with gather()
gather(key =
"measurement", value =
## "value“, -car)
car
measurementvalue
Mazda RX4
mpg
## 21
Mazda RX4
## Cyl
## 6
Mazda RX4disp
## 160
Mazda RX4 Wagmpg
## 23
Mazda RX4 Wagcyl
## 4
Mazda RX4 Wagdisp
## 120
## ...
carmpgcyldisp
Mazda RX4216160
Mazda RX4 Wag23
## 4
## 120
•key –new variable for the
gathered columns
•values –new variable for
the gathered values

Gatherpractice-Temperature Data
gather(key = ???,
value = ???, ???)
cityJanFebMar
## Melbourne252624
## Sydney272826
city
MonthTemperature
## Melbourne
## Jan
## 25
## Melbourne
## Feb
## 26
## Melbourne
## Mar
## 24
## Sydney
## Jan
## 27
## Sydney
## Feb
## 28
## Sydney
## Mar
## 26

Reshaping Data: Long to Wide with spread()
spread(key =
"measurement", value =
## "value“)
car
measurementvalue
Mazda RX4
mpg
## 21
Mazda RX4
## Cyl
## 6
Mazda RX4disp
## 160
Mazda RX4 Wagmpg
## 23
Mazda RX4 Wagcyl
## 4
Mazda RX4 Wagdisp
## 120
carmpgcyldisp
Mazda RX4216160
Mazda RX4 Wag23
## 4
## 120
## Spreadtransforms ‘long’
to a tidy ‘wide’ form,
which works like gather
but in reverse

•Mistakes in data
•Reshaping
•Combining
•Filtering
•Transforming
## •...
## Data Wrangling

Why do we visualise data?

Life expectancy by continent
## 35
## 45
## 55
## 65
## 75
## 85
## 1960197019801990200020102020
Life expectancy (years)
AfricaAsiaEuropeAmericas

Population by state & age
## 0
## 2
## 4
## 6
## 8
## 10
## NSWVICQLDWASA
## Population (millions)
## Under 1515–6465+

Student performance
## 40
## 50
## 60
## 70
## 80
## 90
## 100
## 051015
Exam score
Study hours / week
## Tutorial A
## Tutorial B
## Tutorial C

Number of people walking on each
street by time of day in January

## Visualisation
R can be used to create a wide range of data
visualisations.
ggplot2: the main package used
You will create and interpret many different types of
charts in the applied classes!

Thank you!
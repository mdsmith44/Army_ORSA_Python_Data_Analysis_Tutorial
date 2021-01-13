## Army ORSA Python Data Analysis Tutorial Outline

### Lesson 1: Intro to Python and Jupyter Notebooks
- Why Python
- Jupyter Notebook Environment
- Basic Python Syntax: code syntax, comments, assigning variables, installing packages
- Data Types
  - Individual Types: numbers, strings, booleans, None type, Type-Casting
  - Composite Data Structures: lists, tuples, sets, dicts, comprehensions, Oh My..
- String Matching: regular expression, fuzzy matching
- Code Structures 
  - if-else controls
  - for/while loops
  - try-except
  - functions
  - classes
- Numpy Basics

### Lesson 2: Data Management with Pandas
- Pandas Data Structures: DataFrame and Series
    - Pandas Overview
    - DataFrame and Series Objects
    - Working with Data by Index and Columns
    - Removing Data
    - Multi-Level Indexing
    - Common Series Methods
    - Filtering and Sorting Data
- Getting Data
    - From Files
    - From User Generated Data
    - Webscraping
    - Writing and Saving Data
- Cleaning Data
    - Handling Nulls
    - Using Where Functions
    - String Matching and Cleaning
- Data Wrangling and Manipulation
    - Applying Functions and Transformations
    - Joining/Merging Data Sets
    - Aggregating Data: Groupby and Pivot Tables
- Handling Dates and Times

### Lesson 3: Data Visualization
- Matplotlib
    - Quick Matplotlib Orientation
    - Figures, Axes, and Subplots
    - Common Plot Types
    - Labeling Plots
- Plotting with Pandas
    - Pandas Plotting Overview
    - Example: Plotting GFEBS Data
- Seaborn
- Interactive Graphics with Bokeh
    - Example: COVID19 Dashboard
- Making GIFs

### Lesson 4: Machine Learning and Other Topics
- Machine Learning with scikit-learn
    - Scikit-Learn Overview: Linear Regression
    - Data Prep
        - Data Reduction with PCA
        - Train-Test Splits
    -  Classification
        - Multi-Layer Perceptron Neural Nets (MLPs)
        - Logistic Regression
        - Random Forest
        - Decision Trees
        - K Nearest Neighbors
    - Cross Validation with GridSearch
    - Unsupervised Learning / Clustering
- Other Data Analysis Tools
    - Natural Lanugage Processing with nltk
    - Network Analysis with networkx
    - Statistical Modeling and Time Series Analysis with statsmodel
    - Optimization
    - Simulation
    - Association Analysis

## References
With an active development community, there are now many resources and references avaialable to learn how to do data analysis in python.  Depending on your learning style, level of interest, and specific area of interest, here are some resources you may find useful.  

Many good textbooks are available on the O'Reily Learning (formerly called Safari Online Books) platform, which is available free to those with a .mil email address through the DoD MWR Online Digital Library: https://www.militaryonesource.mil/recreation-travel-shopping/recreation/libraries/morale-welfare-and-recreation-digital-library. Here are some great python data analysis references on that platform.  If there's another area you are interested in, it's worth searching the O'Reily library to see if they have a book on that topic.  
- *Python for Data Analysis*, by Wes McKinney (https://learning.oreilly.com/library/view/python-for-data/9781491957653/).  If you're just going to work through one resource I'd recommend this one.  It goes into great detail on the ins and outs of data management with pandas, and introduces visualization and other data analysis extensions.
- *Introducing Python*, by Bill Lubanovic (https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/).  The McKinney book gives enough of a python primer to get started, but if you want to dig into more details on the python language (e.g. if you want to do serious development) then this is a good resource.  
- *Introduction to Machine Learning with Python*, by Andreas C. Müller, Sarah Guidom (https://learning.oreilly.com/library/view/introduction-to-machine/9781449369880/).  There's a ton of ML books and resources out there.  I like this one because it does a gives a good overview of HOW to implement models in python, and also gives good overview and intuition for the math and intuition behind the techniques. 
- *Applied Text Analysis with Python* (https://learning.oreilly.com/library/view/applied-text-analysis/9781491963036/) is an excellent resources for diving into text analysis, natural language processing, topic modeling with python.


Another great reference is Coursera, specifically the sequence Applied Data Science with Python specialization (https://www.coursera.org/specializations/data-science-python).  It contains the following 5 courses:
- Introduction to Data Science with Python (covers pandas)
- Applied Plotting, Charting & Data Representation in Python (mainly focuses on matplotlib)
- Applied Machine Learning in Python
- Applied Text Mining in Python
- Applied Social Network Analysis in Python

All the courses are great, and also will give you some useful code you can re-use.  All the courses are also conducted in Jupyter environment which is great practice.  

Some other freely available resources that could be useful:
- W3 Python Tutorial (https://www.w3schools.com/python/).  A good free tutorial, which also makes for a nice easilly accessible reference.
- An Introduction to Statistical Learning: https://link.springer.com/book/10.1007/978-1-4614-7138-7.  Technically this one gives its examples in R, but it's a great overview of the math and theory of machine learning topics so can't make a list of Data Analysis references without it!
- Kaggle Courses (https://www.kaggle.com/learn/overview) offers a variety of useful and succinct lessons covering many areas of data analysis in python.  All courses are presented through interactive Jupyter notebooks, similar to this tutorial. 

Any and all feedback welcome!  
-Matt Smith, mdsmith44@gmail.com

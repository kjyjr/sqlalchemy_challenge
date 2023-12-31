# SQL Alchemy Challenge

This assignment consisted of a climate analysis of the Honolulu, Hawaii area as part of planning a fictional trip there. The assignment was comprised of two parts.

Climate Data Exploration and Analysis

In the first part, Python and SQL Alchemy were used to conduct a basic climate analysis and exploration of a climate database. For those, SQL Alchemy ORM queries were performed, along with Pandas and Matplotlib. SQL Alchemy was used to connect to an SQLite database and to reflect tables into classes for reference in conducting a precipitation analysis and weather station analysis. Results of those analyses were then loaded into a Pandas dataframe and subsequently plotted into a dot plot graph and histogram.

Climate App

In the second part, a Flask API was designed based on the queries developed in part one. Query results from the precipitation analysis were converted to a dictionary and returned via a JSON representation. Further JSON lists were also produced for stations and two sets of temperature observations: one for a user-selected start date and its subsequent dates available in the dataset and another set for a user-selected date range. Both sets of temperature observations consisted of minimum, average, and maximum temperatures for the dates selected.

 

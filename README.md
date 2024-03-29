Winnipeg Weather Processor
==========================

This application is for scrapping weather data from the [Government of Canda's website](https://climate.weather.gc.ca/index_e.html) and processing the data to generate 
monthly and yearly graphs for analysis. It's currently set to scrape data for Winnipeg Manitoba, but could be adjusted if required. 

I developed this application for my final project for a Python class I took in [Red River College's BIT Program](https://catalogue.rrc.ca/Programs/WPG/Fulltime/BUSGF-DP) :)

How it works
------------

This application does three things. 

First, it scrapes weather data from the Government of Canda's website via [HTMLParser](https://docs.python.org/3/library/html.parser.html).

Second, it processes the data by filtering out bad data (i.e. nulls and non-numerics). The data is stored in an SQLite database.

Third, the application will generate either box plots or line plots via [Matplotlib](https://matplotlib.org/) depending on user input. Users can either request graphs for monthly average 
temperature from a set of years (e.g. 1999 – 2003) or a daily average temperatures for a specific month (e.g. January 2009).

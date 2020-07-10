# sqlalchemy-challenge

### Step 1 - Climate Analysis and Exploration

To begin, I used Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database. All of the following analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.
- The hawaii.sqlite file was used to complete the climate analysis and data exploration.
- I chose a start date and end date for your trip
- I then used SQLAlchemy create_engine to connect to the sqlite database.
- Then used SQLAlchemy automap_base() to reflect the tables into classes and save a reference to those classes called Station and Measurement.

Precipitation Analysis
- Designed a query to retrieve the last 12 months of precipitation data.
- Loaded the query results into a Pandas DataFrame and set the index to the date column.
- Plotted the results using the DataFrame plot method.

Station Analysis
- Designed a query to calculate the total number of stations.
- Designed a query to find the most active stations.
 -- Listed the stations and observation counts in descending order.
 -- Used this to find the station that has the highest number of observations
- Designed a query to retrieve the last 12 months of temperature observation data (TOBS).
 -- Filtered by the station with the highest number of observations.
 -- Plotted the results as a histogram with bins=12.

### Step 2 - Climate App
Once the initial analysis was complete, I then designed a Flask API based on the queries that I developed.
- I used Flask to create your routes.
- Listed all routes that are available.
- I converted the query results to a dictionary using date as the key and prcp as the value.
- Returned is the JSON representation of the dictionary.

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return precipitation data"""
    # Query precipitation data for last year in database
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').filter(Measurement.date <= '2017-08-23').all()

    session.close()

    year_precip_dict = []
    for date, precipitation in results:
        precip_dict = {}
        precip_dict['date'] = date
        precip_dict['precipitation'] = precipitation
        year_precip_dict.append(precip_dict)

    return jsonify(year_precip_dict)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return station data"""
    # Query data for all stations
    results = session.query(Station.station).all()

    session.close()

    stations = list(np.ravel(results))

    return jsonify(stations)


app.route("/api/v1.0/tobs")
def temperature():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return temperature data"""
    # Query temperature data from most active station for last year of data
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= '2016-08-23').filter(Measurement.date <= '2017-08-23').filter(Measurement.station == "USC00519281").all()

    session.close()

    year_temp_dict = []
    for date, temperature in results:
        temp_dict = {}
        temp_dict['date'] = date
        temp_dict['temperature'] = temperature
        year_temp_dict.append(temp_dict)

    return jsonify(year_temp_df)

app.route("/api/v1.0/<start>")
def startTemp(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return temperature data from start date"""
    # Query temperature data from from a given start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= "start").all()

    session.close()

    return jsonify(results)

app.route("/api/v1.0/<start>/<end>")
def startEndTemp(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return temperature data"""
    # Query temperature data from most active station for last year of data
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= "start").filter(Measurement.date <= "end").all()

    session.close()
    
    temps_dates = list(np.ravel(results))

    return jsonify(temps_dates)

if __name__ == '__main__':
    app.run(debug=True)

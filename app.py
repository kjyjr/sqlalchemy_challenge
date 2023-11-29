# Import the dependencies.
import numpy as np
import datetime as dt

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
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    return (
        f"Aloha! Welcome to my page of climate data from beautiful Hawaii! <br><br>"
        f"Your available routes are: <br>"
        f" - home (/) <br>"
        f" - Precipitation (/api/v1.0/precipitation) <br>"
        f" - Weather Stations (/api/v1.0/stations) <br>"
        f" - Temperature Observations (TOBS) (/api/v1.0/tobs) <br>"
        f" - Start Date for TOBS (/api/v1.0/date formatted as YYYY-MM-DD) <br>"
        f" - Start to End Date Range for TOBS (/api/v1.0/start date formatted as YYYY-MM-DD/end date formatted as YYYY-MM-DD) <br><br>"
        f"Enjoy!"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    query_results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= query_date).all()
    precip_results = []
    for date, prcp in query_results:
        precip_dict = {}
        precip_dict['date'] = date
        precip_dict['prcp'] = prcp
        precip_results.append(precip_dict)
    return jsonify(precip_results)

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results)) 
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= query_date)\
        .filter(Measurement.station == 'USC00519281').all()    
    tobs = list(np.ravel(results)) 
    return jsonify(tobs)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def new_function(start=0, end=0):
    selection = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    start_results = session.query(*selection).filter(Measurement.date >= start).all()
    start = list(np.ravel(start_results))
    return jsonify(start)
    start_end_results = session.query(*selection).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    start_end = list(np.ravel(start_end_results))
    return jsonify(start_end)

if __name__ == "__main__":
    app.run(debug=True)

session.close()
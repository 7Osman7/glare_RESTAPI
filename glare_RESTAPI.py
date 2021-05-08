#!flask/bin/python
from flask import Flask, request, jsonify
import errors
from pysolar import solar
import datetime 
import pytz
from timezonefinder import TimezoneFinder
import time

app = Flask(__name__)
app.register_blueprint(errors.blueprint) #Import errors blueprint
app.config['JSON_SORT_KEYS'] = False #Prevent auto sorting of JSON elements to preserve error format

@app.route('/detect_glare', methods=['POST'])
def glare():
    glare = None

    #Throw exception if not json
    if not request.is_json:
        raise errors.ValidationError('Please Enter a JSON')

    request_data = request.get_json()
    
    #Throw exception if missing field or outside allowable range
    fields = ['lat', 'lon', 'epoch', 'orientation']
    field_range = {
                  "lat": 90,
                  "lon": 180,
                  "epoch": time.time(),
                  "orientation": 180
                  }
    for field in fields:
        if not field in request_data:
            raise errors.ValidationError('Missing one of the inputs. Please ensure you have ' + field)
        if abs(float(request_data[field])) > field_range[field]:
            raise errors.ValidationError('Input outside allowable range. Change your ' + field)


    lat = float(request_data['lat'])
    lon =float(request_data['lon'])
    epoch = float(request_data['epoch'])
    orientation = float(request_data['orientation'])
    
    #Get altitude and azimuthal difference and check glare conditions
    alt, sun_orientation = sun_positon(lat, lon, epoch)
    if alt < 45.0 and  abs(orientation-sun_orientation) < 30.0:
        glare = "true"
    else:
        glare = "false"
    return jsonify({'glare': glare}), 201


# --- Sun Position finding function ---
def sun_positon(lat, lon, time):
    tzfinder = TimezoneFinder()
    timezone = tzfinder.timezone_at(lng = lon, lat = lat)    #Find timezone at specified lat and lon
    date = datetime.datetime.fromtimestamp(time, pytz.timezone(timezone))
    alt = solar.get_altitude(lat, lon, date)
    sun_orientation = solar.get_azimuth(lat, lon, date)
    return alt, sun_orientation


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) # IMPORTANT: set debug to False if in production stage

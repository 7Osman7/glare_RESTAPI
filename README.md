# glare_RESTAPI

**Introduction**


**Perquisites:**

* Software
  * Postman
 
* Python libraries:
  * Flask
  * pysolar
  * timezonefinder
  * pytz


**Usage:**

1. Open Postman and create a new workspace
2. Change method to POST
3. Put the endpoint as "http://localhost:5000/detect_glare"
4. Post a JSON Object in the following format:
       {
    "lat": " a float between 90 and -90",
    "lon": "a float between 180 and -180, 
    "epoch": "a float less than current epoch",
    "orientation": "a float between 180 and -180"
    }

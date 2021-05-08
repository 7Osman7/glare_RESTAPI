# glare_RESTAPI

**Description:**

This is a REST API created in Flask that takes in an image's metadata and determines if there is a possibility of direct glare in the associated image 
or not. This relies on finding the altitude angle of the sun, as well the azimuthal angle difference between the sun and the direction of a forward facing camera mounted on a car. The API returns a JSON object of the form:

 {
 “glare”: “true or false”,
}


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
3. Set the endpoint as "http://localhost:5000/detect_glare"
4. Post a JSON Object in the following format:
       {
    "lat": " a float between 90 and -90",
    "lon": "a float between 180 and -180, 
    "epoch": "a float less than current epoch",
    "orientation": "a float between 180 and -180"
    }

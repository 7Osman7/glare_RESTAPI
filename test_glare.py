from glare_RESTAPI import app 
import unittest
from flask import jsonify
app.testing = True
import json

class FlaskTests(unittest.TestCase):
    
    #Test for 201 response from POST method
    def test_index(self):
        tester = app.test_client(self)
        input = {
            "lat": "49.2699648",
            "lon": "-123.1290368", 
            "epoch": "1588704959.321",
            "orientation": "-10.0"
            }
        result = tester.post("/detect_glare", json = input)
        statuscode = result.status_code
        self.assertEqual(statuscode, 201)

    #Test for json data result
    def test_index_content(self):
        tester = app.test_client(self)
        input = {
            "lat": "49.2699648",
            "lon": "-123.1290368", 
            "epoch": "1588704959.321",
            "orientation": "-10.0"
            }
        result = tester.post("/detect_glare", json = input)
        self.assertEqual(result.content_type, "application/json")

    #Test if the returned json has the expected data/message
    def test_index_message(self):
        tester = app.test_client(self)
        input = {
            "lat": "49.2699648",
            "lon": "-123.1290368", 
            "epoch": "1588704959.321",
            "orientation": "-10.0"
            }
        result = tester.post("/detect_glare", json = input)
        self.assertTrue(b'glare' in result.data)

    #Test the result given metadata that is outside allowable range (range error)
    def test_range_error(self):
        tester = app.test_client(self)
        input = {
            "lat": "49.2699648",
            "lon": "-123.1290368", 
            "epoch": "1588704959.321",
            "orientation": "-1000.0"
            }
        result = tester.post("/detect_glare",  json = input)
        self.assertTrue(b'Input outside allowable range.' in result.data)
       
    #Test missing inputs error
    def test_input_missing(self):
        tester = app.test_client(self)
        input = {
            "lat": "49.2699648",
            "lon": "-123.1290368", 
            "epoch": "1588704959.321",
            }
        result = tester.post("/detect_glare", json = input)
        self.assertTrue(b'Missing one of the inputs.' in result.data)


if __name__ == '__main__':
    unittest.main()
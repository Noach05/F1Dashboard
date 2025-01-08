from flask import Flask, render_template
from urllib.request import urlopen
import json

app = Flask(__name__)

key_mapping {
    "session_key": "Overall Session Number",
    "session_name": "Session",
    "date_start": "Event Start Date and Time",
    "date_end": "Event End Date and Time",
    "gmt_offset": "Time Difference from GMT",
    "session_type": "Session Type",
    "meeting_key": "Meeting Number",
    "location": "Location",
    "country_key": "Country Key",
}


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/latest')
def latest():
    response = urlopen('https://api.openf1.org/v1/sessions?session_key=latest')
    data = json.loads(response.read().decode('utf-8'))
    return render_template('latest.html', data=data)


if __name__ == '__main__':
    app.run()

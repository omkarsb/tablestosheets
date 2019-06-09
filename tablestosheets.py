from bottle import route, run

# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route

import pandas as pd

import gspread
from oauth2client.client import GoogleCredentials

from oauth2client.service_account import ServiceAccountCredentials


import gspread_dataframe as gd
from gspread_dataframe import set_with_dataframe

gc = gspread.authorize(GoogleCredentials.get_application_default())

scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

sh = gc.create('hello.py')


@route('/')
def hello_world():

    return '''
	<html>
            <body>
                <center>Enter Your Email Address:</center>
                <br/>
                    <center><input name="email" /></center>
                    <br/>
                    <center><input type="submit" value="Generate HexCode" /></center>
                    <br/>
                    <center><input name="hexcode" /></center>
                    <br/>
                    <center>
                        File Name(Optional):<input name="hexcode" /><input type="submit" value="Create Link" /><br/>
                        File Name(Optional):<input name="hexcode" /><input type="submit" value="Create Link" /><br/>
			File Name(Optional):<input name="hexcode" /><input type="submit" value="Create Link" /><br/>
                        File Name(Optional):<input name="hexcode" /><input type="submit" value="Create Link" /><br/>
                    </center>
            </body>
        </html>
    '''


#application = default_app()
run(host='0.0.0.0', port=8080)



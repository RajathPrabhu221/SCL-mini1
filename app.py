from flask import Flask, render_template
import requests
import json


app= Flask(__name__)

@app.route('/')
def synonym():
	params = {'api_key': 'aa714afb26mshadc5a2c5d8fe45cp1e76b1jsn7282425dc7b5'}
	r=requests.get('wordsapiv1.p.rapidapi.com',params=params)
	return render_template('synonyms.html', synonyms=json.loads(r.text)['movies'])

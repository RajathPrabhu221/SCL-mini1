from flask import Flask, render_template
import requests
import json
import pdb

app= Flask(__name__)

@app.route('/')
def home_page():
	render_template('index.html')
	

@app.route('/antonyms')
def antonyms():
	return render_template('Antonym.html')

@app.route('/synonyms')
def synonyms():
	# params = {'api_key': 'aa714afb26mshadc5a2c5d8fe45cp1e76b1jsn7282425dc7b5'}
	# r=requests.get('wordsapiv1.p.rapidapi.com',params=params)
	return render_template('synonyms.html', synonyms=json.loads(r.text)['synonyms'])
	
@app.route('/form')
def report():
    return render_template('report.html')

@app.route("/synans")
def synans():
	params = {'api_key': 'aa714afb26mshadc5a2c5d8fe45cp1e76b1jsn7282425dc7b5'}
	r=requests.get('wordsapiv1.p.rapidapi.com',params=params)
	pdb.run()


	

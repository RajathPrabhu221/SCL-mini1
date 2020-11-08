from flask import Flask, render_template, request
import json
import urllib

app= Flask(__name__)


def gen(word, generation_type):
	link = "http://api.datamuse.com/words?rel_"+ generation_type + "=" + word
	response = urllib.request.urlopen(link)
	data = json.loads(response.read())
	list_responses = list()
	if len(data) == 0:
		return list_responses.append('404')
	for i in data:
		list_responses.append(i["word"])
	return list_responses


#-------------------- Routing -------------------------------------------------------------------

@app.route('/')
def home_page():
	return render_template('index.html')
	

@app.route('/antonyms')
def antonyms():
	return render_template('Antonym.html')

@app.route('/antonym_gen',methods = ['POST'])
def antonym_gen():
	word = request.form['word']
	list_of_antonym = gen(word ,"ant")
	return render_template('Antonym.html',list_of_antonym)

@app.route('/synonyms')
def synonyms():
	return render_template('synonyms.html')

@app.route('/synonym_gen', methods = ['POST'])
def synonym_gen():
	word = request.form['word']
	list_of_synonyms = gen(word, "syn")
	return render_template('synonynms.html',list_of_synonyms)

@app.route('/form')
def report():
    return render_template('report.html')

#------------------------------------------------------------------------------------------------------

	
if __name__ == '__main__':
	app.run(host = "localhost", port = 5000)
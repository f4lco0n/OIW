from app import app
from flask import Flask, jsonify, request

languages = [{'name': 'JavaScript',"level" : "expert"}, 
			 {"name": 'Python',"level": "medium"}, 
			 {"name": 'C++',"level": "medium"},
			 {"name": "C#","level": "easy"}, 
			 {"name": "PHP", "level": "that's not programming language"}, 
			 {"name": "C", "level": "hard"},
			 {"name": "Prolog", "level": "easy"}]



@app.route('/', methods=['GET'])
def test():
	return jsonify({'message': 'Add /lang to your URL!!!'})

@app.route('/lang', methods=['GET'])
def returnLanguages():
	return jsonify({'languages': languages})



@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
	langs = [language for language in languages if language['name'] == name]
	return jsonify({'language': langs[0]})

@app.route('/lang', methods=['POST'])
def addOne():
	language = {'name' : request.get_json(force=True).get('name'), 'level' : request.get_json(force=True).get('level')}

	languages.append(language)
	return jsonify({'languages': languages})

@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
	langs = [language for language in languages if language['name'] == name]
	langs[0]['name'] = request.get_json(force=True).get('name')
	return jsonify({'language': langs[0]})

@app.route('/lang/<string:name>', methods=['DELETE'])
def removeONe(name):
	lang = [language for language in languages if language['name'] == name]
	languages.remove(lang[0])
	return jsonify({'language': languages})
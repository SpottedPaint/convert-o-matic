from flask import Flask, render_template, request, session, jsonify, send_from_directory
import re, convertor, sqlite3, logging, random, os
app = Flask(__name__)

from logging import FileHandler
file_handler = FileHandler('error.log')
file_handler.setLevel(logging.ERROR)
app.logger.addHandler(file_handler)

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]L(**(^WX/,?RT'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
@app.route('/json/<question>')
def hello_world(question=None):
	#return question
	if not 'userId' in session:
		session['userId'] = random.randint(1,1953884345)

	output = {}
	output['input'] = question or request.args.get('question', '')
	dimensions = re.sub(r'[^0-9.]', '', output['input'])
	units = re.sub(r'[^a-zA-Z"\']', ' ', output['input'].lower())
	words = units.split()
	found = False
	
	for word in words:
		found = word in convertor.options
		#print "-" + word + " %s" % found
		if found:
			break
	
	if output['input'] == '':
		output['output'] = """Enter your dimension e.g. 384400000 m"""
	elif not found:
		output['output'] = "Sorry we can't convert the number '%(dimensions)s' you could tell us the units you are using." % {'dimensions':dimensions}
	else:
		output['output'] = convertor.options[word](dimensions) 
		logRequest(output['input'],output['output'])
	
	output['recent'] = dumpRequest()
	
	if question:
		return jsonify(output)
	else:
		return render_template('index.html', output=output)

def logRequest(question,output):
	db = sqlite3.connect('log.db')
	c = db.cursor()
	#c.execute('''DROP TABLE log ''')
	#c.execute('''DELETE FROM log ''')
	#c.execute('''
	#ALTER TABLE log ADD COLUMN userId INTEGER NOT NULL DEFAULT 1
	#''')
	#db.commit()
	#c.execute('''
	#CREATE TABLE log (
	#id INTEGER PRIMARY KEY AUTOINCREMENT, 
	#userId INTEGER NOT NULL DEFAULT 1,
	#datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
	#question VARCHAR,
	#output VARCHAR
	#)''')
	c.execute("INSERT INTO log (question,output,userId) VALUES (:question,:output,:userId)",{"question": question, "output": output, "userId": session['userId'] })
	db.commit()
	c.close()
	return True;

def dumpRequest():
	db = sqlite3.connect('log.db')
	c = db.cursor()
	c.execute("SELECT question,output,userId FROM log ORDER BY datetime DESC LIMIT 5")
	rows = c.fetchall()
	c.close()
	return rows

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/why')
def hello():
	return """
	Q: why?\n\n
	Answer: I'm learning me some python and wanted to go through whole process of setting up little site.
	"""
	
if __name__ == '__main__':
    app.run()
    #debug=True
    
#if not app.debug:
    #import logging
    #from logging.handlers import FileHandler
    #file_handler = FileHandler('log.txt')
    #file_handler.setLevel(logging.WARNING)
    #app.logger.addHandler(file_handler)


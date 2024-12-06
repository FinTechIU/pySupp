from flask import Flask, render_template, redirect, request, session
from random import randint

app = Flask(__name__)

@app.route('/')
def index():
	x = randint(1, 10)
	return render_template('index.html', title='This will be the page title!', copies=x, copy_text='See me!')

@app.route('/get')
def get():
	if 'username' in request.args:
		s = '''GET params: (look at the url!)<br>'''
		for item in request.args:
			s += item + ': ' + request.args[item] + '<br>'
		return s
	return render_template('form.html', name='GET demo', method='GET')

@app.route('/post', methods=['GET', 'POST'])
def post():
	if request.method == 'POST':
		s = '''POST form:<br>'''
		for item in request.form:
			s += item + ': ' + request.form[item] + '<br>'
		return s
	return render_template('form.html', name='POST demo', method='POST')
	return ''
	
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template, redirect, request, session, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html>
    <head>
    <title>Flask Demo</title>
    </head>
    <body>
    Hello, World!
    </body>
</html>'''

app.add_url_rule('/url-rule', view_func=lambda: '/url-rule route!')

@app.route('/redirect301')
def redirect_301():
    return redirect(url_for('redirect_to'), 301)

@app.route('/redirect302')
def redirect_302():
    return redirect(url_for('redirect_to'), 302)

@app.route('/redirect_to')
def redirect_to():
    return 'Success!'

@app.route('/error')
def err_example():
    var = None
    return var['invalid-key']

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)


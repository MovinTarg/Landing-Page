from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='Pete')

@app.route('/ninjas')
def ninja():
    return render_template('ninjas.html')

@app.route('/dojo/new')
def forms():
    return render_template('dojos.html')

app.run(debug=True)
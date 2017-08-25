from flask import Flask,render_template, request,json, redirect, url_for
import os
app = Flask(__name__)
 
@app.route("/", methods=['GET'])
def home():
	if request.method == 'GET':
		return render_template('index.html')
    
@app.route("/login", methods=['POST'])
def login():
	if request.method == 'POST':
		user = request.form['username']
		pwd = request.form['password']
		return redirect(url_for('dashboard'))

@app.route("/dashboard", methods=['GET'])
def dashboard():
		return render_template('dashboard.html')

@app.route("/logout", methods=['GET'])
def logout():
	return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
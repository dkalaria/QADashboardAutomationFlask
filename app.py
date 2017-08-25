from flask import Flask,render_template, request,json, redirect, url_for
import os
import sys
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

# @app.route("/getJenkinsData", methods=['GET'])
# def getJenkinsData():
# 	return JenkinController.get_jenkin_job_test_results(JenkinController(),JenkinController().get_jenkin_user_auth(JenkinController(),'DKalaria','Jalebi@123'), base_url, "stg2-investor-platform-order-tests",)
	
if __name__ == "__main__":
    sys.path.append('./service')
    app.run(debug=True)
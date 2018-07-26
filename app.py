from flask import Flask,render_template, request,json, redirect, url_for
import os
import sys
from service.jenkin_api import JenkinController
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

@app.route("/getJenkinsData", methods=['GET'])
def getJenkinsData():
	base_url="https://jenkins.prosper.com/job/Investor/job/QA"
	return JenkinController.get_jenkin_job_test_results_with_auth(base_url,
															 "stg2-investor-platform-order-tests",
															 "",
															 "")
	# return JenkinController.get_jenkin_job_test_results(JenkinController(),JenkinController().get_jenkin_user_auth(JenkinController(),'',''), base_url, "stg2-investor-platform-order-tests",)

@app.route("/getJenkinsJobsList", methods=['GET'])
def getJenkinsJobsList():
	base_url="https://jenkins.prosper.com/job/Investor/job/QA"
	return JenkinController.get_jenkin_jobs_list_with_user_auth(base_url,
																"",
																"")

if __name__ == "__main__":
    sys.path.append('./service')
    app.run(debug=True)

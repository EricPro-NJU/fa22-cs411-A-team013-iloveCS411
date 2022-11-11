""" Specifies routing for the application"""
from flask import render_template, request, jsonify, flash, session, redirect, url_for
from app import app
from app import database as db_helper

# needed to use sessions
app.secret_key = "this is a great secret key"

@app.route("/")
def homepage():
    """ returns rendered homepage """

    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.pop('_flashes', None) #clear flash message
    netId = request.form.get("netId")
    password = request.form.get("password")
    ret = db_helper.login(netId, password)
    '''
    if ret == 2:
        result = {'success': False, 'response': 'User Not Found (NetId: {})'.format(netId)}
    elif ret == 3:
        result = {'success': False, 'response': 'Password incorrect (NetId: {})'.format(netId)}
    else:
        result = {'success': True, 'response': 'Login Success. Your NetId is {}, UserType {}.'.format(netId, 'Student' if ret==0 else 'Professor')}
    return jsonify(result)
    '''
    #after log in, determine if student account or prof account, then render the according home page (not for midterm demo)
    if ret == 0: #success login for student
        flash("login successful")
        session["username"] = netId
        return redirect(url_for("student"))
    elif ret == 1: #success login for faculty
        flash("login successful")
        session["username"] = netId
        return redirect(url_for("faculty"))
    else: #wrong login credentials
        flash("Invalid netId or password!")
        return redirect(url_for("homepage"))


#this is student home page
@app.route("/student", methods=["GET", "POST"])
def student():
    netId = session["username"]
    semester = 'SP23' #this is the current semester
    ret  = db_helper.show_schedule(netId, semester)
    return render_template("student.html", enrolled = ret)

#for drop courses
@app.route("/drop/<string:drop_crn>/", methods=["GET", "POST"])
def drop(drop_crn):
    netId = session["username"]
    CRN = drop_crn
    ret = db_helper.drop(netId, CRN)
    flash("Course dropped successfully")
    return redirect(url_for("student")) #direct to register page


#for change course credit
@app.route("/update_cred/<string:crn>/", methods=["GET", "POST"])
def update_cred(crn):
    netId = session["username"]
    new_cred = request.form.get("new_cred")
    ret = db_helper.change_credit(netId, crn, new_cred)
    if ret == 0:
        flash("Credit update was successful")
    else:
        flash("Credit update was unsuccessful")
    return redirect(url_for("student")) #direct to register page

#faculty home page
@app.route("/history", methods=["GET", "POST"])
def history():
    #todo
    return render_template("history.html")


#faculty home page
@app.route("/faculty", methods=['POST'])
def faculty():
    #todo
    return render_template("faculty.html")


#log out page
@app.route("/logout/")
def unlogger():
	# if logged in, log out, otherwise offer to log in
	if "username" in session:
		# note, here were calling the .clear() method for the python dictionary builtin
		session.clear()
		return render_template("logout.html")
	else:
		return redirect(url_for("homepage"))

@app.route('/explorer')
def explorer():
    return render_template('explorer.html')

@app.route('/search', methods=['POST'])
def search():
    input = request.get_json()['keyword']
    data = db_helper.keyword_course_search(input)
    return jsonify(data)

@app.route('/getSections', methods=['POST'])
def getSections():
    input = request.get_json()['section']
    data = db_helper.show_sections(input)
    return jsonify(data)

@app.route('/enroll', methods=['POST'])
def enroll():
    resp = request.get_json()
    data = db_helper.enroll(resp['netid'], resp['CRN'])
    return jsonify(data)

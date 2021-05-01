from flask import Flask, render_template, request
app = Flask(__name__)

# May be we should add a default branch? Or make this work for default as well
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    name = request.form.get("name")
    email_address = request.form.get("email_address")
    note = request.form.get("note")

    isValid, err = isValidRequest(request.form) 
    if not isValid:
        return "Error: {}".format(err), 400
    return "", 200

# private methods
def isValidRequest(params):
    email = params.get("email_address", False) 
    if not params.get("name", False):
        return False, "A name is required"
    if not email:
        return False, "An email is required"
    if isValidEmail(email) == False:
        return False, "Email must be formatted like characters + @ + characters"
    return True, ""

def isValidEmail(email):
    if len(email.split("@")) == 2:
        return True
    return False

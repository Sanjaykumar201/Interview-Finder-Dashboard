from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = "secret"
app.config['UPLOAD_FOLDER'] = "uploads"

applications = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        session['name'] = request.form['name']
        session['age'] = request.form['age']
        session['college'] = request.form['college']
        session['stream'] = request.form['stream']
        session['interest'] = request.form['interest']
        return redirect("/domain")
    return render_template("profile.html")

@app.route("/domain", methods=["GET", "POST"])
def domain():
    if request.method == "POST":
        domain = request.form['domain']
        if domain.lower() not in ["frontend", "backend", "web development", "graphic designer"]:
            return render_template("domain.html", error="Enter valid domain only")
        session['domain'] = domain
        return redirect("/companies")
    return render_template("domain.html")

@app.route("/companies")
def companies():
    company_list = [
        {"name": "Company A", "role": "Frontend Developer", "type": "Online", "pay": "Unpaid"},
        {"name": "Company B", "role": "Backend Developer", "type": "Online", "pay": "Unpaid"},
        {"name": "Company C", "role": "Web Developer", "type": "Online", "pay": "Unpaid"},
        {"name": "Company D", "role": "Graphic Designer", "type": "Online", "pay": "Unpaid"},
    ]
    return render_template("companies.html", companies=company_list)

@app.route("/apply/<company>")
def apply(company):
    session['company'] = company
    return render_template("apply.html", company=company)

@app.route("/submit", methods=["POST"])
def submit():
    file = request.files['resume']
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    data = {
        "name": session.get('name'),
        "company": session.get('company')
    }
    applications.append(data)
    return redirect("/success")

@app.route("/success")
def success():
    return render_template("success.html", name=session.get('name'), company=session.get('company'))

@app.route("/applications")
def applications_view():
    return render_template("applications.html", apps=applications)

if __name__ == "__main__":
    app.run(debug=True)
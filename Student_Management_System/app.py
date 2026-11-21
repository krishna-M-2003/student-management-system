from flask import Flask, render_template, redirect

# Create Flask application
app = Flask(__name__)

students = [
    {"name": "Arun", "age": 21, "email": "arun@gmail.com", "course": "Python"},
    {"name": "Priya", "age": 22, "email": "priya@gmail.com", "course": "Java"},
    {"name": "Karthik", "age": 20, "email": "karthik@gmail.com", "course": "Python"},
    {"name": "Divya", "age": 23, "email": "divya@gmail.com", "course": "HTML"},
    {"name": "Rahul", "age": 21, "email": "rahul@gmail.com", "course": "CSS"},
    {"name": "Sneha", "age": 22, "email": "sneha@gmail.com", "course": "JavaScript"},
    {"name": "Vijay", "age": 24, "email": "vijay@gmail.com", "course": "Python"},
    {"name": "Meena", "age": 20, "email": "meena@gmail.com", "course": "SQL"},
    {"name": "Ajay", "age": 23, "email": "ajay@gmail.com", "course": "Flask"},
    {"name": "Nisha", "age": 21, "email": "nisha@gmail.com", "course": "Bootstrap"}
]

# Create LoginPage route
@app.route('/')
def LoginPage():
    return render_template('LoginPage.html')

# Create DashboardPage route
@app.route("/dashboard")
def Dashboard():
    return render_template('Dashboard.html', students=students)

# @app.route('/login')
# def Login():
#     return redirect('/dashboard')

if __name__ == "__main__":
    app.run(debug=True)
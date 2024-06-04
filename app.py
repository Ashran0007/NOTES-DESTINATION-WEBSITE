from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to connect to SQLite database
def connect_db():
    conn = sqlite3.connect('database.db')
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        name TEXT NOT NULL,
                        phone TEXT NOT NULL,
                        university TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

create_table()


# Route for home page
@app.route('/')
def home():
    return render_template('home.html')
# @app.route('/signup')
# def signup():
#     return render_template('signup.html')

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("login working")
        email = request.form['email']
        password = request.form['password']
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            return redirect(url_for('course'))
        else:
            return "Invalid email or password. Please try again."
    return render_template('home.html')

# Route for signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        phone = request.form['phone']
        university = request.form['university']
       
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (email, password,name,phone,university) VALUES (?, ?,?,?,?)", (email, password,name,phone,university))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))
    return render_template('signup.html')

# Route for course page
@app.route('/course')
def course():
    return render_template('course.html')

@app.route('/bcasem')
def bcasem():
    return render_template('bcasem.html')

@app.route('/bcasem1')
def bcasem1():
    return render_template('bcasem1.html')

@app.route('/bcasem2')
def bcasem2():
    return render_template('bcasem2.html')

@app.route('/bcasem3')
def bcasem3():
    return render_template('bcasem3.html')
    
@app.route('/bcasem4')
def bcasem4():
    return render_template('bcasem4.html')

@app.route('/bcasem5')
def bcasem5():
    return render_template('bcasem5.html')

@app.route('/bcasem6')
def bcasem6():
    return render_template('bcasem6.html')
    


@app.route('/admin')
def admin():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return render_template('admin.html', users=users)

@app.route('/logout')
def logout():
    # Your logout logic goes here...
    # For example, clearing session data or other authentication related tasks.
    # Then, redirect to the home page.
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

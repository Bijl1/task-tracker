from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Create a helper function for database operations
def execute_query(query, args=()):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    conn.close()

# Database initialization
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            description TEXT NOT NULL,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Routes
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('tasks'))
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        
        query = 'INSERT INTO users (username, password) VALUES (?, ?)'
        execute_query(query, (username, hashed_password))

        flash('Account created successfully. Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, username, password FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()
        
        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            return redirect(url_for('tasks'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/tasks')
def tasks():
    if 'user_id' in session:
        user_id = session['user_id']
        
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE user_id = ?', (user_id,))
        tasks = cursor.fetchall()
        conn.close()
        
        return render_template('tasks.html', tasks=tasks)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/create_task', methods=['GET', 'POST'])
def create_task():
    if 'user_id' in session:
        if request.method == 'POST':
            name = request.form['name']
            date = request.form['date']
            time = request.form['time']
            description = request.form['description']
            user_id = session['user_id']

            query = 'INSERT INTO tasks (name, date, time, description, user_id) VALUES (?, ?, ?, ?, ?)'
            execute_query(query, (name, date, time, description, user_id))

            flash('Task created successfully.', 'success')
            return redirect(url_for('tasks'))

        return render_template('create_task.html')

    return redirect(url_for('login'))

@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if 'user_id' in session:
        if request.method == 'POST':
            name = request.form['name']
            date = request.form['date']
            time = request.form['time']
            description = request.form['description']
            user_id = session['user_id']

            query = 'UPDATE tasks SET name=?, date=?, time=?, description=? WHERE id=? AND user_id=?'
            execute_query(query, (name, date, time, description, task_id, user_id))

            flash('Task updated successfully.', 'success')
            return redirect(url_for('tasks'))

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE id=? AND user_id=?', (task_id, session['user_id']))
        task = cursor.fetchone()
        conn.close()

        if task:
            return render_template('edit_task.html', task=task)
        else:
            flash('Task not found or you do not have permission to edit it.', 'danger')
            return redirect(url_for('tasks'))

    return redirect(url_for('login'))

@app.route('/delete_task/<int:task_id>', methods=['GET', 'POST'])
def delete_task(task_id):
    if 'user_id' in session:
        query = 'DELETE FROM tasks WHERE id=? AND user_id=?'
        execute_query(query, (task_id, session['user_id']))

        flash('Task deleted successfully.', 'success')
        return redirect(url_for('tasks'))

    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

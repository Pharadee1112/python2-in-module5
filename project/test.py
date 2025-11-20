from flask import Flask, request, render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('add.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    borrow_date = request.form['borrow_date']
    email = request.form['email']
    
    # Save data ลง CSV
    with open('user.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, borrow_date])
    
    return f"Data received! Name: {name}, Email: {email}, Borrow date: {borrow_date}"

if __name__ == '__main__':
    app.run(debug=True)

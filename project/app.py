from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# หน้าแรก
@app.route('/')
def main():
    return render_template('main.html')

# หน้า Home
@app.route('/home')
def home():
    return render_template('home.html')

# หน้า Books
@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/labye')
def labye():
    return render_template('labye.html')

@app.route('/borrowpages')
def borrowpages():
    return render_template('borrowpages.html')

# รับข้อมูล form
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    borrow_date = request.form['borrow_date']
    email = request.form['email']

    # คุณสามารถบันทึกลงไฟล์ หรือ database ได้ที่นี่
    print(f"{name} | {borrow_date} | {email}")  # แค่โชว์ใน console

    return redirect(url_for('success'))

# หน้า success
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)
